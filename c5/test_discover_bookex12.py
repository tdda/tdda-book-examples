"""
test_discover_bookex12.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'tdda discover -xG accounts1k.csv accounts.tdda' 'test_discover_bookex12.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_DISCOVER_BOOKEX12(ReferenceTestCase):
    command = 'tdda discover -xG accounts1k.csv accounts.tdda'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'discover_bookex12')

    generated_files = [
        os.path.join(cwd, 'accounts.tdda')
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

    def test_accounts_tdda(self):
        patterns = [
            r'^        "local_time": "2026\-04\-09T09:03:[0-9]{2}",$',
            r'^        "utc_time": "2026\-04\-09T08:03:[0-9]{2}\+00:00",$',
        ]
        substrings = [
            '2026-04-09',
            'gardot.local',
            'njr',
            'creator',
        ]
        self.assertTextFileCorrect(os.path.join(self.cwd, 'accounts.tdda'),
                                   os.path.join(self.refdir, 'accounts.tdda'),
                                   ignore_patterns=patterns,
                                   ignore_substrings=substrings,
                                   encoding='MacRoman')

if __name__ == '__main__':
    ReferenceTestCase.main()
