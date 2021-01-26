import functools
import time
import types
from dataclasses import dataclass

def time_recorder(f):
    """
    Print the execution time of decorated function.
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        rt = f(*args, **kwargs)
        execution_time = time.perf_counter() - start
        print(f"The execution time of {f.__name__!r} is {execution_time:.3f} secs")
        return rt

    return wrapper


@time_recorder
def test(n):
    time.sleep(n)
    print('end')


def time_recorder_for_kls(kls):
    class Wapper(object):
        def __init__(self, *args, **kwargs):
            self.instance = kls(*args, **kwargs)

        def __getattribute__(self, attr):
            try:
                ar = super().__getattribute__(attr)
            except AttributeError:
                pass
            else:
                return ar
            f = self.instance.__getattribute__(attr)
            if isinstance(f, (types.MethodType, types.FunctionType)):
                return time_recorder(f)
            else:
                return f

    return Wapper


@time_recorder_for_kls
class T:

    def func_1(self,a):
        time.sleep(0.1)
        print('end func 1')

    @classmethod
    def func_2(cls):
        time.sleep(0.2)
        print('end func 2')

    @staticmethod
    def func_3():
        time.sleep(0.3)
        print('end func 3')

# Python3.7  dataclass的定义位于[PEP-557](https://www.python.org/dev/peps/pep-0557/)，根据定义一个dataclass是指“一个带有默认值的可变的namedtuple”

@dataclass
class InventoryItem:
    """
    1. 相比普通class，dataclass通常不包含私有属性，数据可以直接访问
    2. dataclass的repr方法通常有固定格式，会打印出类型名以及属性名和它的值
    3. dataclass拥有__eq__和__hash__魔法方法
    4. dataclass有着模式单一固定的构造方式，或是需要重载运算符，而普通class通常无需这些工作
    """
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        print(f'name={self.name},price={self.unit_price},quntirty={self.quantity_on_hand}')
        return self.unit_price * self.quantity_on_hand


if __name__ == '__main__':
    test(1)
    T().func_1()
    T().func_2() # 不能使用T.func2
    T().func_3()
    # T.func_2()
    # T.func_3()
    print(InventoryItem('a',1,2).total_cost())
