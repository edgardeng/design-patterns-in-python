from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle::draw()")


class Circle(Shape):
    def draw(self):
        print("Circle::draw()")


class Triangle(Shape):
    def draw(self):
        print("Triangle::draw()")


class ShapeMaker():
    def __init__(self, rectangle=None, circle=None, triangle=None) -> None:
        self._rectangle = rectangle or Rectangle()
        self._circle = circle or Circle()
        self._triangle = triangle or Triangle()

    def draw(self):
        print('ShapeMaker: start draw')
        self._rectangle.draw()
        self._circle.draw()
        self._triangle.draw()

    def draw_rectangle(self):
        self._rectangle.draw()

    def draw_circle(self):
        self._circle.draw()

    def draw_triangle(self):
        self._triangle.draw()


if __name__ == '__main__':
    ShapeMaker().draw()
