"""
test_sh_ieee_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh ieee.sh' 'test_sh_ieee_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_IEEE(ReferenceTestCase):
    command = 'sh ieee.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_ieee_sh')

    generated_files = [
        os.path.join(cwd, 'googol.txt'),
    os.path.join(cwd, 'googol.txt.tex'),
    os.path.join(cwd, 'ieee64-1over10.txt'),
    os.path.join(cwd, 'ieee64-1over10.txt.tex'),
    os.path.join(cwd, 'ieee64-googol.txt'),
    os.path.join(cwd, 'ieee64-googol.txt.tex'),
    os.path.join(cwd, 'ieee64-m2.125.txt'),
    os.path.join(cwd, 'ieee64-m2.125.txt.tex')
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

    def test_googol_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'googol.txt'),
                                   os.path.join(self.refdir, 'googol.txt'),
                                   encoding='ascii')

    def test_googol_txt_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'googol.txt.tex'),
                                   os.path.join(self.refdir, 'googol.txt.tex'),
                                   encoding='ascii')

    def test_ieee64_1over10_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-1over10.txt'),
                                   os.path.join(self.refdir, 'ieee64-1over10.txt'),
                                   encoding='ascii')

    def test_ieee64_1over10_txt_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-1over10.txt.tex'),
                                   os.path.join(self.refdir, 'ieee64-1over10.txt.tex'),
                                   encoding='ascii')

    def test_ieee64_googol_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-googol.txt'),
                                   os.path.join(self.refdir, 'ieee64-googol.txt'),
                                   encoding='ascii')

    def test_ieee64_googol_txt_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-googol.txt.tex'),
                                   os.path.join(self.refdir, 'ieee64-googol.txt.tex'),
                                   encoding='ascii')

    def test_ieee64_m2_125_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-m2.125.txt'),
                                   os.path.join(self.refdir, 'ieee64-m2.125.txt'),
                                   encoding='Windows-1252')

    def test_ieee64_m2_125_txt_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ieee64-m2.125.txt.tex'),
                                   os.path.join(self.refdir, 'ieee64-m2.125.txt.tex'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
