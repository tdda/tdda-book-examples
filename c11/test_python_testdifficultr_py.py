"""
test_python_testdifficultr_py.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest --non-zero-exit 'python testdifficultr.py' 'test_python_testdifficultr_py.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PYTHON_TESTDIFFICULTR(ReferenceTestCase):
    command = 'python testdifficultr.py'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'python_testdifficultr_py')
    orig_tmpdir = '/var/folders/2y/72gfd2691h9gf2cy48xp8slh0000gn/T/tmp0nh3653n'
    if not os.environ.get('TMPDIR_SET_BY_GENTEST'):
        tmpdir = tempfile.mkdtemp()
        os.environ['TMPDIR'] = tmpdir
        os.environ['TMPDIR_SET_BY_GENTEST'] = 'true'
    else:
        tmpdir = os.environ['TMPDIR']
    
    generated_files = [
        os.path.join(tmpdir, 'actual-alice.txt'),
    os.path.join(tmpdir, 'actual-raw-alice.txt'),
    os.path.join(tmpdir, 'expected-alice.txt')
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
        self.assertEqual(self.exit_code, 1)

    def test_stdout(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
            self.orig_tmpdir,
        ]
        self.assertStringCorrect(self.output,
                                 os.path.join(self.refdir, 'STDOUT'),
                                 ignore_substrings=substrings)

    def test_stderr(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
            self.orig_tmpdir,
        ]
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'),
                                 ignore_substrings=substrings)

    def test_actual_alice_txt(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
            self.orig_tmpdir,
        ]
        self.assertTextFileCorrect(os.path.join(self.tmpdir, 'actual-alice.txt'),
                                   os.path.join(self.refdir, 'actual-alice.txt'),
                                   ignore_substrings=substrings,
                                   encoding='utf-8')

    def test_actual_raw_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.tmpdir, 'actual-raw-alice.txt'),
                                   os.path.join(self.refdir, 'actual-raw-alice.txt'),
                                   encoding='utf-8')

    def test_expected_alice_txt(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c11',
            self.orig_tmpdir,
        ]
        self.assertTextFileCorrect(os.path.join(self.tmpdir, 'expected-alice.txt'),
                                   os.path.join(self.refdir, 'expected-alice.txt'),
                                   ignore_substrings=substrings,
                                   encoding='utf-8')

if __name__ == '__main__':
    ReferenceTestCase.main()
