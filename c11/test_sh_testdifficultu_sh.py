"""
test_sh_testdifficultu_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh testdifficultu.sh' 'test_sh_testdifficultu_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command

IGNORE_PATTERNS = ['Ran 1 test in (0.[0-9]+)s']

class Test_SH_TESTDIFFICULTU(ReferenceTestCase):
    command = 'sh testdifficultu.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_testdifficultu_sh')

    generated_files = [
        os.path.join(cwd, 'testdifficultu.txt'),
    os.path.join(cwd, 'testdifficultu.txt.tex')
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
                                 os.path.join(self.refdir, 'STDOUT'),
                                 ignore_patterns=IGNORE_PATTERNS)

    def test_stderr(self):
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'))

    def test_testdifficultu_txt(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
        ]
        self.assertTextFileCorrect(os.path.join(self.cwd, 'testdifficultu.txt'),
                                   os.path.join(self.refdir, 'testdifficultu.txt'),
                                   ignore_substrings=substrings,
                                   ignore_patterns=IGNORE_PATTERNS,
                                   encoding='ascii')

    def test_testdifficultu_txt_tex(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
        ]
        self.assertTextFileCorrect(os.path.join(self.cwd, 'testdifficultu.txt.tex'),
                                   os.path.join(self.refdir, 'testdifficultu.txt.tex'),
                                   ignore_substrings=substrings,
                                   ignore_patterns=IGNORE_PATTERNS,
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
