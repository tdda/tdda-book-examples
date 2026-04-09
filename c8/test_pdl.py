"""
test_pdl.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'python pdl.py' 'test_pdl.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PDL(ReferenceTestCase):
    command = 'python pdl.py'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'pdl')

    generated_files = [
        os.path.join(cwd, 'simple3x2-inmd.psv'),
    os.path.join(cwd, 'simple3x2-pdl+pandas.serial'),
    os.path.join(cwd, 'simple3x2-pdl.psv'),
    os.path.join(cwd, 'simple3x2-pdl2.serial')
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

    def test_simple3x2_inmd_psv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-inmd.psv'),
                                   os.path.join(self.refdir, 'simple3x2-inmd.psv'),
                                   encoding='ISO-8859-1')

    def test_simple3x2_pdl_pandas_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-pdl+pandas.serial'),
                                   os.path.join(self.refdir, 'simple3x2-pdl+pandas.serial'),
                                   encoding='ascii')

    def test_simple3x2_pdl_psv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-pdl.psv'),
                                   os.path.join(self.refdir, 'simple3x2-pdl.psv'),
                                   encoding='ISO-8859-1')

    def test_simple3x2_pdl2_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-pdl2.serial'),
                                   os.path.join(self.refdir, 'simple3x2-pdl2.serial'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
