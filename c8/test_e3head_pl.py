"""
test_e3head_pl.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh e3head-pl.sh' 'test_e3head_pl.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_E3HEAD_PL(ReferenceTestCase):
    command = 'sh e3head-pl.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'e3head_pl')

    generated_files = [
        os.path.join(cwd, 'e3head-pl.txt'),
    os.path.join(cwd, 'repl_e3head_pl.py')
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

    def test_e3head_pl_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'e3head-pl.txt'),
                                   os.path.join(self.refdir, 'e3head-pl.txt'),
                                   encoding='utf-8')

    def test_repl_e3head_pl_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_e3head_pl.py'),
                                   os.path.join(self.refdir, 'repl_e3head_pl.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
