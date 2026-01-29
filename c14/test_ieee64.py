"""
test_ieee64.py: Tests for ieee64.py

Copyright (c) Nicholas J. Radcliffe 2024
MIT Licensed: see accompanying licence file LICENSE.

USAGE: python test_ieee64.py

   or: pytest
       (if you have pytest installed)
"""

import math
import numpy as np
import struct
import sys
import unittest

from ieee64 import IEEE64f, INFINITY

TEST_EXPRESSIONS = [
    0,
    0.0,
    1,
    -1,
    2,
    -2,
    '1/3',
    '-1/3',
    '1/10',
    -2.25,
    123_456_789_012.345_678_901,
    -987_654_321_098.765_432_109,
    '1 << 1000',
    '-1<<1000',
    '1/(1 << 1000)',
    '-1/(1 << 1000)',
    '"1" + "0" * 100',   # googol
    '"-1" + "0" * 100',  # -googol
    math.pi,
    math.e,
    'math.nan',
    'math.inf',
    '-math.inf',
    '"1" + "0" * 1000',
    '"1" + "0" * 1000',
]

MINUS_ZERO = np.float64(0) * np.float64(-1.0)

EQUIVS = {
    'nan': 'NaN',
    'inf': f'+{INFINITY}',
    '-inf': f'–{INFINITY}',
}


def eq(v1, v2):
    """
    Checks equality of v1 and v2, which are normally floats,
    but also allows 'NaN' to match np.nan and '±∞' to match ±math.inf.
    """
    return v1 == v2 or EQUIVS.get(str(v1), v1) == EQUIVS.get(str(v2), v2)


def hex_to_float(hexstr):
    """
    Constructs a float64 from the its in its IEEE754 64-bit float
    hex representation (using big-endian for both).

    Takes a hex string, possibly with spaces between digits,
    and converts to the equivalent unsigned big-endian 64-bit integer
    and then unpacks the bits as if they had come from a float64.

    This allows, inter alia, the hex representations on the (versioned)
    Wikipedia page on Double-precision floating-point format (as of 2024-11-23)
        https://en.wikipedia.org/w/index.php?
        title=Double-precision_floating-point_format&oldid=1256949768
    to be parsed and used to create known floats for the testst.
    """
    packed = struct.pack('>Q', np.uint64(eval('0X' + hexstr.replace(' ', ''))))
    return struct.unpack('>d', packed)[0]


def hex_and_float(hexstr):
    """
    Returns pair with the hex string provided and the IEEE754 float64
    it represents.
    """
    return (hexstr, hex_to_float(hexstr))



