from tdda.referencetest import ReferenceTestCase, tag
from wrap import *

#     012345678901234567890123456789012345678901234567890123456789
#     .         .         .         .         .         .
L1 = 'one,two,three,four,five,six'
L2 = 'seven,eight,nine,ten,eleven,twelve'
L3 = 'thirteen,fourteen,fifteen,sixteen,seveteen,eighteen'
L4 = 'nineteen,twenty,thirty,forty,fifty,sixty'
L5 = ',,,,,'

LINES = [L1, L2, L3, L4, L5]

class TestWrap(ReferenceTestCase):
    def testFindSplitField(self):
        self.assertEqual(find_split_field(L1, 10), 2)
        self.assertEqual(find_split_field(L2, 10), 1)
        self.assertEqual(find_split_field(L3, 10), 1)
        self.assertEqual(find_split_field(L4, 10), 1)
        self.assertEqual(find_split_field(L5, 10), 6)

        self.assertEqual(find_split_field(L1, 11), 2)
        self.assertEqual(find_split_field(L2, 11), 1)
        self.assertEqual(find_split_field(L3, 11), 1)
        self.assertEqual(find_split_field(L4, 11), 1)

        self.assertEqual(find_split_field(L1, 12), 2)
        self.assertEqual(find_split_field(L2, 12), 2)
        self.assertEqual(find_split_field(L3, 12), 1)
        self.assertEqual(find_split_field(L4, 12), 1)

        self.assertEqual(find_split_field(L1, 20), 4)
        self.assertEqual(find_split_field(L2, 20), 3)
        self.assertEqual(find_split_field(L3, 20), 2)
        self.assertEqual(find_split_field(L4, 20), 2)

        self.assertEqual(find_split_field(L1, 21), 4)
        self.assertEqual(find_split_field(L2, 21), 4)
        self.assertEqual(find_split_field(L3, 21), 2)
        self.assertEqual(find_split_field(L4, 21), 2)

        self.assertEqual(find_split_field(L1, 2), 1)
        self.assertEqual(find_split_field(L2, 2), 1)
        self.assertEqual(find_split_field(L3, 2), 1)
        self.assertEqual(find_split_field(L4, 2), 1)

        self.assertEqual(find_split_field(L1, 3), 1)
        self.assertEqual(find_split_field(L2, 3), 1)
        self.assertEqual(find_split_field(L3, 3), 1)
        self.assertEqual(find_split_field(L4, 3), 1)

        self.assertEqual(find_split_field(L1, 50), 6)
        self.assertEqual(find_split_field(L2, 50), 6)
        self.assertEqual(find_split_field(L3, 50), 5)
        self.assertEqual(find_split_field(L4, 50), 6)

        self.assertEqual(find_split_field(L1, 60), 6)
        self.assertEqual(find_split_field(L2, 60), 6)
        self.assertEqual(find_split_field(L3, 60), 6)
        self.assertEqual(find_split_field(L4, 60), 6)

    def testFindCommonSplit(self):
        self.assertEqual(find_common_split_field(LINES, 10), 1)
        self.assertEqual(find_common_split_field(LINES, 20), 2)
        self.assertEqual(find_common_split_field(LINES, 30), 3)
        self.assertEqual(find_common_split_field(LINES, 40), 4)
        self.assertEqual(find_common_split_field(LINES, 50), 5)
        self.assertEqual(find_common_split_field(LINES, 51), 5)
        self.assertEqual(find_common_split_field(LINES, 52), 6)
        self.assertEqual(find_common_split_field(LINES, 100), 6)

    def testSplitLineBefore(self):
        self.assertEqual(split_line_before(L1, 0),
                         ('one,', L1[4:]))
        self.assertEqual(split_line_before(L1, 1),
                         ('one,', L1[4:]))
        self.assertEqual(split_line_before(L1, 2),
                         ('one,two,', L1[8:]))
        self.assertEqual(split_line_before(L1, 3),
                         ('one,two,three,', L1[14:]))
        self.assertEqual(split_line_before(L1, 4),
                         ('one,two,three,four,', L1[19:]))
        self.assertEqual(split_line_before(L1, 5),
                         ('one,two,three,four,five,', 'six'))
        self.assertEqual(split_line_before(L1, 6),
                         ('one,two,three,four,five,six', ''))
        self.assertEqual(split_line_before(L1, 7),
                         ('one,two,three,four,five,six', ''))

        self.assertEqual(split_line_before(L5, 0),
                         (',', ',,,,'))
        self.assertEqual(split_line_before(L5, 1),
                         (',', ',,,,'))
        self.assertEqual(split_line_before(L5, 2),
                         (',,', ',,,'))
        self.assertEqual(split_line_before(L5, 3),
                         (',,,', ',,'))
        self.assertEqual(split_line_before(L5, 4),
                         (',,,,', ','))
        self.assertEqual(split_line_before(L5, 5),
                         (',,,,,', ''))
        self.assertEqual(split_line_before(L5, 6),
                         (',,,,,', ''))
        self.assertEqual(split_line_before(L5, 7),
                         (',,,,,', ''))

    def testWrap(self):
        text = wrap('a25k-bads-v2c-head-2-raw.csv', 72, show=False)
        self.assertStringCorrect(text, 'a25k-bads-v2c-head-2.csv')


if __name__ == '__main__':
    ReferenceTestCase.main()

