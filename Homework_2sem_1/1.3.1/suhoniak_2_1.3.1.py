from math import pi, sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        s_squared = p * (p - self.a) * (p - self.b) * (p - self.c)
        return sqrt(s_squared) if s_squared >= 0 else 0


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return (self.a + self.b) * 0.5 * self.d


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)


def read_files(filenames):
    figures = []
    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                figure_type = parts[0]
                parameters = list(map(float, parts[1:]))
                if figure_type == 'Triangle':
                    figures.append(Triangle(*parameters))
                elif figure_type == 'Rectangle':
                    figures.append(Rectangle(*parameters))
                elif figure_type == 'Trapeze':
                    figures.append(Trapeze(*parameters))
                elif figure_type == 'Parallelogram':
                    figures.append(Parallelogram(*parameters))
                elif figure_type == 'Circle':
                    figures.append(Circle(*parameters))
    return figures


def find_largest_area_and_perimeter(figures):
    largest_area_figure = max(figures, key=lambda f: f.area(), default=None)
    largest_perimeter_figure = max(figures, key=lambda f: f.perimeter(), default=None)

    return largest_area_figure, largest_perimeter_figure


def main():
    filenames = ['input01.txt', 'input02.txt', 'input03.txt']
    figures = read_files(filenames)
    largest_area_figure, largest_perimeter_figure = find_largest_area_and_perimeter(figures)

    if largest_area_figure and largest_perimeter_figure:
        print("Figure with the largest area:", largest_area_figure.__class__.__name__)
        print(f"Area: {largest_area_figure.area():.4f}")
        print("Figure with the largest perimeter:", largest_perimeter_figure.__class__.__name__)
        print(f"Perimeter: {largest_perimeter_figure.perimeter():.4f}")
    else:
        print("No figures found in the input files.")


if __name__ == "__main__":
    main()
