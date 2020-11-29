"""
Visitor Pattern with Python Code

"""

from abc import abstractmethod, ABCMeta


#
class ComputerPart(metaclass=ABCMeta):
    """
    定义一个表示元素（Element）的接口
    Define an interface to represent an element
    """
    @abstractmethod
    def accept(self, computer_input):
        pass


class Keyboard(ComputerPart):
    def accept(self, computer_input):
        computer_input.visit_keyboard(self)


class Monitor(ComputerPart):
    def accept(self, computer_input):
        computer_input.visit_monitor(self)


class Mouse(ComputerPart):
    def accept(self, computer_input):
        computer_input.visit_mouse(self)


class Computer(ComputerPart):
    _parts = []

    def __init__(self):
        self._parts.append(Mouse())
        self._parts.append(Keyboard())
        self._parts.append(Monitor())

    def accept(self, computer_input):
        for aPart in self._parts:
            aPart.accept(computer_input)
        computer_input.visit_computer(self)


#
class ComputerPartVisitor(metaclass=ABCMeta):
    """
    Define an interface that represents the visitor
    定义一个表示访问者的接口
    """
    @abstractmethod
    def visit_computer(self, in_computer):
        pass

    @abstractmethod
    def visit_mouse(self, inMouse):
        pass

    @abstractmethod
    def visit_keyboard(self, inKeyboard):
        pass

    @abstractmethod
    def visit_monitor(self, inMonitor):
        pass


# 实现访问者接口的实体类
class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit_computer(self, inComputer):
        print("Displaying {0}. Called in {1}".format(inComputer.__class__.__name__, self.__class__.__name__))

    def visit_mouse(self, inMouse):
        print("Displaying {0}. Called in {1}".format(inMouse.__class__.__name__, self.__class__.__name__))

    def visit_keyboard(self, inKeyboard):
        print("Displaying {0}. Called in {1}".format(inKeyboard.__class__.__name__, self.__class__.__name__))

    def visit_monitor(self, inMonitor):
        print("Displaying {0}. Called in {1}".format(inMonitor.__class__.__name__, self.__class__.__name__))


# 调用输出
if __name__ == '__main__':
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())
