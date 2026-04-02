"""
test_sh_pythonfragments_sh.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh pythonfragments.sh' 'test_sh_pythonfragments_sh.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_SH_PYTHONFRAGMENTS(ReferenceTestCase):
    command = 'sh pythonfragments.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'sh_pythonfragments_sh')

    generated_files = [
        os.path.join(cwd, '123.txt'),
    os.path.join(cwd, 'dictorder.txt'),
    os.path.join(cwd, 'indentedjson.txt'),
    os.path.join(cwd, 'jsondictorder.txt'),
    os.path.join(cwd, 'jsondictorder2.txt'),
    os.path.join(cwd, 'repl_123.py'),
    os.path.join(cwd, 'repl_dictorder.py'),
    os.path.join(cwd, 'repl_indentedjson.py'),
    os.path.join(cwd, 'repl_jsondictorder.py'),
    os.path.join(cwd, 'repl_jsondictorder2.py')
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

    def test_123_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, '123.txt'),
                                   os.path.join(self.refdir, '123.txt'),
                                   encoding='ascii')

    def test_dictorder_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'dictorder.txt'),
                                   os.path.join(self.refdir, 'dictorder.txt'),
                                   encoding='ascii')

    def test_indentedjson_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'indentedjson.txt'),
                                   os.path.join(self.refdir, 'indentedjson.txt'),
                                   encoding='ascii')

    def test_jsondictorder_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'jsondictorder.txt'),
                                   os.path.join(self.refdir, 'jsondictorder.txt'),
                                   encoding='ascii')

    def test_jsondictorder2_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'jsondictorder2.txt'),
                                   os.path.join(self.refdir, 'jsondictorder2.txt'),
                                   encoding='ascii')

    def test_repl_123_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_123.py'),
                                   os.path.join(self.refdir, 'repl_123.py'),
                                   encoding='ascii')

    def test_repl_dictorder_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_dictorder.py'),
                                   os.path.join(self.refdir, 'repl_dictorder.py'),
                                   encoding='ascii')

    def test_repl_indentedjson_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_indentedjson.py'),
                                   os.path.join(self.refdir, 'repl_indentedjson.py'),
                                   encoding='ascii')

    def test_repl_jsondictorder_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_jsondictorder.py'),
                                   os.path.join(self.refdir, 'repl_jsondictorder.py'),
                                   encoding='ascii')

    def test_repl_jsondictorder2_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_jsondictorder2.py'),
                                   os.path.join(self.refdir, 'repl_jsondictorder2.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
