from fractions import Fraction as frac
from decimal import Decimal, getcontext
from math import sin, cos

getcontext().prec = 10


def showf(f):
    s = str(f.numerator / Decimal(f.denominator))
    return s.rstrip('0').rstrip('.') if '.' in s else s


class Quaternion:
    def __init__(self, a: int | str | frac, b: int | str | frac, c: int | str | frac, d: int | str | frac) -> None:
        if isinstance(a, int) or isinstance(a, float) or isinstance(a, str):
            a = frac(a)
        if isinstance(b, int) or isinstance(b, float) or isinstance(b, str):
            b = frac(b)
        if isinstance(c, int) or isinstance(c, float) or isinstance(c, str):
            c = frac(c)
        if isinstance(d, int) or isinstance(d, float) or isinstance(d, str):
            d = frac(d)

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return f"{showf(self.a)} + {showf(self.b)}i + {showf(self.c)}j + {showf(self.d)}k"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __truediv__(self, other):
        if isinstance(other, Quaternion):
            return self * other.inverse()
        elif isinstance(other, frac):
            return Quaternion(
                self.a / other,
                self.b / other,
                self.c / other,
                self.d / other
            )
        else:
            raise TypeError(
                f"invalid type for quaternion div: '{type(other).__name__}' (expected Quaternion or Fraction)")

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            a1 = self.a
            a2 = other.a
            b1 = self.b
            b2 = other.b
            c1 = self.c
            c2 = other.c
            d1 = self.d
            d2 = other.d

            a = a1*a2 - b1*b2 - c1*c2 - d1*d2
            b = a1*b2 + b1*a2 + c1*d2 - d1*c2
            c = a1*c2 - b1*d2 + c1*a2 + d1*b2
            d = a1*d2 + b1*c2 - c1*b2 + d1*a2

            return Quaternion(a, b, c, d)
        elif isinstance(other, frac):
            return Quaternion(
                self.a * other,
                self.b * other,
                self.c * other,
                self.d * other
            )
        else:
            raise TypeError(
                f"invalid type for quaternion mult: '{type(other).__name__}' (expected Quaternion or Fraction)")

    def norm(self):
        n = self.a**2 + self.b**2 + self.c**2 + self.d**2
        assert isinstance(n, frac)
        return n

    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def inverse(self):
        return self.conjugate() / self.norm()


PRECISION_LIMIT = 10**4

def precise(n):
    return frac(n).limit_denominator(PRECISION_LIMIT)


def point_rotate(p, axis, angle):
    # point quaternion
    p = Quaternion('0', *p)

    sine_angle = precise(
        sin(angle / 2)
    )
    cosine_angle = precise(
        cos(angle / 2)
    )

    q = Quaternion(
        cosine_angle, 
        *[i*sine_angle for i in axis]
    )

    rotated = q * p * q.inverse()

    assert rotated.a == 0
    return (rotated.b, rotated.c, rotated.d)
