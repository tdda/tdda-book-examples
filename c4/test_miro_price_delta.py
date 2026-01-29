"""
test_miro_price_delta.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'miro price-delta' 'test_miro_price_delta.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command

from ignores import MIRO_IGNORE_LINES


class Test_MIRO_PRICE_DE(ReferenceTestCase):
    command = 'miro price-delta'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'miro_price_delta')

    generated_files = [
        os.path.join(cwd, 'price-delta-defs.tex'),
    os.path.join(cwd, 'price-delta-values.json')
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
                                 os.path.join(self.refdir, 'STDOUT'),
                                 ignore_lines=MIRO_IGNORE_LINES)

    def test_stderr(self):
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'))

    def test_price_delta_defs_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'price-delta-defs.tex'),
                                   os.path.join(self.refdir, 'price-delta-defs.tex'),
                                   encoding='ascii')

    def test_price_delta_values_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'price-delta-values.json'),
                                   os.path.join(self.refdir, 'price-delta-values.json'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
