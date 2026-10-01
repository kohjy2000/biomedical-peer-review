"""Synthetic end-to-end checks for template provenance and delivery rejection."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

from pypdf import PdfWriter

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/review_run.py'
spec = importlib.util.spec_from_file_location('review_run', SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
REPORT = '''## Overall Assessment

The contribution is useful, with one interpretation requiring correction.

## Major Comments

### 1. Interpretation of the comparison

The comparison does not establish the proposed mechanism; narrow that claim.

## Minor Comments

- Figure 1: define the unit in the axis label.

## Recommendation

Major revision, with source-based corrections.
'''


class TemplateDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.pdf = self.root / 'fixture.pdf'
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        writer.write(self.pdf)
        self.plan = self.root / 'visual-plan.json'
        self.plan.write_text(json.dumps({'coverage_note': 'Synthetic blank-page fixture; no scientific evidence.', 'pages': []}))

    def prepare(self, template=None, original=None, basis=None, recommendation=False):
        args = SimpleNamespace(template=template, template_original=original, template_basis=basis,
                               recommendation=recommendation, visual_plan=self.plan,
                               run=self.root / 'run', pdf=[self.pdf], model='synthetic-test',
                               effort='high', journal='Fixture', cutoff='2026-10-01', language='English')
        with contextlib.redirect_stdout(io.StringIO()):
            runner.prepare(args)
        return args.run

    def delivery_args(self, run, report=REPORT):
        for name, text in [('draft.md', 'Untouched synthetic draft.'), ('full.md', report),
                           ('review.md', report), ('notes.md', 'Synthetic host comparison record; no scientific validation is claimed.')]:
            (self.root / name).write_text(text)
        return SimpleNamespace(draft=self.root / 'draft.md', full_review=self.root / 'full.md',
                               review=self.root / 'review.md', notes=self.root / 'notes.md',
                               template=run / 'provenance/review-template.md',
                               manifest=run / 'manifest.json', out=self.root / 'delivery')

    def finalize(self, args):
        with contextlib.redirect_stdout(io.StringIO()):
            runner.finalize(args)
        return json.loads((args.out / 'finalization.json').read_text())

    def assert_rejected(self, args):
        with self.assertRaises(ValueError):
            self.finalize(args)
        self.assertFalse(args.out.exists(), 'Invalid report must not create a delivery directory')

    def test_default_report_finalizes_and_keeps_template_record(self):
        run = self.prepare(recommendation=True)
        args = self.delivery_args(run)
        saved = self.finalize(args)
        self.assertEqual((args.out / 'peer-review.md').read_text(), REPORT)
        self.assertIn('template-record.json', saved['files'])
        self.assertIn('template-manifest.json', saved['files'])
        self.assertEqual(saved['verification']['template_integrity'], 'passed')
        self.assertIn('Passed default', saved['verification']['template_structure'])
        self.assertIn('not automatically assessed', saved['verification']['scientific_content'])

    def test_questionnaire_rejected_under_default_contract(self):
        run = self.prepare()
        report = '\n\n'.join(f'## Q{i}\n\nAnswer.' for i in range(1, 8))
        self.assert_rejected(self.delivery_args(run, report))

    def test_missing_minor_section_rejected(self):
        run = self.prepare()
        report = REPORT.replace('## Minor Comments\n\n- Figure 1: define the unit in the axis label.\n\n', '')
        self.assert_rejected(self.delivery_args(run, report))

    def test_reordered_core_sections_rejected(self):
        run = self.prepare()
        report = REPORT.replace('## Overall Assessment', '## TEMP').replace('## Major Comments', '## Overall Assessment').replace('## TEMP', '## Major Comments')
        self.assert_rejected(self.delivery_args(run, report))

    def test_requested_recommendation_is_required(self):
        run = self.prepare(recommendation=True)
        self.assert_rejected(self.delivery_args(run, REPORT.split('## Recommendation')[0]))

    def test_unrequested_recommendation_can_be_omitted(self):
        run = self.prepare()
        args = self.delivery_args(run, REPORT.split('## Recommendation')[0])
        self.finalize(args)
        self.assertTrue(args.out.exists())

    def test_changed_template_rejected(self):
        run = self.prepare()
        args = self.delivery_args(run)
        args.template.write_text('A replacement chosen after writing.\n')
        self.assert_rejected(args)

    def test_changed_selection_record_rejected(self):
        run = self.prepare()
        args = self.delivery_args(run)
        path = run / 'provenance/template-record.json'
        record = json.loads(path.read_text())
        record['template_supplied'] = True
        path.write_text(json.dumps(record))
        self.assert_rejected(args)

    def test_override_requires_original_and_basis_before_preparation(self):
        template = self.root / 'supplied.md'
        template.write_text('## Summary\n\n## Concerns\n')
        with self.assertRaisesRegex(ValueError, 'template-original'):
            self.prepare(template=template)
        self.assertFalse((self.root / 'run').exists())

    def test_supplied_format_preserves_binary_original_without_false_auto_pass(self):
        template = self.root / 'supplied.md'
        template.write_text('## Summary\n\n## Concerns\n')
        run = self.prepare(template=template, original=self.pdf,
                           basis='Synthetic explicit user-supplied report format; no conflicting prior format.')
        args = self.delivery_args(run, '## Summary\n\nSupported contribution.\n\n## Concerns\n\nOne correction.\n')
        saved = self.finalize(args)
        self.assertEqual((args.out / 'template-original.pdf').read_bytes(), self.pdf.read_bytes())
        self.assertIn('not automatically assessed', saved['verification']['template_structure'])

    def test_changed_preserved_original_rejected(self):
        template = self.root / 'supplied.md'
        template.write_text('## Summary\n')
        run = self.prepare(template=template, original=template, basis='Synthetic supplied format.')
        args = self.delivery_args(run, '## Summary\n\nA finding.\n')
        (run / 'provenance/template-original.md').write_text('Changed original.\n')
        self.assert_rejected(args)

    def test_existing_delivery_is_preserved_on_repeat(self):
        run = self.prepare()
        args = self.delivery_args(run)
        self.finalize(args)
        before = {p.name: p.read_bytes() for p in args.out.iterdir()}
        self.finalize(args)
        self.assertEqual({p.name: p.read_bytes() for p in args.out.iterdir()}, before)

    def test_word_target_is_not_a_hard_cap(self):
        run = self.prepare()
        report = REPORT.replace('narrow that claim.', 'narrow that claim. ' + 'context ' * 1500)
        args = self.delivery_args(run, report)
        self.finalize(args)
        self.assertEqual((args.out / 'peer-review.md').read_text(), report)


if __name__ == '__main__':
    unittest.main()
