"""
test_pqrecords.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'python countpqrecords.py us-states.parquet us-states-count.csv' 'test_pqrecords.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PQRECORDS(ReferenceTestCase):
    command = 'python countpqrecords.py us-states.parquet us-states-count.csv'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'pqrecords')

    generated_files = [
        os.path.join(cwd, 'us-states-count.csv')
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

    def test_us_states_count_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'us-states-count.csv'),
                                   os.path.join(self.refdir, 'us-states-count.csv'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
