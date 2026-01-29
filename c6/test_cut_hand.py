"""
test_cut_hand.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh cut-hand.sh' 'test_cut_hand.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_CUT_HAND(ReferenceTestCase):
    command = 'sh cut-hand.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'cut_hand')

    generated_files = [
        os.path.join(cwd, 'accounts-enhanced-extract-edited.tdda')
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

    def test_accounts_enhanced_extract_edited_tdda(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'accounts-enhanced-extract-edited.tdda'),
                                   os.path.join(self.refdir, 'accounts-enhanced-extract-edited.tdda'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
