from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    """
    1. 创建 Employee 类，该类带有 Employee 对象的列表

    """

    def __init__(self, name, dept, sal):
        self.name = name
        self.dept = dept
        self.salary = sal
        self.subordinates = []

    @abstractmethod
    def operation(self) -> str:
        pass

    def add(self, e):
        self.subordinates.append(e)

    def remove(self, e):
        self.subordinates.remove(e)

    def get_subordinates(self) -> List:
        return self.subordinates

    def __str__(self):
        return "Employee: [ Name : %s, dept :%s, salary :%d ]" % (self.name, self.dept, self.salary)


class Manager(Employee):
    def operation(self) -> str:
        return ' manage working'


class Staff(Employee):
    def operation(self) -> str:
        return ' common working'


if __name__ == '__main__':
    CEO = Manager("John", "CEO", 30000);

    headSales = Manager("Robert", "Head Sales", 20000);

    headMarketing = Manager("Michel", "Head Marketing", 20000);

    clerk1 = Staff("Laura", "Marketing", 10000)
    clerk2 = Staff("Bob", "Marketing", 10000)
    salesExecutive1 = Staff("Richard", "Sales", 10000);
    salesExecutive2 = Staff("Rob", "Sales", 10000);

    CEO.add(headSales)
    CEO.add(headMarketing)

    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)

    headMarketing.add(clerk1)
    headMarketing.add(clerk2)
    print(CEO)
    for manager in CEO.get_subordinates():
        print(manager, manager.operation())
        for staff in manager.get_subordinates():
            print(staff, staff.operation())
