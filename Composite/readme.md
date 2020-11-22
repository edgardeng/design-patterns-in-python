## Composite (组合)
> Composite is a structural design pattern that allows composing objects into a tree-like structure and work with the it as if it was a singular object.
<br> 组合是一种结构设计模式，将对象组合成树状结构，并将其当作单个对象来处理， 

> It’s often used to represent hierarchies of user interface components or the code that works with graphs.
<br> 通常用于表示用户界面组件的层次结构或处理图形的代码
>  If you have an object tree, and each object of a tree is a part of the same class hierarchy, this is most likely a composite. If methods of these classes delegate the work to child objects of the tree and do it via the base class/interface of the hierarchy, this is definitely a composite.
如果有一个对象树，并且树的每个对象都是同一类层次结构的一部分，那么可能就是一个组合。如果类的方法将工作委托给树的子对象，并通过层次结构的基类/接口来完成，那么这绝对是一个组合

意图：将对象组合成树形结构以表示"部分-整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

主要解决：它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以像处理简单元素一样来处理复杂元素，从而使得客户程序与复杂元素的内部结构解耦。

何时使用： 1、您想表示对象的部分-整体层次结构（树形结构）。 2、您希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

如何解决：树枝和叶子实现统一接口，树枝内部组合该接口。

关键代码：树枝内部组合该接口，并且含有内部属性 List，里面放 Component。

应用实例： 1、算术表达式包括操作数、操作符和另一个操作数，其中，另一个操作符也可以是操作数、操作符和另一个操作数。 2、在 JAVA AWT 和 SWING 中，对于 Button 和 Checkbox 是树叶，Container 是树枝。

优点： 1、高层模块调用简单。 2、节点自由增加。

缺点：在使用组合模式时，其叶子和树枝的声明都是实现类，而不是接口，违反了依赖倒置原则。

使用场景：部分、整体场景，如树形菜单，文件、文件夹的管理


### 实例一

职员树

[代码](./employee.py)

### 参考 Reference

* [Composite ](https://refactoring.guru/design-patterns/composite)
 
* [菜鸟教程-组合模式](https://www.runoob.com/design-pattern/composite-pattern.html)
