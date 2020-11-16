"""

原型设计模式 代码实例 （原型注册表）
Prototype Code Demo （Prototype registry ）

"""
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def getColor(self) -> str:
        pass

    def clone(self):
        pass


# class Button():
class Button(Prototype):
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.color = c

    def getColor(self) -> str:
        return self.color

    def clone(self):
        return Button(self.x, self.y, self.color)

    def __str__(self):
        return 'x: %d, y: %d, c: %s' % (self.x, self.y, self.color)


class PrototypeRegistry():
    def __init__(self, ):
        self.items = {}

    def addItem(self, id: str, p):
        self.items[id] = p

    def getById(self, id: str):
        return self.items[id]

    def getByColor(self, c: str):
        for item in self.items.values():
            if item.getColor() == c:
                return item.clone()


if __name__ == '__main__':
    button = Button(1, 1, 'red')
    registry = PrototypeRegistry()
    registry.addItem('LandingButton', button)
    print(id(button))
    print(button)
    button_copy = registry.getByColor('red')
    print(id(button_copy))
    print(button_copy)
