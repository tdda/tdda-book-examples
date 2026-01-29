"""
test_disco_books.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh disco-books.sh' 'test_disco_books.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_DISCO_BOOKS(ReferenceTestCase):
    command = 'sh disco-books.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'disco_books')

    generated_files = [
        os.path.join(cwd, 'books.tdda')
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

    def test_books_tdda(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'books.tdda'),
                                   os.path.join(self.refdir, 'books.tdda'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
