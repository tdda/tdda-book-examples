"""
test_disco_enhanced.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'python discover_enhanced_accounts.py accounts1k.parquet accounts-enhanced.tdda' 'test_disco_enhanced.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_DISCO_ENHANCED(ReferenceTestCase):
    command = 'python discover_enhanced_accounts.py accounts1k.parquet accounts-enhanced.tdda'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'disco_enhanced')

    generated_files = [
        os.path.join(cwd, 'accounts-enhanced.tdda')
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

    def test_accounts_enhanced_tdda(self):
        substrings = [
            '2025-08-24',
            'gardot.local',
            'njr',
            '"min": -',  # added
            '"max": -',  # added
        ]
        # added by hand
        lines = [
            '"local_time"',
            '"utc_time"',
            '"creator":',
            '"host":',
            '"user":',
        ]

        self.assertTextFileCorrect(os.path.join(self.cwd, 'accounts-enhanced.tdda'),
                                   os.path.join(self.refdir, 'accounts-enhanced.tdda'),
                                   ignore_substrings=substrings,
                                   ignore_lines=lines,
                                   encoding='ascii')


if __name__ == '__main__':
    ReferenceTestCase.main()