class TestIEEE64f(unittest.TestCase):
    def testInOut(self):
        vals = [IEEE64f(expr) for expr in TEST_EXPRESSIONS]
        same_in_out = [eq(v.in_val, v.out_val) for v in vals]
        if not(all(same_in_out)):
            for v in vals:
                if v.in_val != v.out_val:
                    print('FAILURE CASE:', file=sys.stderr)
                    print(v, end='\n\n', file=sys.stderr)
        self.assertTrue(all(same_in_out))

    def testInOutNumpyF64(self):
        vals = [
            IEEE64f(f=np.float64(eval(str(expr))))
            for expr in TEST_EXPRESSIONS
        ]
        same_in_out = [eq(v.in_val, v.out_val) for v in vals]
        if not(all(same_in_out)):
            for v in vals:
                if v.in_val != v.out_val:
                    print('FAILURE CASE:', file=sys.stderr)
                    print(v, end='\n\n', file=sys.stderr)
        self.assertTrue(all(same_in_out))

    def testEquality(self):
        tenth = IEEE64f(1/10)
        point1 = IEEE64f(0.1)
        self.assertEqual(tenth, tenth)
        self.assertEqual(point1, point1)
        self.assertEqual(point1, tenth)
        self.assertEqual(tenth, point1)

    def testNonEquality(self):
        tenth_64 = IEEE64f(1/10)
        point2_64 = IEEE64f(0.2)
        self.assertNotEqual(tenth_64, point2_64)

        zero = np.float64(0.0)
        minus_zero = np.float64(-1.0) * np.float64(0.0)
        self.assertNotEqual(IEEE64f(f=zero), IEEE64f(minus_zero))

    def testZeroMinusZeroRep(self):
        zero_64 = IEEE64f(f=0.0)
        minus_zero_64 = IEEE64f(f=MINUS_ZERO)
        self.assertEqual(str(zero_64).strip(), '''
    expr:   None
    in:     0.000000000000000000000000000000
    out:    0.000000000000000000000000000000
    hex:    0000000000000000
    binary: 0000000000000000000000000000000000000000000000000000000000000000
    raw:    sign s: 0  exponent:      0  mantissa:                       0
    denary: sign:   +  exponent e: -1023  mantissa m: 0.0000000000000000000

    s eeeeeeeeeee mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    0 00000000000 0000000000000000000000000000000000000000000000000000
'''.strip())
        self.assertEqual(str(minus_zero_64).strip(), '''
    expr:   None
    in:     -0.000000000000000000000000000000
    out:    -0.000000000000000000000000000000
    hex:    8000000000000000
    binary: 1000000000000000000000000000000000000000000000000000000000000000
    raw:    sign s: 1  exponent:      0  mantissa:                       0
    denary: sign:   –  exponent e: -1023  mantissa m: 0.0000000000000000000

    s eeeeeeeeeee mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    1 00000000000 0000000000000000000000000000000000000000000000000000
'''.strip())

    def testMostWikipediaExamples(self):
        """
        Examples from Wikipedia page on Double-precision floating-point format
        (version as of 2024-11-23)
        https://en.wikipedia.org/w/index.php?
        title=Double-precision_floating-point_format&oldid=1256949768

        Can test all except the NaN values straightforwardly.
        Next test (testWikipediaNaNExamples) does the NaN examples.

        0 01111111111 0000000000000000000000000000000000000000000000000000₂
          ≙ 3FF0 0000 0000 0000₁₆   ≙ +2^0 × 1 = 1

        0 01111111111 0000000000000000000000000000000000000000000000000001₂
          ≙ 3FF0 0000 0000 0001₁₆
          ≙ +2^0 × (1 + 2−52) ≈ 1.0000000000000002, the smallest number > 1
        0 01111111111 0000000000000000000000000000000000000000000000000010₂
          ≙ 3FF0 0000 0000 0002₁₆
          ≙ +2*0 × (1 + 2−51) ≈ 1.0000000000000004
        0 10000000000 0000000000000000000000000000000000000000000000000000₂
          ≙ 4000 0000 0000 0000₁₆
          ≙ +2^1 × 1 = ₂
        1 10000000000 0000000000000000000000000000000000000000000000000000₂
          ≙ C000 0000 0000 0000₁₆
          ≙ −2^1 × 1 = −₂

        0 10000000000 1000000000000000000000000000000000000000000000000000₂
          ≙ 4008 0000 0000 0000₁₆
          ≙ +2^1 × 1.12 = 112 = 3
        0 10000000001 0000000000000000000000000000000000000000000000000000₂
          ≙ 4010 0000 0000 0000₁₆
          ≙ +22 × 1 = 1002 = 4
        0 10000000001 0100000000000000000000000000000000000000000000000000₂
          ≙ 4014 0000 0000 0000₁₆
          ≙ +22 × 1.012 = 1012 = 5
        0 10000000001 1000000000000000000000000000000000000000000000000000₂
          ≙ 4018 0000 0000 0000₁₆
          ≙ +22 × 1.12 = 1102 = 6
        0 10000000011 0111000000000000000000000000000000000000000000000000₂
          ≙ 4037 0000 0000 0000₁₆
          ≙ +24 × 1.01112 = 10111₂ = 23

        0 00000000000 0000000000000000000000000000000000000000000000000001₂
          ≙ 0000 0000 0000 0001₁₆
          ≙ +2−1022 × 2−52 = 2−1074 ≈ 4.9406564584124654 × 10−324
           (Min. subnormal positive double)
        0 00000000000 1111111111111111111111111111111111111111111111111111₂
          ≙ 000F FFFF FFFF FFFF₁₆
          ≙ +2−1022 × (1 − 2−52) ≈ 2.2250738585072009 × 10−308
           (Max. subnormal double)
        0 00000000001 0000000000000000000000000000000000000000000000000000₂
          ≙ 0010 0000 0000 0000₁₆
          ≙ +2−1022 × 1 ≈ 2.2250738585072014 × 10−308
           (Min. normal positive double)
        0 11111111110 1111111111111111111111111111111111111111111111111111₂
          ≙ 7FEF FFFF FFFF FFFF₁₆
          ≙ +21023 × (1 + (1 − 2−52)) ≈ 1.7976931348623157 × 10308
           (Max. double)

        0 00000000000 0000000000000000000000000000000000000000000000000000₂
          ≙ 0000 0000 0000 0000₁₆
          ≙ +0
        1 00000000000 0000000000000000000000000000000000000000000000000000₂
          ≙ 8000 0000 0000 0000₁₆
          ≙ −0
        0 11111111111 0000000000000000000000000000000000000000000000000000₂
          ≙ 7FF0 0000 0000 0000₁₆
          ≙ +∞ (positive infinity)
        1 11111111111 0000000000000000000000000000000000000000000000000000₂
          ≙ FFF0 0000 0000 0000₁₆
          ≙ −∞ (negative infinity)
        0 11111111111 0000000000000000000000000000000000000000000000000001₂
          ≙ 7FF0 0000 0000 0001₁₆
          ≙ NaN (sNaN on most processors, such as x86 and ARM)
        0 11111111111 1000000000000000000000000000000000000000000000000001₂
          ≙ 7FF8 0000 0000 0001₁₆
          ≙ NaN (qNaN on most processors, such as x86 and ARM)
        0 11111111111 1111111111111111111111111111111111111111111111111111₂
          ≙ 7FFF FFFF FFFF FFFF₁₆
          ≙ NaN (an alternative encoding of NaN)

        0 01111111101 0101010101010101010101010101010101010101010101010101₂
          = 3FD5 5555 5555 5555₁₆
          ≙ +2−2 × (1 + 2−2 + 2−4 + ... + 2−52) ≈ 1/3

        0 10000000000 1001001000011111101101010100010001000010110100011000₂
          = 4009 21FB 5444 2D1816 ≈ pi
        """

        cases = {
          '0 01111111111 0000000000000000000000000000000000000000000000000000':
          ('3FF0 0000 0000 0000', 1),

          '0 01111111111 0000000000000000000000000000000000000000000000000001':
          ('3FF0 0000 0000 0001', 1.0000000000000002),

          '0 01111111111 0000000000000000000000000000000000000000000000000010':
          ('3FF0 0000 0000 0002', 1.0000000000000004),

          '0 10000000000 0000000000000000000000000000000000000000000000000000':
          ('4000 0000 0000 0000', 2),

          '1 10000000000 0000000000000000000000000000000000000000000000000000':
          ('C000 0000 0000 0000', -2),

          '0 10000000000 1000000000000000000000000000000000000000000000000000':
          ('4008 0000 0000 0000', 3),

          '0 10000000001 0000000000000000000000000000000000000000000000000000':
          ('4010 0000 0000 0000', 4),

          '0 10000000001 0100000000000000000000000000000000000000000000000000':
          ('4014 0000 0000 0000', 5),

          '0 10000000001 1000000000000000000000000000000000000000000000000000':
          ('4018 0000 0000 0000', 6),

          '0 00000000000 0000000000000000000000000000000000000000000000000001':
          ('0000 0000 0000 0001', 4.9406564584124654e-324),

          '0 00000000000 1111111111111111111111111111111111111111111111111111':
          ('000F FFFF FFFF FFFF', 2.2250738585072009e-308),

          '0 00000000001 0000000000000000000000000000000000000000000000000000':
          ('0010 0000 0000 0000', 2.2250738585072014e-308),

          '0 11111111110 1111111111111111111111111111111111111111111111111111':
          ('7FEF FFFF FFFF FFFF', 1.7976931348623157e308),


          '0 00000000000 0000000000000000000000000000000000000000000000000000':
          ('0000 0000 0000 0000', 0.0),

          '1 00000000000 0000000000000000000000000000000000000000000000000000':
          ('8000 0000 0000 0000', MINUS_ZERO),

          '0 11111111111 0000000000000000000000000000000000000000000000000000':
          ('7FF0 0000 0000 0000', math.inf),

          '1 11111111111 0000000000000000000000000000000000000000000000000000':
          ('FFF0 0000 0000 0000', -math.inf),

          '0 01111111101 0101010101010101010101010101010101010101010101010101':
          ('3FD5 5555 5555 5555', 1/3),

          '0 10000000000 1001001000011111101101010100010001000010110100011000':
          ('4009 21FB 5444 2D18', math.pi),

        }
        for bitstr, (hexstr, v) in cases.items():
            fp = IEEE64f(f=v)
            h = hexstr.replace(' ', '')
            b = bitstr.replace(' ', '')
            self.assertEqual(f'{fp.bits:016X}', h)
            self.assertEqual(f'{fp.bits:064b}', b)

    def testWikipediaNaNExamples(self):

        nan_cases = {
          '0 11111111111 0000000000000000000000000000000000000000000000000001':
          hex_and_float('7FF0 0000 0000 0001'),
          #   NaN (sNaN on most processors', such as x86 and ARM)),

          '0 11111111111 1000000000000000000000000000000000000000000000000001':
          hex_and_float('7FF8 0000 0000 0001'),
          #   NaN (qNaN on most processors, such as x86 and ARM)

          '0 11111111111 1111111111111111111111111111111111111111111111111111':
          hex_and_float('7FFF FFFF FFFF FFFF'),
          # NaN (an alternative encoding of NaN)

        }
        for bitstr, (hexstr, v) in nan_cases.items():
            fp = IEEE64f(f=v)
            h = hexstr.replace(' ', '')
            b = bitstr.replace(' ', '')
            self.assertEqual(f'{fp.bits:016X}', h)
            self.assertEqual(f'{fp.bits:064b}', b)
            self.assertTrue(np.isnan(np.float64(fp.out_val)))

    def testBadInput(self):
        self.assertRaises(NameError, IEEE64f, 'foo')
        self.assertRaises(ZeroDivisionError, IEEE64f, '0/0')
        self.assertRaises(SyntaxError, IEEE64f, '3 +')
        self.assertRaises(AssertionError, IEEE64f)


if __name__ == '__main__':
    unittest.main()
