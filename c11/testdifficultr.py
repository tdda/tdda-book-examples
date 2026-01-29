from tdda.referencetest import ReferenceTestCase, tag  # tdda import
from testdifficultu import difficult_alice             # re-use from previous

class TestBigTextDiff(ReferenceTestCase):              # Inherit from tdda
    def testImpossibleDifficultAlice(self):
        # no need to read expected file
        actual = difficult_alice()
        self.assertStringCorrect(actual,                # TDDA assertion method
                                 'alice/alice.txt')     # just point to file

if __name__ == '__main__':
    ReferenceTestCase.main()                            # main from tdda
