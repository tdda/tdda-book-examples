"""
test_discover_us.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh discover-us.sh' 'test_discover_us.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_DISCOVER_US(ReferenceTestCase):
    command = 'sh discover-us.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'discover_us')

    generated_files = [
        os.path.join(cwd, 'us-states-count.tdda')
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

    def test_us_states_count_tdda(self):
        substrings = [
            '2025-08-24',
            'gardot.local',
            'njr',
        ]
        # added by hand
        lines = [
            '"local_time":',
            '"utc_time":',
            '"creator":',
            '"host":',
            '"user":',
        ]
        self.assertTextFileCorrect(os.path.join(self.cwd, 'us-states-count.tdda'),
                                   os.path.join(self.refdir, 'us-states-count.tdda'),
                                   ignore_substrings=substrings,
                                   ignore_lines = lines,
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
