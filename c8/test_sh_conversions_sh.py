"""
test_sh_conversions_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh conversions.sh' 'test_sh_conversions_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_CONVERSIONS(ReferenceTestCase):
    command = 'sh conversions.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_conversions_sh')

    generated_files = [
        os.path.join(cwd, 'a-pdr.serial'),
    os.path.join(cwd, 'a-plr.serial'),
    os.path.join(cwd, 'a.json'),
    os.path.join(cwd, 'foo.serial'),
    os.path.join(cwd, 'pdread.py')
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

    def test_a_pdr_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a-pdr.serial'),
                                   os.path.join(self.refdir, 'a-pdr.serial'),
                                   encoding='ascii')

    def test_a_plr_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a-plr.serial'),
                                   os.path.join(self.refdir, 'a-plr.serial'),
                                   encoding='ascii')

    def test_a_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'a.json'),
                                   os.path.join(self.refdir, 'a.json'),
                                   encoding='ascii')

    def test_foo_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'foo.serial'),
                                   os.path.join(self.refdir, 'foo.serial'),
                                   encoding='ascii')

    def test_pdread_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pdread.py'),
                                   os.path.join(self.refdir, 'pdread.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
