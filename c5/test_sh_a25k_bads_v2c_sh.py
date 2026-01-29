"""
test_sh_a25k_bads_v2c_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh a25k-bads-v2c.sh' 'test_sh_a25k_bads_v2c_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_A25K_BADS_V2C(ReferenceTestCase):
    command = 'sh a25k-bads-v2c.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_a25k_bads_v2c_sh')

    generated_files = [
        os.path.join(cwd, 'a25k-bads-v2c-head-2-raw.csv'),
    os.path.join(cwd, 'a25k-bads-v2c-head-2.csv'),
    os.path.join(cwd, 'a25k-bads-v2c.csv'),
    os.path.join(cwd, 'a25k-bads-v2c.txt')
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

    def test_a25k_bads_v2c_head_2_raw_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a25k-bads-v2c-head-2-raw.csv'),
                                   os.path.join(self.refdir, 'a25k-bads-v2c-head-2-raw.csv'),
                                   encoding='ascii')

    def test_a25k_bads_v2c_head_2_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a25k-bads-v2c-head-2.csv'),
                                   os.path.join(self.refdir, 'a25k-bads-v2c-head-2.csv'),
                                   encoding='ascii')

    def test_a25k_bads_v2c_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a25k-bads-v2c.csv'),
                                   os.path.join(self.refdir, 'a25k-bads-v2c.csv'),
                                   encoding='ascii')

    def test_a25k_bads_v2c_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a25k-bads-v2c.txt'),
                                   os.path.join(self.refdir, 'a25k-bads-v2c.txt'),
                                   encoding='utf-8')

if __name__ == '__main__':
    ReferenceTestCase.main()
