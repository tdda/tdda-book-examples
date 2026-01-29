"""
test_pandas_rw_repls.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh pandas-rw-repls.sh' 'test_pandas_rw_repls.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PANDAS_RW_REPLS(ReferenceTestCase):
    command = 'sh pandas-rw-repls.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'pandas_rw_repls')

    generated_files = [
        os.path.join(cwd, 'accounts1k-out.csv'),
    os.path.join(cwd, 'json_pdr_syntax.py'),
    os.path.join(cwd, 'pdr_syntax.py'),
    os.path.join(cwd, 'pdw_syntax.py')
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

    def test_accounts1k_out_csv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'accounts1k-out.csv'),
                                   os.path.join(self.refdir, 'accounts1k-out.csv'),
                                   encoding='utf-8')

    def test_json_pdr_syntax_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'json_pdr_syntax.py'),
                                   os.path.join(self.refdir, 'json_pdr_syntax.py'),
                                   encoding='ascii')

    def test_pdr_syntax_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pdr_syntax.py'),
                                   os.path.join(self.refdir, 'pdr_syntax.py'),
                                   encoding='ascii')

    def test_pdw_syntax_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pdw_syntax.py'),
                                   os.path.join(self.refdir, 'pdw_syntax.py'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
