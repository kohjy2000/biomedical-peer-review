"""Synthetic publication checks; no model, search or confidential review input."""
import contextlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from types import SimpleNamespace
import unittest
from urllib.parse import unquote

import test_template_delivery as fixtures

runner = fixtures.runner


class WorkingMaterialsTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.TemplateDeliveryTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.run = self.fixture.prepare(recommendation=True)
        # Stand in for a successful older runner; publication must not rerun it.
        frozen = self.run / 'provenance/review_run.py'
        frozen.write_text('# preserved earlier runner\n')
        manifest = runner.read(self.run / 'manifest.json')
        manifest['files']['provenance/review_run.py'] = runner.sha(frozen)
        runner.dump(self.run / 'manifest.json', manifest)
        for stage, name, text in [('baseline', 'review.md', 'Original independent review.'),
                                  ('map', 'map.md', 'Neutral claims and evidence, not a verdict.')]:
            directory = self.run / 'runs' / stage
            directory.mkdir(parents=True)
            (directory / name).write_text(text)
            runner.dump(directory / 'response.json', {'synthetic': stage})
            self.complete(stage)
        literature = self.run / 'literature'
        literature.mkdir()
        (literature / 'notes.md').write_text('Source A: abstract accessed; unresolved limitations.')
        runner.dump(literature / 'search-log.json', [{'query': 'synthetic only; no search performed'}])
        runner.dump(literature / 'seal.json', {
            'manifest_sha256': runner.sha(self.run / 'manifest.json'),
            'map_sha256': runner.sha(self.run / 'runs/map/response.json'),
            'files': {p.name: runner.sha(p) for p in literature.iterdir()}})
        for name, text in [('draft-review.md', 'Original generated draft.'),
                           ('assessment.md', 'Reassessment-stage contribution and priorities.')]:
            (self.run / name).write_text(text)
        directory = self.run / 'runs/final'
        directory.mkdir()
        runner.dump(directory / 'response.json', {'synthetic': 'final'})
        self.complete('final', deliverables={name: runner.sha(self.run / name)
                      for name in ['draft-review.md', 'assessment.md']},
                      dependencies={'literature/seal.json': runner.sha(literature / 'seal.json')})
        args = self.fixture.delivery_args(self.run)
        args.draft = self.run / 'draft-review.md'
        self.fixture.finalize(args)
        self.delivery = args.out
        self.args = SimpleNamespace(run=self.run, delivery=self.delivery, out=self.root / 'working',
                                    review_name='peer-review.md', word_review=None, literature_corrections=None)

    def complete(self, stage, **extra):
        directory = self.run / 'runs' / stage
        runner.dump(directory / 'complete.json', {'manifest_sha256': runner.sha(self.run / 'manifest.json'),
                    'files': {p.name: runner.sha(p) for p in directory.iterdir() if p.name != 'complete.json'}, **extra})

    def publish(self):
        with contextlib.redirect_stdout(io.StringIO()):
            runner.publish(self.args)

    def protected(self):
        return {str(p): p.read_bytes() for directory in [self.run, self.delivery]
                for p in directory.rglob('*') if p.is_file()}

    def test_cli_publishes_complete_bundle_from_frozen_run(self):
        protected = self.protected()
        result = subprocess.run([sys.executable, str(fixtures.SCRIPT), 'publish', '--run', str(self.run),
                                 '--delivery', str(self.delivery), '--out', str(self.args.out)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        folder = self.args.out / 'Review_materials'
        self.assertEqual((self.args.out / 'peer-review.md').read_text(), fixtures.REPORT)
        for name, source in [('claim-structure.md', self.run / 'runs/map/map.md'),
                             ('literature.md', self.run / 'literature/notes.md'),
                             ('assessment.md', self.run / 'assessment.md'),
                             ('full-review.md', self.delivery / 'full-review.md'),
                             ('editing-notes.md', self.delivery / 'editing-notes.md')]:
            self.assertEqual((folder / name).read_bytes(), source.read_bytes())
        for target in re.findall(r'\]\(([^)]+)\)', (folder / 'README.md').read_text()):
            self.assertTrue((folder / unquote(target)).exists(), target)
        self.assertEqual(self.protected(), protected)

    def test_explicit_latest_delivery_supersedes_old_run_delivery(self):
        old = self.run / 'delivery'
        old.mkdir()
        (old / 'peer-review.md').write_text('Superseded report; never select by folder guess.')
        self.publish()
        self.assertEqual((self.args.out / 'peer-review.md').read_text(), fixtures.REPORT)
        self.assertEqual((old / 'peer-review.md').read_text(), 'Superseded report; never select by folder guess.')

    def test_existing_matching_final_word_and_correction_are_linked_unchanged(self):
        self.args.review_name = 'Review comments.md'
        self.args.out.mkdir()
        report = self.args.out / self.args.review_name
        report.write_bytes((self.delivery / 'peer-review.md').read_bytes())
        word = self.args.out / 'Review comments.docx'
        word.write_bytes(b'Synthetic opaque binary; no Word validation claimed.')
        self.args.word_review = word
        corrections = self.root / 'corrections.md'
        corrections.write_text('A later metadata correction; sealed notes unchanged.')
        self.args.literature_corrections = corrections
        before = report.read_bytes(), word.read_bytes()
        self.publish()
        folder = self.args.out / 'Review_materials'
        self.assertEqual(before, (report.read_bytes(), word.read_bytes()))
        self.assertEqual((folder / 'literature-corrections.md').read_bytes(), corrections.read_bytes())
        for target in re.findall(r'\]\(([^)]+)\)', (folder / 'README.md').read_text()):
            self.assertTrue((folder / unquote(target)).exists(), target)

    def test_repeat_publication_preserves_all_bytes(self):
        self.publish()
        before = {str(p): p.read_bytes() for p in self.args.out.rglob('*') if p.is_file()}
        self.publish()
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.args.out.rglob('*') if p.is_file()})

    def test_conflicting_final_rejected_before_materials_created(self):
        self.args.out.mkdir()
        report = self.args.out / self.args.review_name
        report.write_text('A different user report.')
        with self.assertRaisesRegex(ValueError, 'Existing file differs'):
            self.publish()
        self.assertFalse((self.args.out / 'Review_materials').exists())
        self.assertEqual(report.read_text(), 'A different user report.')

    def test_missing_or_tampered_source_rejected_before_output(self):
        source = self.run / 'runs/map/map.md'
        original = source.read_bytes()
        for tamper in [False, True]:
            with self.subTest(tamper=tamper):
                source.write_text('Changed map.') if tamper else source.unlink()
                with self.assertRaises((ValueError, FileNotFoundError)):
                    self.publish()
                self.assertFalse(self.args.out.exists())
                source.write_bytes(original)

    def test_tampered_checked_delivery_rejected_before_output(self):
        (self.delivery / 'full-review.md').write_text('Unrecorded change.')
        with self.assertRaises(ValueError):
            self.publish()
        self.assertFalse(self.args.out.exists())

    def test_wrong_draft_identity_rejected_before_output(self):
        args = self.fixture.delivery_args(self.run)
        args.out = self.root / 'other-delivery'
        self.fixture.finalize(args)
        self.args.delivery = args.out
        with self.assertRaisesRegex(ValueError, 'different generated draft'):
            self.publish()
        self.assertFalse(self.args.out.exists())

    def test_changed_inputs_do_not_overwrite_published_bundle(self):
        self.publish()
        before = {str(p): p.read_bytes() for p in self.args.out.rglob('*') if p.is_file()}
        corrections = self.root / 'new-corrections.md'
        corrections.write_text('New host correction after earlier publication.')
        self.args.literature_corrections = corrections
        with self.assertRaisesRegex(ValueError, 'Published inputs differ'):
            self.publish()
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.args.out.rglob('*') if p.is_file()})

    def test_incomplete_bundle_and_preserved_directory_rejected(self):
        folder = self.args.out / 'Review_materials'
        folder.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.publish()
        self.assertEqual(list(folder.iterdir()), [])
        self.args.out = self.run
        with self.assertRaisesRegex(ValueError, 'not inside'):
            self.publish()


if __name__ == '__main__':
    unittest.main()
