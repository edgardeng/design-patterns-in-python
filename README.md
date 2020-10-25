# Design Patterns implemented in Python

> reference from [DESIGN PATTERNS in Refactoring.Guru](https://refactoring.guru/design-patterns/python)

## Creational Patterns

| |Creational Patterns|||
|:----|:----|:----|:----|
|![](./img/abstract-factory-mini.png) |Abstract Factory|Lets you produce families of related objects without specifying their concrete classes.|[code](./abstract_factory/index.py)|
|![](img/builder-mini.png) |Builder |Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.|[code](./builder/index.py)|
|![](img/factory-method-mini.png) |Factory Method |Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created|[code](./factory/index.py)
|![](img/prototype-mini.png) |Prototype|Lets you copy existing objects without making your code dependent on their classes.|[code](./prototype/index.py)|
|![](img/singleton-mini.png) |Singleton|Lets you ensure that a class has only one instance, while providing a global access point to this instance.|[code](./singleton/index.py)|


## Structural Patterns

| |Creational Patterns|||
|:----|:----|:----|:----|

|![](img/adapter-mini.png) | Adapter | Allows objects with incompatible interfaces to collaborate. |[code](./adapter/index.py)|
|![](img/bridge-mini.png) | Bridge | Lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.|[code](./Bridge/index.py)|
|![](img/composite-mini.png) | Composite | Lets you compose objects into tree structures and then work with these structures as if they were individual objects.|[code](./Composite/index.py)|
|![](img/decorator-mini.png) | Decorator | Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.|[code](./Decorator/index.py)|
|![](img/facade-mini.png) | Facade | Provides a simplified interface to a library, a framework, or any other complex set of classes.|[code](./Facade/index.py)|
|![](img/flyweight-mini.png) | Flyweight | Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.|[code](./Flyweight/index.py)|
|![](img/prototype-mini.png) | Proxy | Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.|[code](./Proxy/index.py)|
