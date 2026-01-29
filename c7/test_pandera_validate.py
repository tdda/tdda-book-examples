"""
test_pandera_validate.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh pandera_books_validate.sh' 'test_pandera_validate.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PANDERA_VALIDATE(ReferenceTestCase):
    command = 'sh pandera_books_validate.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'pandera_validate')

    generated_files = [
        os.path.join(cwd, 'pandera_books_results.json'),
    os.path.join(cwd, 'pbr-actual-expanded.json'),
    os.path.join(cwd, 'pbr-ref-expanded.json')
    ]
    @classmethod
    def setUpClass(cls):
        for path in cls.generated_files:
            if os.path.exists(path):
                os.unlink(path)
        (cls.output,
         cls.error,
         cls.exception,
         cls.exit_code,
         cls.duration) = exec_command(cls.command, cls.cwd)

    def test_no_exception(self):
        self.assertIsNone(self.exception)

    def test_exit_code(self):
        self.assertEqual(self.exit_code, 0)

    def test_stdout(self):
        self.assertStringCorrect(self.output,
                                 os.path.join(self.refdir, 'STDOUT'))

    def test_stderr(self):
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'))

    def test_pandera_books_results_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pandera_books_results.json'),
                                   os.path.join(self.refdir, 'pandera_books_results.json'),
                                   encoding='ascii')

    def test_pbr_actual_expanded_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pbr-actual-expanded.json'),
                                   os.path.join(self.refdir, 'pbr-actual-expanded.json'),
                                   encoding='ascii')

    def test_pbr_ref_expanded_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pbr-ref-expanded.json'),
                                   os.path.join(self.refdir, 'pbr-ref-expanded.json'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
