# 设计模式之Python实现

> 本仓库主要参考来源: [DESIGN PATTERNS in Refactoring.Guru](https://refactoring.guru/design-patterns/python)

[中文版](./README-CN.md)

## 创建型模式 

| |创建型模式|||
|:----|:----|:----|:----|
| ![](img/abstract-factory-mini.png) |抽象工厂 (Abstract Factory)| 允许您生成一系列相关对象，而无需指定它们的具体类. | [代码](./abstract_factory/index.py)|
| ![](img/builder-mini.png) |生成器 (Builder) | 逐步构造复杂的对象，通过使用相同的构造代码生成对象的不同类型和表示 | [代码](./builder/index.py)|
| ![](img/factory-method-mini.png) | 工厂方法 (Factory Method) | 提供在超类中创建对象的接口，但允许子类更改将要创建的对象的类型 | [代码](./factory/index.py)
| ![](img/prototype-mini.png) |原型 (Prototype) | 允许您复制现有对象而不使代码依赖于它们的类.|[代码](./prototype/index.py)|
| ![](img/singleton-mini.png) |单例 (Singleton) | 确保类只有一个实例，同时为该实例提供全局访问点 | [代码](./singleton/index.py)|


## 结构型模式

| | 结构型模式 |||
|:----|:----|:----|:----|
|![](img/adapter-mini.png) | 适配器 (Adapter) | 允许具有不兼容接口的对象进行协作 |[code](Adapter/index.py)|
|![](img/bridge-mini.png) | 桥接 (Bridge) | 允许您将一个大类或一组密切相关的类拆分为两个独立的层次结构抽象和实现，它们可以相互独立地开发.|[code](./Bridge/index.py)|
|![](img/composite-mini.png) | 组合 (Composite) | 允许您将对象组合到树结构中，然后将这些结构视为单个对象来处理.|[code](./Composite/index.py)|
|![](img/decorator-mini.png) | 装饰器 (Decorator) | 通过将这些对象放置在包含行为的特殊包装对象中，可以将这些对象附加到对象.|[code](./Decorator/index.py)|
|![](img/facade-mini.png) | 外观 (Facade) | 为库、框架或任何其他复杂类集,提供简化的接口.|[code](./Facade/index.py)|
|![](img/flyweight-mini.png) | 享元 (Flyweight) | 通过共享多个对象之间状态的公共部分,而不是将所有数据保留在每个对象中，从而将更多的对象放入可用的RAM内存中.|[code](./Flyweight/index.py)|
|![](img/proxy-mini.png) | 代理 (Proxy) | 允许您为另一个对象提供替换项或占位符。代理控制对原始对象的访问，允许您在请求到达原始对象之前或之后执行某些操作.|[code](./Proxy/index.py)|


## 行为型模式

| | 行为型模式 |||
|:----|:----|:----|:----|
|![](/img/chain-of-responsibility-mini.png) | 责任链 (Chain of Responsibility) | 沿着程序链来传递请求。收到请求后，每个处理程序决定：是处理该请求，还是将其传递给链中的下一个处理程序 |[code](./Chain/index.py)|
|![](img/command-mini.png) | 命令 (Command) | 将请求转换为包含有关该请求的所有信息的独立对象。该转换让我们使用不同的请求参数，将请求的执行进行延迟或加入队列，并支持可撤消的操作|[code](./Command/index.py)|
|![](img/iterator-mini.png) | 迭代器 (Iterator) |让我们遍历集合中的元素，但不公开其底层表示（列表、堆栈、树等）|[code](./Iterator/index.py)|
|![](img/mediator-mini.png) | 中介者(Mediator) | 减少对象之间的混乱依赖关系。该模式限制了对象之间的直接通信，并强制其通过中介对象进行协作 |[code](./Mediator/index.py)|
|![](img/memento-mini.png) | 备忘录 (Memento) | 保存和恢复对象的先前状态，而不显示其实现的详细信息|[code](./Memento/index.py)|
|![](img/observer-mini.png) | 观察者 (Observer) | 定义订阅机制，以通知多个对象所观察的对象发生的任何事件 |[code](./Observer/index.py)|
|![](img/state-mini.png) | 状态 (State) | 对象在其内部状态变化时，改变其行为。就像对象改变了它的类|[code](./State/index.py)|
|![](img/strategy-mini.png) | 策略 (Strategy) | 定义一系列算法，将每个算法放入单独的类中，并使其对象可互换。|[code](./Strategy/index.py)|
|![](img/template-method-mini.png) | 模板方法 (Template Method)  | 在超类中定义算法的骨架，但允许子类重写算法的特定步骤而不更改其结构。|[code](./Template_Method /index.py)|
|![](img/visitor-mini.png) | 访问者 (Visitor) | 将算法与其操作的对象分开|[code](./Visitor/index.py)|
 