"""
 生成器 代码实例
 Builder Code Demo
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Car:
    """
    A car can have a GPS, trip computer and some number of seats. Different models of cars (sports car, SUV)
    """

    def __init__(self):
        self.parts = {}

    def set_part(self, part, value):
        self.parts[part] = value

    def __str__(self):
        return 'Parts: ' + str(self.parts)


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, num):
        pass

    @abstractmethod
    def set_engine(self, num):
        pass

    @abstractmethod
    def set_trip_computer(self, num):
        pass

    @abstractmethod
    def set_gps(self, num):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def product(self) -> Car:
        return self._product

    def set_seats(self, num):
        self._product.set_part('seats', num)

    def set_engine(self, name):
        self._product.set_part('engine', name)

    def set_trip_computer(self, exist):
        self._product.set_part('TripComputer', exist)

    def set_gps(self, exist):
        self._product.set_part('GPS', exist)


def build_sports_car() -> Car:
    print('---- buildASportsCar --- ')
    builder = CarBuilder()
    builder.set_seats(2)
    builder.set_engine('SportEngine')
    builder.set_trip_computer(True)
    builder.set_gps(True)
    return builder.product


if __name__ == "__main__":
    car = build_sports_car()
    print(car)
