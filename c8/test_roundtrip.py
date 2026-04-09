"""
test_roundtrip.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'sh csv_pdl_roundtrip.sh' 'test_roundtrip.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_ROUNDTRIP(ReferenceTestCase):
    command = 'sh csv_pdl_roundtrip.sh'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'roundtrip')

    generated_files = [
        os.path.join(cwd, 'csv_pdl_roundtrip.txt'),
    os.path.join(cwd, 'read_pdl_polars.txt'),
    os.path.join(cwd, 'repl_csv_pdl_roundtrip_pandas.py'),
    os.path.join(cwd, 'repl_df2.txt'),
    os.path.join(cwd, 'repl_pd2csv.txt'),
    os.path.join(cwd, 'repl_pl_pdl.txt'),
    os.path.join(cwd, 'repl_read_pdl_polars.py'),
    os.path.join(cwd, 'simple3x2-pdl.psv'),
    os.path.join(cwd, 'simple3x2-pdl.serial')
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

    def test_csv_pdl_roundtrip_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'csv_pdl_roundtrip.txt'),
                                   os.path.join(self.refdir, 'csv_pdl_roundtrip.txt'),
                                   encoding='ascii')

    def test_read_pdl_polars_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'read_pdl_polars.txt'),
                                   os.path.join(self.refdir, 'read_pdl_polars.txt'),
                                   encoding='ascii')

    def test_repl_csv_pdl_roundtrip_pandas_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_csv_pdl_roundtrip_pandas.py'),
                                   os.path.join(self.refdir, 'repl_csv_pdl_roundtrip_pandas.py'),
                                   encoding='ascii')

    def test_repl_df2_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_df2.txt'),
                                   os.path.join(self.refdir, 'repl_df2.txt'),
                                   encoding='ascii')

    def test_repl_pd2csv_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_pd2csv.txt'),
                                   os.path.join(self.refdir, 'repl_pd2csv.txt'),
                                   encoding='ascii')

    def test_repl_pl_pdl_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_pl_pdl.txt'),
                                   os.path.join(self.refdir, 'repl_pl_pdl.txt'),
                                   encoding='ascii')

    def test_repl_read_pdl_polars_py(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'repl_read_pdl_polars.py'),
                                   os.path.join(self.refdir, 'repl_read_pdl_polars.py'),
                                   encoding='ascii')

    def test_simple3x2_pdl_psv(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-pdl.psv'),
                                   os.path.join(self.refdir, 'simple3x2-pdl.psv'),
                                   encoding='ISO-8859-1')

    def test_simple3x2_pdl_serial(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'simple3x2-pdl.serial'),
                                   os.path.join(self.refdir, 'simple3x2-pdl.serial'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
