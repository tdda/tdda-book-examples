"""
test_prt.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh prt.sh' 'test_prt.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PRT(ReferenceTestCase):
    command = 'sh prt.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'prt')

    generated_files = [
        os.path.join(cwd, 'prt-output.py'),
    os.path.join(cwd, 'repl_prt.py')
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

    def test_prt_output_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'prt-output.py'),
                                   os.path.join(self.refdir, 'prt-output.py'),
                                   encoding='ascii')

    def test_repl_prt_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_prt.py'),
                                   os.path.join(self.refdir, 'repl_prt.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
