Composite is a structural design pattern that allows composing objects into a tree-like structure and work with the it as if it was a singular object.

Usage examples: The Composite pattern is pretty common in Python code. It’s often used to represent hierarchies of user interface components or the code that works with graphs.

Identification: If you have an object tree, and each object of a tree is a part of the same class hierarchy, this is most likely a composite. If methods of these classes delegate the work to child objects of the tree and do it via the base class/interface of the hierarchy, this is definitely a composite.

将对象组合成树形结构以表示‘部分-整体’的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。



