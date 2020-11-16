## 工厂方法（Factory Method）
> 在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象

> Factory method is a creational design pattern which solves the problem of creating product objects without specifying their concrete classes.
  <br>工厂方法是一种创造型设计模式，解决了在不指定具体类的情况下创建产品对象的问题
  
定义一个创建对象的接口，但让实现这个接口的类来决定实例化哪个类。工厂方法让类的实例化推迟到子类中进行。

> Factory Method defines a method, which should be used for creating objects instead of direct constructor call (new operator). Subclasses can override this method to change the class of objects that will be created.
  <br>工厂方法定义了一个方法，用来创建对象，而不是直接调用构造函数(new操作符)。子类可以重写此方法以更改将要创建的对象的类

意图：定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。

主要解决：主要解决接口选择的问题。

何时使用：我们明确地计划不同条件下创建不同实例时。

如何解决：让其子类实现工厂接口，返回的也是一个抽象的产品。

> 和抽象工厂模式不同的是： 抽象工厂生成多个产品类的实例。 工厂方法生成一个产品的不同实例

## 案例

![](./solution1.png)

1. 构造一个交通工具生成的工厂超类，负责生产交通工具， 使用交通工具
2. 可继承多个工厂超类，负责生产具体的交通工具

![](./solution2.png)

1. 构造一个交通工具超类
2. 可继承多个交通工具超类，用于工厂类构建不同的实例


[代码 Demo](./transport_factory.py)
 
### 参考 Reference

* [Factory Method](https://refactoring.guru/design-patterns/factory-method)
 
* [菜鸟教程-工厂模式](https://www.runoob.com/design-pattern/factory-pattern.html)


