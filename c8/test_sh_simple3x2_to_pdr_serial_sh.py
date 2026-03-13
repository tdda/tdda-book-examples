"""
test_sh_simple3x2_to_pdr_serial_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh simple3x2-to-pdr-serial.sh' 'test_sh_simple3x2_to_pdr_serial_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_SIMPLE3X2_TO_PDR_SERIAL(ReferenceTestCase):
    command = 'sh simple3x2-to-pdr-serial.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_simple3x2_to_pdr_serial_sh')

    generated_files = [
        os.path.join(cwd, 'simple3x2.py')
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

    def test_simple3x2_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2.py'),
                                   os.path.join(self.refdir, 'simple3x2.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
