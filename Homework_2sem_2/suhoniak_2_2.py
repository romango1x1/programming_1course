import math


class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Division by zero")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    @classmethod
    def from_string(cls, s):
        parts = s.split('/')
        if len(parts) == 1:
            return cls(int(parts[0]))
        return cls(int(parts[0]), int(parts[1]))

    def __add__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        if other.numerator == 0:
            raise ValueError("Division by zero")
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __gt__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        other = other if isinstance(other, Rational) else Rational.from_string(str(other))
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("Exponent must be an integer")
        if power == 0:
            return Rational(1)
        if power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        return Rational(self.denominator ** abs(power), self.numerator ** abs(power))

    def reciprocal(self):
        return Rational(self.denominator, self.numerator)

    def absolute(self):
        return Rational(abs(self.numerator), self.denominator)

    def sign(self):
        if self.numerator > 0:
            return 1
        if self.numerator < 0:
            return -1
        return 0

    def is_integer(self):
        return self.denominator == 1

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator


with open('input1.txt', 'r') as file:
    numbers = [Rational.from_string(line.strip()) for line in file]
numerators = [number.get_numerator() for number in numbers]

average_numerator = sum(numerators) // len(numerators)
average = Rational(average_numerator)

max_number = max(numbers)
max_abs_number = max(numbers, key=abs)

print("Max number:", max_number)
print("Max absolute number:", max_abs_number)
print("Average:", average)


def evaluate_polynomial(coeffs, x):
    result = Rational(0)
    n = len(coeffs)
    for i in range(n):
        result += coeffs[i] * Rational(x) ** (n - i - 1)
    return result


def find_roots(coeffs):
    n = len(coeffs)
    if n == 1:
        return []
    if n == 2:
        a, b = coeffs
        if a == 0:
            return []
        return [-b / a]
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
    return "Coefficients are not all integers, unable to find rational roots."


with open('input2.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
    for line in file_in:
        coeffs = [Rational.from_string(part.strip()) for part in line.strip().split(',')]
        file_out.write("Coefficients: " + str(coeffs) + '\n')

        value_at_1 = evaluate_polynomial(coeffs, 1)
        file_out.write("Value of the polynomial at x=1: " + str(value_at_1) + '\n')

        roots = find_roots([coef.numerator / coef.denominator for coef in coeffs])
        file_out.write("Roots: " + str(roots) + '\n\n')
