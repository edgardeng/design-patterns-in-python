## Command (命令)
> 命令模式是一种设计模式，它尝试以对象来代表实际行动。命令对象可以把行动(action) 及其参数封装起来，于是这些行动可以被：
  
> * 重复多次
> * 取消（如果该对象有实现的话）
> * 取消后又再重做

Command is behavioral design pattern that converts requests or simple operations into objects.

Usage examples: The Command pattern is pretty common in Python code. Most often it’s used as an alternative for callbacks to parameterizing UI elements with actions. It’s also used for queueing tasks, tracking operations history, etc.

Identification: The Command pattern is recognizable by behavioral methods in an abstract/interface type (sender) which invokes a method in an implementation of a different abstract/interface type (receiver) which has been encapsulated by the command implementation during its creation. Command classes are usually limited to specific actions.
