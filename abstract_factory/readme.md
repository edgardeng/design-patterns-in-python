## 抽象工厂（Abstract Factory）
> Abstract Factory is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.
  <br/>抽象工厂是一种创造性的设计模式，它解决了在不指定具体类的情况下创建整个产品系列的问题

> Abstract Factory defines an interface for creating all distinct products but leaves the actual product creation to concrete factory classes. Each factory type corresponds to a certain product variety.
  <br/>抽象工厂定义了一个用于创建所有不同产品的接口，但将实际的产品创建留给具体的工厂类。每种工厂类型对应于某种产品种类。
  
意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

主要解决：主要解决接口选择的问题。

何时使用：系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。

如何解决：在一个产品族里面，定义多个产品

## 案例一

![](./structure.png)

解释：
1. 创建 AbstractProductA 和 AbstractProductB 抽象类
2. 创建产品实类ConcreteProductA1和ConcreteProductA2 继承至 AbstractProductA
3. 创建产品实类ConcreteProductB1和ConcreteProductB2 继承至 AbstractProductB
4. 创建抽象工厂类 AbstractFactory （具有方法 create_product_a, create_product_b）
5. 定义工厂类 ConcreteFactory1 (生产ProductA1+ProductB1) 和 ConcreteFactory2 (生产ProductA2+ProductB2)
[代码 Demo](./index.py)

## 案例二
![](./solution2.png)

[代码 Demo](./furniture_factory.py)
 
### 参考 Reference

* [abstract-factory](https://refactoring.guru/design-patterns/abstract-factory)
 
* [菜鸟教程-抽象工厂模式](https://www.runoob.com/design-pattern/abstract-factory-pattern.html)
