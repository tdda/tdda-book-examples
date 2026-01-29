"""
test_python_pandas_nulls_py_t.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'python pandas-nulls.py t' 'test_python_pandas_nulls_py_t.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_PYTHON_PANDAS_NULLS_P(ReferenceTestCase):
    command = 'python pandas-nulls.py t'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'python_pandas_nulls_py_t')

    generated_files = [
        os.path.join(cwd, 'pandas-comparison-eq.tex'),
    os.path.join(cwd, 'pandas-comparison-is.tex'),
    os.path.join(cwd, 'pd-nulls-df1-comparisons.txt'),
    os.path.join(cwd, 'pd-nulls-df1.txt'),
    os.path.join(cwd, 'pd-nulls-df1==df1.txt'),
    os.path.join(cwd, 'pd-nulls-df1==df2.txt')
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

    def test_pandas_comparison_eq_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pandas-comparison-eq.tex'),
                                   os.path.join(self.refdir, 'pandas-comparison-eq.tex'),
                                   encoding='ascii')

    def test_pandas_comparison_is_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pandas-comparison-is.tex'),
                                   os.path.join(self.refdir, 'pandas-comparison-is.tex'),
                                   encoding='ascii')

    def test_pd_nulls_df1_comparisons_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pd-nulls-df1-comparisons.txt'),
                                   os.path.join(self.refdir, 'pd-nulls-df1-comparisons.txt'),
                                   encoding='ascii')

    def test_pd_nulls_df1_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pd-nulls-df1.txt'),
                                   os.path.join(self.refdir, 'pd-nulls-df1.txt'),
                                   encoding='ascii')

    def test_pd_nulls_df1__df1_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pd-nulls-df1==df1.txt'),
                                   os.path.join(self.refdir, 'pd-nulls-df1==df1.txt'),
                                   encoding='ascii')

    def test_pd_nulls_df1__df2_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'pd-nulls-df1==df2.txt'),
                                   os.path.join(self.refdir, 'pd-nulls-df1==df2.txt'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
