from abc import(ABC, abstractmethod)
import math

class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r: float):
        self.r : float = r

    def perimeter(self):
        print(round(2 * self.r* math.pi, 3))

    def area(self):
        print(round(math.pi * self.r**2, 3))

class Rectangle(Shape):
    def __init__(self, b: float, h : float):
        self.b : float = b
        self.h : float = h

    def perimeter(self):
        print(round((self.b + self.h) *2, 3))

    def area(self):
        print(round(self.b * self.h, 3))

cerchio : Circle = Circle(3.2)
cerchio.perimeter()
cerchio.area()
rettangolo : Rectangle = Rectangle(5, 3)
rettangolo.perimeter()
rettangolo.area()

