## Decorator
> Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects.
<br> 装饰器是一种结构型设计模式，通过将新行为放入特殊的包装对象中来动态地向对象添加新行为

> Decorator can be recognized by creation methods or constructor that accept objects of the same class or interface as a current class.
<br>通过创建方法或构造函数来识别装饰器，它们接受与当前类相同的类或接口的对象。


意图：动态地给一个对象添加一些额外的职责。就增加功能来说，装饰器模式相比生成子类更为灵活。修饰模式相比生成子类更为灵活，可以给某个对象而不是整个类添加一些功能

主要解决：一般的，我们为了扩展一个类经常使用继承方式实现，由于继承为类引入静态特征，并且随着扩展功能的增多，子类会很膨胀。

何时使用：在不想增加很多子类的情况下扩展类。

如何解决：将具体功能职责划分，同时继承装饰者模式。

关键代码： 1、Component 类充当抽象角色，不应该具体实现。 2、修饰类引用和继承 Component 类，具体扩展类重写父类方法。

应用实例： 1、孙悟空有 72 变，当他变成"庙宇"后，他的根本还是一只猴子，但是他又有了庙宇的功能。 2、不论一幅画有没有画框都可以挂在墙上，但是通常都是有画框的，并且实际上是画框被挂在墙上。在挂在墙上之前，画可以被蒙上玻璃，装到框子里；这时画、玻璃和画框形成了一个物体。

优点：装饰类和被装饰类可以独立发展，不会相互耦合，装饰模式是继承的一个替代模式，装饰模式可以动态扩展一个实现类的功能。

缺点：多层装饰比较复杂。

使用场景： 1、扩展一个类的功能。 2、动态增加功能，动态撤销。

### 案例一

通知案例

![](./solution_1.png)

[代码（code）](./notifications.py)

### 案例二

使用Python的方法装饰器
```
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

```
### 案例三

使用Python的类装饰器

```
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

```

### 参考 Reference

* [ Decorator ](https://refactoring.guru/design-patterns/decorator)
 
* [菜鸟教程-装饰器模式](https://www.runoob.com/design-pattern/decorator-pattern.html)
