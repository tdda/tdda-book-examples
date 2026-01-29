"""
test_sh_dump_doubledot_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh dump-doubledot.sh' 'test_sh_dump_doubledot_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_DUMP_DOUBLEDOT(ReferenceTestCase):
    command = 'sh dump-doubledot.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_dump_doubledot_sh')

    generated_files = [
        os.path.join(cwd, 'doubledot-hexdump-tex.txt'),
    os.path.join(cwd, 'doubledot-hexdump.txt')
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

    def test_doubledot_hexdump_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'doubledot-hexdump-tex.txt'),
                                   os.path.join(self.refdir, 'doubledot-hexdump-tex.txt'),
                                   encoding='ascii')

    def test_doubledot_hexdump_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'doubledot-hexdump.txt'),
                                   os.path.join(self.refdir, 'doubledot-hexdump.txt'),
                                   encoding='utf-8')

if __name__ == '__main__':
    ReferenceTestCase.main()
