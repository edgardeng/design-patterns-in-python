from __future__ import annotations
from abc import ABC, abstractmethod


class Order(ABC):
    """
    Order:  The Command interface to execute buy or sell command
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class Stock:
    def __init__(self, name=None, q=None):
        self.name = name or 'ABC'
        self.quantity = q or 10

    def buy(self):
        print("Stock [ Name: %s , Quantity: %d] bought" % (self.name, self.quantity))

    def sell(self):
        print("Stock [ Name: %s , Quantity: %d] sold" % (self.name, self.quantity))


class BuyStock(Order):
    def __init__(self, s):
        self.stock = s

    def execute(self):
        self.stock.buy()


class SellStock(Order):
    def __init__(self, s):
        self.stock = s

    def execute(self):
        self.stock.sell()


class Broker:
    def __init__(self):
        self.orderList = []

    def add_order(self, order):
        self.orderList.append(order)

    def place_all_order(self):
        for order in self.orderList:
            order.execute()
        self.orderList.clear()


if __name__ == '__main__':
    abcStock = Stock()
    buy = BuyStock(abcStock)
    sell = SellStock(abcStock)

    broker = Broker()
    broker.add_order(buy)
    broker.add_order(sell)
    broker.place_all_order()
