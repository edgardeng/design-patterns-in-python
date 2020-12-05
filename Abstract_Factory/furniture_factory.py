"""
 抽象工厂 代码实例
 Abstract Factory Code Demo
 家具工厂
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Chair(ABC):
    """
    product interface 1: Chair
    """

    @abstractmethod
    def sit_on(self) -> str:
        pass


class Sofa(ABC):
    """
    product interface 2: Sofa
    """

    @abstractmethod
    def lie_on(self) -> str:
        pass


class ModernChair(Chair):
    """
    product implement Chair: ModernChair
    """

    def sit_on(self) -> str:
        return 'I sit on a Modern Chair'


class ClassicChair(Chair):
    """
    product implement Chair: ClassicChair
    """

    def sit_on(self) -> str:
        return 'I sit on a Classic Chair'


class ModernSofa(Sofa):
    """
    product implement Sofa: ModernSofa
    """

    def lie_on(self) -> str:
        return 'I sit on a Modern Sofa'


class ClassicSofa(Sofa):
    """
    product implement Sofa: ClassicSofa
    """

    def lie_on(self) -> str:
        return 'I sit on a Classic Sofa'


class FurnitureFactory(ABC):
    """
    一个抽象工厂接口 定义了一系列方法，用来返回不同的抽象产品
    The Abstract Factory interface declares a set of methods that return different abstract products.
    家具工厂生成沙发和椅子 Furniture Factory produce Chair and SOfa
    """

    @abstractmethod
    def produce_chair(self) -> Chair:
        pass

    @abstractmethod
    def produce_sofa(self) -> Sofa:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    """
    一个抽象工厂的实现类 implement FurnitureFactory to produce true product
    """

    def produce_chair(self) -> Chair:
        print('ModernFurnitureFactory produce chair ...')
        return ModernChair()

    def produce_sofa(self) -> Sofa:
        print('ModernFurnitureFactory produce sofa ...')
        return ModernSofa()


class ClassicFurnitureFactory(FurnitureFactory):
    """
    一个抽象工厂的实现类 implement FurnitureFactory to produce true product
    """

    def produce_chair(self) -> Chair:
        print('ClassicFurnitureFactory produce chair ...')
        return ClassicChair()

    def produce_sofa(self) -> Sofa:
        print('ClassicFurnitureFactory produce sofa ...')
        return ClassicSofa()


def client_code(factory: FurnitureFactory):
    chair = factory.produce_chair()
    print(chair.sit_on())
    sofa = factory.produce_sofa()
    print(sofa.lie_on())


if __name__ == '__main__':
    print('\r\n--- I want some Modern Furniture ---\r\n')
    client_code(ModernFurnitureFactory())
    print('\r\n--- I want some Classic Furniture ---\r\n')
    client_code(ClassicFurnitureFactory())
