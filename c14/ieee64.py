"""
ieee64.py: Prints information about IEEE754 64-bit floating point values

Copyright (c) Nicholas J. Radcliffe 2024
MIT Licensed: see accompanying licence file LICENSE.

USAGE: python ieee64.py [v1 [v2 ...]]

Values v are strings that will be evaluated as eval(v) with math in scope.
Can be decimals -1.5 or expressions like 1/3 or math.nan, math.inf etc.
"""

import math
import platform
import struct  # https://docs.python.org/3.13/library/struct.html
import sys

SIGN_MASK = 1 << 63  # top bit is sign (1 for negative)
EXPONENT_MASK = eval('0b0' + '1' * 11 + '0' * 52)  # 11 exponent bits
MANTISSA_MASK = eval('0b' + '0' * 12 + '1' * 52)   # 52 mantissa bits
DIV = 1 << 52       # 52 mantissa bits
EXP_OFFSET = 0x3ff  # 1023 = 2^{10} - 1 (11 mantissa bits)
EXP_MAX = 0x7ff     # Used for NaNs and Infinities
INFINITY = 'inf' if platform.system() == 'Windows' else '∞'

class IEEE64f:
    """
    Unpack and show components of 64-bit IEEE754 floating point expression
    """
    def __init__(self, expression=None, f=None):
        self.expr = expression
        assert expression is not None or f is not None
        self.in_val = float(eval(str(expression))) if f is None else f
        self.packed = struct.pack('>d', self.in_val)  # big-endian double
        self.bits = bits = struct.unpack('>Q', self.packed)[0]  # 8-byte buf

        self.sign_bit = int(bits & SIGN_MASK > 0)
        self.exponent_raw = (bits & EXPONENT_MASK) // DIV
        self.mantissa_raw = bits & MANTISSA_MASK

        self.sign = -1 if self.sign_bit else 1  # -1 for neg; +1 for pos
        self.sgn = '+' if self.sign == 1 else '–'
        self.mantissa = (
            int(self.exponent_raw > 0)   # 0.mmm if raw exp is 0 else 1.mmm
            + (self.mantissa_raw / DIV)
        )
        self.exponent = self.exponent_raw - 1023  # exponent is offset
        if self.exponent_raw == 0x7ff:
            if self.mantissa_raw == 0:  # indicates infinity
                self.out_val = f'{self.sgn}{INFINITY}'
            else:
                self.out_val = 'NaN'  # qNaN vs. sNaN is machine dependent
        else:
            self.out_val = self.sign * self.mantissa * pow(2, self.exponent)

    def __str__(self):
        o = (
            self.out_val if type(self.out_val) is str
            else f'{self.out_val:.30f}'
        )
        return f'''
    expr:   {self.expr}
    in:     {self.in_val:.30f}
    out:    {o}
    hex:    {self.bits:016X}
    binary: {self.bits:064b}
    raw:    sign s: {self.sign_bit}  exponent:   {self.exponent_raw:4d}  mantissa:   {self.mantissa_raw:21d}
    denary: sign:   {self.sgn}  exponent e: {self.exponent:4d}  mantissa m: {self.mantissa:1.19f}

    s eeeeeeeeeee mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    {self.sign_bit} {self.exponent_raw:011b} {self.mantissa_raw:052b}
'''

    def __eq__(self, other):
        return all(self.__dict__[k] == other.__dict__[k]
                   for k in self.__dict__ if k != 'expr')


if __name__ == '__main__':
    defaults = (
        0, 1, -1, 2, -2, 1/3, 1/10, 'math.inf', '-math.inf', 'math.nan',
       '1 << 1000', '-1<<1000', '1/(1 << 1000)', '-1/(1 << 1000)',
    )
    vals = sys.argv[1:] if len(sys.argv) > 1 else defaults
    for v in vals:
        print(IEEE64f(v))
