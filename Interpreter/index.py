from abc import ABC


class IntegerExpression(ABC):

    def evaluate(self, context) -> int:
        pass

    def replace(self, character, expression):
        pass

    def copied(self):
        pass


class IntegerContext(object):
    _data = {}  # : [Character:Int] = [:]

    def lookup(self, name: str) -> int:
        return self._data[name]

    def assign(self, expression: IntegerExpression, value: int):
        self._data[expression._name] = value


class IntegerVariableExpression(IntegerExpression):
    _name = None

    def __init__(self, n):
        self._name = n

    def evaluate(self, context: IntegerContext) -> int:
        return context.lookup(self._name)

    def replace(self, name: str, integerExpression: IntegerExpression) -> IntegerExpression:
        if name == self._name:
            return integerExpression.copied()
        else:
            return IntegerVariableExpression(self._name)

    def copied(self, ) -> IntegerExpression:
        return IntegerVariableExpression(self._name)


class AddExpression(IntegerExpression):
    operand1: IntegerExpression
    operand2: IntegerExpression

    def __init__(self, op1: IntegerExpression, op2: IntegerExpression):
        self.operand1 = op1
        self.operand2 = op2

    def evaluate(self, context: IntegerContext) -> int:
        return self.operand1.evaluate(context) + self.operand2.evaluate(context)

    def replace(self, character: str, expression: IntegerExpression) -> IntegerExpression:
        return AddExpression(self.operand1.replace(character, expression),
                             self.operand2.replace(character, expression))

    def copied(self) -> IntegerExpression:
        return AddExpression(self.operand1, self.operand2)


if __name__ == "__main__":
    context = IntegerContext()
    a = IntegerVariableExpression("A")
    b = IntegerVariableExpression("B")
    c = IntegerVariableExpression("C")

    expression = AddExpression(a, AddExpression(b, c))  # a + (b + c)

    context.assign(a, 2)
    context.assign(b, 1)
    context.assign(c, 3)
    result = expression.evaluate(context)
    print(result)
