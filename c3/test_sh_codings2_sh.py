"""
test_sh_codings2_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh codings2.sh' 'test_sh_codings2_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_CODINGS2(ReferenceTestCase):
    command = 'sh codings2.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_codings2_sh')

    generated_files = [
        os.path.join(cwd, 'codings2-out-2col.svg'),
    os.path.join(cwd, 'codings2-out-2col.txt'),
    os.path.join(cwd, 'codings2-out.txt')
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

    def test_codings2_out_2col_svg(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'codings2-out-2col.svg'),
                                   os.path.join(self.refdir, 'codings2-out-2col.svg'))

    def test_codings2_out_2col_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'codings2-out-2col.txt'),
                                   os.path.join(self.refdir, 'codings2-out-2col.txt'),
                                   encoding='utf-8')

    def test_codings2_out_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'codings2-out.txt'),
                                   os.path.join(self.refdir, 'codings2-out.txt'),
                                   encoding='utf-8')

if __name__ == '__main__':
    ReferenceTestCase.main()
