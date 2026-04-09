"""
test_verify_book_ex13.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'tdda verify accounts1k.csv accounts.tdda' 'test_verify_book_ex13.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_VERIFY_BOOK_EX13(ReferenceTestCase):
    command = 'tdda verify accounts1k.csv accounts.tdda'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'verify_book_ex13')


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
        self.assertEqual(self.exit_code, 0)

    def test_stdout(self):
        self.assertStringCorrect(self.output,
                                 os.path.join(self.refdir, 'STDOUT'))

    def test_stderr(self):
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'))

if __name__ == '__main__':
    ReferenceTestCase.main()
