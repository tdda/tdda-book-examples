"""
test_count_occurrences_sh_Alice_alice_txt___expected_alice_alice_txt.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'count-occurrences.sh Alice alice.txt > expected-alice-alice.txt' 'test_count_occurrences_sh_Alice_alice_txt___expected_alice_alice_txt.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_COUNT_OCCURRENCES_SH_ALICE_ALICE_TXT___EXPECTED_ALICE_ALICE_(ReferenceTestCase):
    command = 'count-occurrences.sh Alice alice.txt > expected-alice-alice.txt'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'count_occurrences_sh_Alice_alice_txt___expected_alice_alice_txt')

    generated_files = [
        os.path.join(cwd, 'expected-alice-alice.txt')
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

    def test_expected_alice_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'expected-alice-alice.txt'),
                                   os.path.join(self.refdir, 'expected-alice-alice.txt'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
