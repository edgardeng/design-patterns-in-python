## Command (命令)
> Command is behavioral design pattern that converts requests or simple operations into objects.
  <br> 命令模式是行为设计模式，将请求或简单操作转换为对象。

> Most often it’s used as an alternative for callbacks to parameterizing UI elements with actions. It’s also used for queueing tasks, tracking operations history, etc.
  <br> 大多数情况下，它被用作通过操作参数化UI元素的回调的替代方法。它还用于排队任务、跟踪操作历史记录等

> The Command pattern is recognizable by behavioral methods in an abstract/interface type (sender) which invokes a method in an implementation of a different abstract/interface type (receiver) which has been encapsulated by the command implementation during its creation. Command classes are usually limited to specific actions.
  <br>通过抽象/接口类型（sender）中的行为方法，很好识别命令模式，该方法调用另一个抽象/接口类型（receiver）的实现中的方法，该方法在创建过程中已被命令实现封装。命令类通常仅限于特定的操作。
       
命令模式是一种设计模式，它尝试以对象来代表实际行动。命令对象可以把行动(action) 及其参数封装起来，于是这些行动可以被：
  
* 重复多次
* 取消（如果该对象有实现的话）
* 取消后又再重做

意图：将一个请求封装成一个对象，从而使您可以用不同的请求对客户进行参数化。

主要解决：在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，但某些场合，比如需要对行为进行记录、撤销或重做、事务等处理时，这种无法抵御变化的紧耦合的设计就不太合适。

何时使用：在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。在这种情况下，如何将"行为请求者"与"行为实现者"解耦？将一组行为抽象为对象，可以实现二者之间的松耦合。

如何解决：通过调用者调用接受者执行命令，顺序：调用者→命令→接受者。

关键代码：定义三个角色：1、received 真正的命令执行对象 2、Command 3、invoker 使用命令对象的入口

应用实例：struts 1 中的 action 核心控制器 ActionServlet 只有一个，相当于 Invoker，而模型层的类会随着不同的应用有不同的模型类，相当于具体的 Command。

优点： 1、降低了系统耦合度。 2、新的命令可以很容易添加到系统中去。

缺点：使用命令模式可能会导致某些系统有过多的具体命令类。

使用场景：认为是命令的地方都可以使用命令模式，比如： 1、GUI 中每一个按钮都是一条命令。 2、模拟 CMD。

注意事项：系统需要支持命令的撤销(Undo)操作和恢复(Redo)操作，也可以考虑使用命令模式，见命令模式的扩展。

命令模式结构示意图:
![](command_uml.jpg)

### 案例一
![](command-1.svg)

[代码 code](stock_buy_sell.py)

### 参考 Reference

* [ Command ](https://refactoring.guru/design-patterns/chain-of-responsibility)
 
* [菜鸟教程-命令模式](https://www.runoob.com/design-pattern/command-pattern.html)


