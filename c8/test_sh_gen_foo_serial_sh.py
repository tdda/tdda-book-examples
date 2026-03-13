"""
test_sh_gen_foo_serial_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh gen-foo-serial.sh' 'test_sh_gen_foo_serial_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_GEN_FOO_SERIAL(ReferenceTestCase):
    command = 'sh gen-foo-serial.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_gen_foo_serial_sh')

    generated_files = [
        os.path.join(cwd, 'foo.csv'),
    os.path.join(cwd, 'foo.serial')
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

    def test_foo_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'foo.csv'),
                                   os.path.join(self.refdir, 'foo.csv'),
                                   encoding='utf-8')

    def test_foo_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'foo.serial'),
                                   os.path.join(self.refdir, 'foo.serial'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
