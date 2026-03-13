"""
test_python_pydantic_bookdata_py.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest --non-zero-exit 'python pydantic_bookdata.py' 'test_python_pydantic_bookdata_py.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PYTHON_PYDANTIC_BOOKDATA_PY(ReferenceTestCase):
    command = 'python pydantic_bookdata.py'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'python_pydantic_bookdata_py')


    @classmethod
    def setUpClass(cls):
        
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
        self.assertStringCorrect(self.output,
                                 os.path.join(self.refdir, 'STDOUT'))

    def test_stderr(self):
        substrings = [
            '/Users/njr/books/tdda-book-examples/c8',
        ]
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'),
                                 ignore_substrings=substrings)

if __name__ == '__main__':
    ReferenceTestCase.main()
