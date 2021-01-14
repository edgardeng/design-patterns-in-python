## Template Method （模板方法）
> Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
<br> 模板方法是一种行为型设计模式，在超类中定义算法的骨架，但允许子类在不改变算法结构的情况下覆盖算法的特定步骤

> The Template Method pattern is quite common in Python frameworks. Developers often use it to provide framework users with a simple means of extending standard functionality using inheritance.
<br> 模板方法模式在Python框架中非常常见。开发人员经常使用它为框架用户提供一种简单的方法，使用继承来扩展标准功能

> Template Method can be recognized by behavioral methods that already have a “default” behavior defined by the base class.
<br> 模板方法可以通过行为方法识别，它有一个由基类定义的“默认”行为。

意图：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

主要解决：一些方法通用，却在每一个子类都重新写了这一方法。

何时使用：有一些通用的方法。

如何解决：将这些通用算法抽象出来。

关键代码：在抽象类实现，其他步骤在子类实现。

应用实例： 1、在造房子的时候，地基、走线、水管都一样，只有在建筑的后期才有加壁橱加栅栏等差异。 2、西游记里面菩萨定好的 81 难，这就是一个顶层的逻辑骨架。 3、spring 中对 Hibernate 的支持，将一些已经定好的方法封装起来，比如开启事务、获取 Session、关闭 Session 等，程序员不重复写那些已经规范好的代码，直接丢一个实体就可以保存。

优点： 1、封装不变部分，扩展可变部分。 2、提取公共代码，便于维护。 3、行为由父类控制，子类实现。

缺点：每一个不同的实现都需要一个子类来实现，导致类的个数增加，使得系统更加庞大。

使用场景： 1、有多个子类共有的方法，且逻辑相同。 2、重要的、复杂的方法，可以考虑作为模板方法

### 案例一

[代码code](game.py)

### 参考 Reference

* [ Template ](https://refactoring.guru/design-patterns/template-method)
 
* [菜鸟教程-模板模式](https://www.runoob.com/design-pattern/template-pattern.html)

