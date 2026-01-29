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
EXPONENT_MASK = eval(\textquotesingle{}0b0\textquotesingle{} + \textquotesingle{}1\textquotesingle{} * 11 + \textquotesingle{}0\textquotesingle{} * 52)  # 11 exponent bits
MANTISSA_MASK = eval(\textquotesingle{}0b\textquotesingle{} + \textquotesingle{}0\textquotesingle{} * 12 + \textquotesingle{}1\textquotesingle{} * 52)   # 52 mantissa bits
DIV = 1 << 52       # 52 mantissa bits
EXP_OFFSET = 0x3ff  # 1023 = 2^\{10\} - 1 (11 mantissa bits)
EXP_MAX = 0x7ff     # Used for NaNs and Infinities
INFINITY = \textquotesingle{}inf\textquotesingle{} if platform.system() == \textquotesingle{}Windows\textquotesingle{} else \textquotesingle{}$\codeinfty$\textquotesingle{}

class IEEE64f:
    """
    Unpack and show components of 64-bit IEEE754 floating point expression
    """
    def __init__(self, expression=None, f=None):
        self.expr = expression
        assert expression is not None or f is not None
        self.in_val = float(eval(str(expression))) if f is None else f
        self.packed = struct.pack(\textquotesingle{}>d\textquotesingle{}, self.in_val)  # big-endian double
        self.bits = bits = struct.unpack(\textquotesingle{}>Q\textquotesingle{}, self.packed)[0]  # 8-byte buf

        self.sign_bit = int(bits & SIGN_MASK > 0)
        self.exponent_raw = (bits & EXPONENT_MASK) // DIV
        self.mantissa_raw = bits & MANTISSA_MASK

        self.sign = -1 if self.sign_bit else 1  # -1 for neg; +1 for pos
        self.sgn = \textquotesingle{}+\textquotesingle{} if self.sign == 1 else \textquotesingle{}-\textquotesingle{}
        self.mantissa = (
            int(self.exponent_raw > 0)   # 0.mmm if raw exp is 0 else 1.mmm
            + (self.mantissa_raw / DIV)
        )
        self.exponent = self.exponent_raw - 1023  # exponent is offset
        if self.exponent_raw == 0x7ff:
            if self.mantissa_raw == 0:  # indicates infinity
                self.out_val = f\textquotesingle{}\{self.sgn\}\{INFINITY\}\textquotesingle{}
            else:
                self.out_val = \textquotesingle{}NaN\textquotesingle{}  # qNaN vs. sNaN is machine dependent
        else:
            self.out_val = self.sign * self.mantissa * pow(2, self.exponent)

    def __str__(self):
        o = (
            self.out_val if type(self.out_val) is str
            else f\textquotesingle{}\{self.out_val:.30f\}\textquotesingle{}
        )
        return f\textquotesingle{}\textquotesingle{}\textquotesingle{}
    expr:   \{self.expr\}
    in:     \{self.in_val:.30f\}
    out:    \{o\}
    hex:    \{self.bits:016X\}
    binary: \{self.bits:064b\}
    raw:    sign s: \{self.sign_bit\}  exponent:   \{self.exponent_raw:4d\}  mantiss
a:   \{self.mantissa_raw:21d\}
    denary: sign:   \{self.sgn\}  exponent e: \{self.exponent:4d\}  mantissa m: \{sel
f.mantissa:1.19f\}

    s eeeeeeeeeee mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    \{self.sign_bit\} \{self.exponent_raw:011b\} \{self.mantissa_raw:052b\}
\textquotesingle{}\textquotesingle{}\textquotesingle{}

    def __eq__(self, other):
        return all(self.__dict__[k] == other.__dict__[k]
                   for k in self.__dict__ if k != \textquotesingle{}expr\textquotesingle{})


if __name__ == \textquotesingle{}__main__\textquotesingle{}:
    defaults = (
        0, 1, -1, 2, -2, 1/3, 1/10, \textquotesingle{}math.inf\textquotesingle{}, \textquotesingle{}-math.inf\textquotesingle{}, \textquotesingle{}math.nan\textquotesingle{},
       \textquotesingle{}1 << 1000\textquotesingle{}, \textquotesingle{}-1<<1000\textquotesingle{}, \textquotesingle{}1/(1 << 1000)\textquotesingle{}, \textquotesingle{}-1/(1 << 1000)\textquotesingle{},
    )
    vals = sys.argv[1:] if len(sys.argv) > 1 else defaults
    for v in vals:
        print(IEEE64f(v))
