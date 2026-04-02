"""
test_make.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'make' 'test_make.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_M(ReferenceTestCase):
    command = 'make'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'make')

    generated_files = [
        os.path.join(cwd, 'count-occurrences-alice-tex.txt'),
    os.path.join(cwd, 'count-occurrences-alice.txt'),
    os.path.join(cwd, 'grep-alice-alice-tex.txt'),
    os.path.join(cwd, 'grep-alice-alice.txt'),
    os.path.join(cwd, 'grep-impossible-tex.txt'),
    os.path.join(cwd, 'grep-impossible.txt'),
    os.path.join(cwd, 'grep-o-alice-tex.txt'),
    os.path.join(cwd, 'grep-o-alice.txt'),
    os.path.join(cwd, 'greps-wc-l-tex.txt'),
    os.path.join(cwd, 'greps-wc-l.txt'),
    os.path.join(cwd, 'wc-alice-tex.txt'),
    os.path.join(cwd, 'wc-alice.txt')
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

    def test_count_occurrences_alice_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'count-occurrences-alice-tex.txt'),
                                   os.path.join(self.refdir, 'count-occurrences-alice-tex.txt'),
                                   encoding='ascii')

    def test_count_occurrences_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'count-occurrences-alice.txt'),
                                   os.path.join(self.refdir, 'count-occurrences-alice.txt'),
                                   encoding='ascii')

    def test_grep_alice_alice_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-alice-alice-tex.txt'),
                                   os.path.join(self.refdir, 'grep-alice-alice-tex.txt'),
                                   encoding='utf-8')

    def test_grep_alice_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-alice-alice.txt'),
                                   os.path.join(self.refdir, 'grep-alice-alice.txt'),
                                   encoding='utf-8')

    def test_grep_impossible_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-impossible-tex.txt'),
                                   os.path.join(self.refdir, 'grep-impossible-tex.txt'),
                                   encoding='iso-8859-1')

    def test_grep_impossible_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-impossible.txt'),
                                   os.path.join(self.refdir, 'grep-impossible.txt'),
                                   encoding='iso-8859-1')

    def test_grep_o_alice_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-o-alice-tex.txt'),
                                   os.path.join(self.refdir, 'grep-o-alice-tex.txt'),
                                   encoding='ascii')

    def test_grep_o_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'grep-o-alice.txt'),
                                   os.path.join(self.refdir, 'grep-o-alice.txt'),
                                   encoding='ascii')

    def test_greps_wc_l_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'greps-wc-l-tex.txt'),
                                   os.path.join(self.refdir, 'greps-wc-l-tex.txt'),
                                   encoding='ascii')

    def test_greps_wc_l_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'greps-wc-l.txt'),
                                   os.path.join(self.refdir, 'greps-wc-l.txt'),
                                   encoding='ascii')

    def test_wc_alice_tex_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'wc-alice-tex.txt'),
                                   os.path.join(self.refdir, 'wc-alice-tex.txt'),
                                   encoding='ascii')

    def test_wc_alice_txt(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'wc-alice.txt'),
                                   os.path.join(self.refdir, 'wc-alice.txt'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
