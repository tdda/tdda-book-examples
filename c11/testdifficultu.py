import unittest

def difficult_alice():
    with open('alice/alice.txt') as f:
         return f.read().replace('impossible', 'difficult')

class TestBigTextDiff(unittest.TestCase):
    def testImpossibleDifficultAlice(self):
        with open('alice/alice.txt') as f:
             expected = f.read()
        actual = difficult_alice()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
