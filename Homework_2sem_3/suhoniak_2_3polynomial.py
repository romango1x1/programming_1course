class Polynomial(dict):
    def __init__(self, arg, coeff_type=float):
        super().__init__()
        self.coeff_type = coeff_type
        if isinstance(arg, str):
            self._parse_string(arg)
        elif isinstance(arg, dict):
            self.update(arg)
        elif isinstance(arg, list):
            for i, coeff in enumerate(arg):
                self[i] = coeff_type(coeff)
        elif isinstance(arg, (int, float)):
            self[0] = coeff_type(arg)
        else:
            raise ValueError("Invalid argument type")

    def _parse_string(self, string):
        terms = string.split('+')
        for term in terms:
            term = term.strip()
            if term:
                parts = term.split('x^')
                if len(parts) == 1:
                    if 'x' in parts[0]:
                        coeff = parts[0].split('x')[0].strip()
                        power = 1
                    else:
                        coeff = parts[0].strip()
                        power = 0
                else:
                    coeff = parts[0].strip()
                    power = int(parts[1])
                self[power] = self.coeff_type(coeff)

    def copy(self):
        return Polynomial(self, self.coeff_type)

    def as_type(self, coeff_type):
        return Polynomial({power: coeff_type(coeff) for power, coeff in self.items()}, coeff_type)

    def __str__(self):
        terms = []
        for power, coeff in sorted(self.items(), reverse=True):
            if power == 0:
                terms.append(str(coeff))
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
        return ' + '.join(terms)



    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        elif not isinstance(other, Polynomial):
            raise TypeError("Unsupported operand type")
        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)
        result = Polynomial(self.copy())
        for power, coeff in other.items():
            result[power] = result.get(power, 0) + coeff
        return result

    def __repr__(self):
        terms = []
        for power, coeff in sorted(self.items(), reverse=True):
            if power == 0:
                terms.append(repr(coeff))
            elif power == 1:
                terms.append(f"{repr(coeff)}x")
            else:
                terms.append(f"{repr(coeff)}x^{power}")
        return 'Polynomial({})'.format(', '.join(terms))

    def __iter__(self):
        return iter(sorted(self.items()))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        elif not isinstance(other, Polynomial):
            raise TypeError("Unsupported operand type")
        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)
        result = {}
        for power1, coeff1 in self.items():
            for power2, coeff2 in other.items():
                result[power1 + power2] = result.get(power1 + power2, 0) + coeff1 * coeff2
        return Polynomial(result, coeff_type=self.coeff_type)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        elif not isinstance(other, Polynomial):
            raise TypeError("Unsupported operand type")
        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)
        result = Polynomial(self.copy())
        for power, coeff in other.items():
            result[power] = result.get(power, 0) - coeff
        return result

    def __call__(self, value):
        return sum(coeff * (value ** power) for power, coeff in self.items())

    def __truediv__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Unsupported operand type")
        result = {power: coeff / value for power, coeff in self.items()}
        return Polynomial(result, coeff_type=self.coeff_type)

    def derivative(self):
        result = {power - 1: power * coeff for power, coeff in self.items() if power != 0}
        if not result:
            result[0] = self.coeff_type(0)
        return Polynomial(result, coeff_type=self.coeff_type)

    def primitive(self):
        result = {}
        previous_power = None
        for power, coeff in self.items():
            if power != 0:
                result[power + 1] = coeff / (power + 1)
            else:
                result[1] = coeff
            if previous_power is not None:
                for i in range(previous_power + 1, power):
                    result[i] = 0
            previous_power = power
        return Polynomial(result, coeff_type=self.coeff_type)

    def _reduce(self):
        zero_powers = [power for power, coeff in self.items() if coeff == self.coeff_type(0)]
        for power in zero_powers:
            del self[power]

    def newton_method(self, x0, epsilon=1e-6, max_iterations=100):
        x_prev = x0
        for _ in range(max_iterations):
            derivative = self.derivative()
            f_x = self(x_prev)
            if abs(f_x) < epsilon:
                return x_prev
            f_prime_x = derivative(x_prev)
            if f_prime_x == 0:
                return None  # Division by zero
            x_next = x_prev - f_x / f_prime_x
            if abs(x_next - x_prev) < epsilon:
                return x_next
            x_prev = x_next
        return None

    def lagrange_interpolation(points):
        n = len(points)
        result = Polynomial({})
        for i in range(n):
            term = Polynomial({0: points[i][1]})
            for j in range(n):
                if i != j:
                    term *= Polynomial({1: -points[j][0], 0: 1}) / (points[i][0] - points[j][0])
            result += term
        return result

    @classmethod
    def gcd(cls, poly1, poly2):
        while poly2:
            _, remainder = Polynomial.divide_with_remainder(poly1, poly2)
            poly1, poly2 = poly2, remainder
        return poly1

    @classmethod
    def divide_with_remainder(cls, dividend, divisor):
        if divisor == Polynomial({0: 0}):
            raise ValueError("Division by zero polynomial")

        quotient = Polynomial({})
        remainder = dividend.copy()

        while remainder and len(remainder) >= len(divisor):
            leading_term_dividend = max(remainder.keys())
            leading_term_divisor = max(divisor.keys())
            power_difference = leading_term_dividend - leading_term_divisor
            coefficient = remainder[leading_term_dividend] / divisor[leading_term_divisor]

            quotient[power_difference] = coefficient

            for power, coeff in divisor.items():
                remainder[power + power_difference] -= coeff * coefficient

            remainder._reduce()

        return quotient, remainder


# Tests
p1 = Polynomial("5x^2 + 2x + 7")
p2 = Polynomial("3x^2 + 3x + 3")
p3 = p1 + p2
print("p1 + p2:", p3)

p4 = p1 - p2
print("p1 - p2:", p4)

p5 = p1 * p2
print("p1 * p2:", p5)

print("p1(2):", p1(2))

p6 = p1 / 2
print("p1 / 2:", p6)

print("Derivative of p1:", p1.derivative())

print("Primitive of p1:", p1.primitive())

p = Polynomial({3: 2, 2: -2, 1: 7, 4: -10})
initial_guess = 3.0
root = p.newton_method(initial_guess)
if root is not None:
    print("Approximate root:", root)
else:
    print("Newton's method did not converge or no root found")

points = [(0, 2), (1, 3), (2, 5)]
lagrange_poly = Polynomial.lagrange_interpolation(points)
print("Lagrange interpolation polynomial:", lagrange_poly)

gcd_poly = Polynomial.gcd(p1, p2)
print("Greatest Common Divisor:", gcd_poly)
