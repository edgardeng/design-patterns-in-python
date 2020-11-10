## 抽象工厂（Abstract Factory）
> Abstract Factory is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.
  抽象工厂是一种创造性的设计模式，它解决了在不指定具体类的情况下创建整个产品系列的问题

> Abstract Factory defines an interface for creating all distinct products but leaves the actual product creation to concrete factory classes. Each factory type corresponds to a certain product variety.
  抽象工厂定义了一个用于创建所有不同产品的接口，但将实际的产品创建留给具体的工厂类。每种工厂类型对应于某种产品种类。
  
The pattern is easy to recognize by methods, which return a factory object. Then, the factory is used for creating specific sub-components.

通过返回工厂对象的方法,就可以判断是否是抽象工厂模式。然后，工厂对象用于创建特定的子组件

### 参考 Reference

* [abstract-factory](https://refactoring.guru/design-patterns/abstract-factory)
 
