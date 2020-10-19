## 抽象工厂（Abstract Factory）
> 抽象工厂模式提供了一种方式，可以将一组具有同一主题的单独的工厂封装起来。在正常使用中，客户端程序需要创建抽象工厂的具体实现，然后使用抽象工厂作为接口来创建这一主题的具体对象。

Abstract Factory is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.

Abstract Factory defines an interface for creating all distinct products but leaves the actual product creation to concrete factory classes. Each factory type corresponds to a certain product variety.

> The Abstract Factory pattern is pretty common in Python code. Many frameworks and libraries use it to provide a way to extend and customize their standard components.

Identification: The pattern is easy to recognize by methods, which return a factory object. Then, the factory is used for creating specific sub-components.

Conceptual Example
This example illustrates the structure of the Abstract Factory design pattern. It focuses on answering these questions:

What classes does it consist of?
What roles do these classes play?
In what way the elements of the pattern are related?
 main.py: Conceptual example
