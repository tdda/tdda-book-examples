"""
test_miro_ch_company_names_miros.py: Automatically generated test code from tdda gentest.

Generation command:

tdda gentest 'miro ch-company-names.miros' 'test_miro_ch_company_names_miros.py' '.'
"""

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command


class Test_MIRO_CH_COMPANY_NAMES_MI(ReferenceTestCase):
    command = 'miro ch-company-names.miros'
    cwd = os.path.abspath(os.path.dirname(__file__))
    refdir = os.path.join(cwd, 'ref', 'miro_ch_company_names_miros')

    generated_files = [
        os.path.join(cwd, 'ch-defs.tex'),
    os.path.join(cwd, 'ch-stats.json')
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
        patterns = [
            r'^Seed: [0-9]{10}$',
            r'^Job completed after a total of 0\.[0-9]{4} seconds\.$',
            r'^Logging to /Users/njr/miro/log/2025/09/04/[a-z]{7}[0-9]{3}\.$',
            r'^Logs [a-z]{6,7} at 2025/09/04 18:[0-9]{2}:[0-9]{2} host gardot\.local\.$',
            r'^Logs written to /Users/njr/miro/log/2025/09/04/[a-z]{7}[0-9]{3}\.$',
        ]
        substrings = [
            '2025/09/04 18:40:59',
            '2025/09/04',
        ]
        self.assertStringCorrect(self.output,
                                 os.path.join(self.refdir, 'STDOUT'),
                                 ignore_patterns=patterns,
                                 ignore_substrings=substrings)

    def test_stderr(self):
        self.assertStringCorrect(self.error,
                                 os.path.join(self.refdir, 'STDERR'))

    def test_ch_defs_tex(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ch-defs.tex'),
                                   os.path.join(self.refdir, 'ch-defs.tex'),
                                   encoding='ascii')

    def test_ch_stats_json(self):
        self.assertTextFileCorrect(os.path.join(self.cwd, 'ch-stats.json'),
                                   os.path.join(self.refdir, 'ch-stats.json'),
                                   encoding='ascii')

if __name__ == '__main__':
    ReferenceTestCase.main()
