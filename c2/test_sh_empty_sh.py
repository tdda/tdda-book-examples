"""
test_sh_empty_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh empty.sh' 'test_sh_empty_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_EMPTY(ReferenceTestCase):
    command = 'sh empty.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_empty_sh')

    generated_files = [
        os.path.join(cwd, 'empty.txt'),
    os.path.join(cwd, 'repl_empty.py')
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

    def test_empty_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'empty.txt'),
                                   os.path.join(self.refdir, 'empty.txt'),
                                   encoding='ascii')

    def test_repl_empty_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_empty.py'),
                                   os.path.join(self.refdir, 'repl_empty.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
