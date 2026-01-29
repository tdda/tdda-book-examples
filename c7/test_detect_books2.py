"""
test_detect_books2.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh detect-2.sh' 'test_detect_books2.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_DETECT_BOOKS2(ReferenceTestCase):
    command = 'sh detect-2.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'detect_books2')

    generated_files = [
        os.path.join(cwd, 'bad-books-tex.txt'),
    os.path.join(cwd, 'bad-books.csv'),
    os.path.join(cwd, 'bad-books.txt')
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

    def test_bad_books_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'bad-books-tex.txt'),
                                   os.path.join(self.refdir, 'bad-books-tex.txt'),
                                   encoding='ascii')

    def test_bad_books_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'bad-books.csv'),
                                   os.path.join(self.refdir, 'bad-books.csv'),
                                   encoding='ISO-8859-9')

    def test_bad_books_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'bad-books.txt'),
                                   os.path.join(self.refdir, 'bad-books.txt'),
                                   encoding='utf-8')

if __name__ == '__main__':
    ReferenceTestCase.main()
