"""
test_sh_pd_serde_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh pd-serde.sh' 'test_sh_pd_serde_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_PD_SERDE(ReferenceTestCase):
    command = 'sh pd-serde.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_pd_serde_sh')

    generated_files = [
        os.path.join(cwd, 'repl_pd-serde.py'),
    os.path.join(cwd, 'simple3x2.csv'),
    os.path.join(cwd, 'simple3x2.serial')
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

    def test_repl_pd_serde_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_pd-serde.py'),
                                   os.path.join(self.refdir, 'repl_pd-serde.py'),
                                   encoding='utf-8')

    def test_simple3x2_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2.csv'),
                                   os.path.join(self.refdir, 'simple3x2.csv'),
                                   encoding='utf-8')

    def test_simple3x2_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2.serial'),
                                   os.path.join(self.refdir, 'simple3x2.serial'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
