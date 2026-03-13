"""
test_make_test.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'make test' 'test_make_test.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_MAKE_T(ReferenceTestCase):
    command = 'make test'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'make_test')

    generated_files = [
        os.path.join(cwd, 'actual-alice-alice.txt'),
    os.path.join(cwd, 'actual-impossible-alice.txt')
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

    def test_actual_alice_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'actual-alice-alice.txt'),
                                   os.path.join(self.refdir, 'actual-alice-alice.txt'),
                                   encoding='ascii')

    def test_actual_impossible_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'actual-impossible-alice.txt'),
                                   os.path.join(self.refdir, 'actual-impossible-alice.txt'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
