"""
test_enhanced_extract.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'awk -f cut-accounts-enhanced.awk accounts-enhanced.tdda > accounts-enhanced-extract.tdda' 'test_enhanced_extract.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_ENHANCED_EXTRACT(ReferenceTestCase):
    command = 'awk -f cut-accounts-enhanced.awk accounts-enhanced.tdda > accounts-enhanced-extract.tdda'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'enhanced_extract')

    generated_files = [
        os.path.join(cwd, 'accounts-enhanced-extract.tdda')
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

    def test_accounts_enhanced_extract_tdda(self):
        substrings = [
            '"min": -',  # added
            '"max": -',  # added
        ]

        self.assertTextFileCorrect(os.path.join(self.cwd, 'accounts-enhanced-extract.tdda'),
                                   os.path.join(self.refdir, 'accounts-enhanced-extract.tdda'),
                                   ignore_substrings=substrings,
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
