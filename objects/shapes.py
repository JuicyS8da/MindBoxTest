from math import pi, sqrt

class BaseShape:
    def calc_square(self):
        raise NotImplementedError(f"Method 'calc_square' hasn't been overridden")

class Circle(BaseShape):
    def __init__(self, radius: float):
        self.radius = radius

    def calc_square(self) -> float:
        return pi * self.radius ** 2

class Triangle(BaseShape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.a = side1
        self.b = side2
        self.c = side3

        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise ValueError('The sum of the two sides of the triangle must be greater than the third side of the triangle')

    def calc_square(self) -> float:
        perimeter = (self.a + self.b + self.c) / 2
        return sqrt(perimeter * (perimeter - self.a) * (perimeter - self.b) * (perimeter - self.c))

    def is_right_triangle(self) -> bool:
        sorted_sides = sorted(list([self.a, self.b, self.c]))
        return bool(sorted_sides[0] > 0 and (sorted_sides[0] * sorted_sides[0]) + (sorted_sides[1] * sorted_sides[1]) == (sorted_sides[2] * sorted_sides[2]))

def Square(BaseShape):
    """ Test class for adding new shapes """
    def __init__(self, side: float):
        if side < 0:
            raise ValueError
        self.a = side

    def calc_square(self) -> float:
        return self.a ** 2

def Rectangle(BaseShape):
    """ Test class for adding new shapes """
    def __init__(self, side1: float, side2: float):
        self.a = side1
        self.b = side2

    def calc_square(self) -> float:
        return self.a * self.b

def calculate_area(*args, **kwargs) -> float:
    """ Вычисление площади фигуры без знания типа фигуры в compile-time """
    if len(args) == 1:
        return Square(*args).calculate_area()
    elif len(args) == 2:
        return Rectangle(*args).calculate_area()
    elif len(args) == 3:
        return Triangle(*args).calculate_area()
    else:
        raise NotImplementedError(
            "The method of calculating the area of this figure is not implemented!"
        )
