import math


class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        if denominator == 0:
            raise ValueError("Division by zero")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    @classmethod
    def from_string(cls, s):
        parts = s.split('/')
        if len(parts) == 1:
            return cls(int(parts[0]))
        else:
            return cls(int(parts[0]), int(parts[1]))

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return self + Rational.from_string(str(other))

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return self - Rational.from_string(str(other))

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator,
                            self.denominator * other.denominator)
        else:
            return self * Rational.from_string(str(other))

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ValueError("Division by zero")
            return Rational(self.numerator * other.denominator,
                            self.denominator * other.numerator)
        else:
            return self / Rational.from_string(str(other))

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        else:
            return self > Rational.from_string(str(other))

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:
            return self < Rational.from_string(str(other))

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __pow__(self, power):
        if isinstance(power, int):
            if power == 0:
                return Rational(1)
            elif power > 0:
                return Rational(self.numerator ** power, self.denominator ** power)
            else:
                return Rational(self.denominator ** abs(power), self.numerator ** abs(power))
        else:
            raise TypeError("Exponent must be an integer")

    def reciprocal(self):
        return Rational(self.denominator, self.numerator)

    def absolute(self):
        return Rational(abs(self.numerator), self.denominator)

    def sign(self):
        if self.numerator > 0:
            return 1
        elif self.numerator < 0:
            return -1
        else:
            return 0

    def is_integer(self):
        return self.denominator == 1

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator


def evaluate_polynomial(coeffs, x):
    """
    Обчислює значення многочлена в точці x.

    :param coeffs: Список коефіцієнтів многочлена, від старшого до молодшого.
    :param x: Точка, в якій обчислюється значення многочлена.
    :return: Значення многочлена в точці x.
    """
    result = Rational(0)
    n = len(coeffs)
    for i in range(n):
        result += coeffs[i] * Rational(x) ** (n - i - 1)
    return result


def find_roots(coeffs):
    """
    Знаходить раціональні корені многочлена з цілими коефіцієнтами.

    :param coeffs: Список коефіцієнтів многочлена.
    :return: Список раціональних коренів.
    """
    n = len(coeffs)
    if n <= 2:
        if n == 1:
            return []
        elif n == 2:
            a, b = coeffs
            if a == 0:
                return []
            else:
                return [-b / a]
    else:
        if all(isinstance(coef, int) for coef in coeffs):
            p = coeffs[-1]
            q = coeffs[0]
            possible_numerators = [i for i in range(1, abs(p) + 1) if p % i == 0]
            possible_denominators = [j for j in range(1, abs(q) + 1) if q % j == 0]
            rational_roots = []
            for numerator in possible_numerators:
                for denominator in possible_denominators:
                    potential_root = Rational(numerator, denominator)
                    if evaluate_polynomial(coeffs, potential_root) == 0:
                        rational_roots.append(potential_root)
            return rational_roots
        else:
            return "Coefficients are not all integers, unable to find rational roots."
