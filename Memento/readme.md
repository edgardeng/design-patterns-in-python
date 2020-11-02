## Memento（备忘录）
> 在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样就可以将该对象恢复到原先保存的状态

Memento is a behavioral design pattern that allows making snapshots of an object’s state and restoring it in future.

Usage examples: The Memento’s principle can be achieved using the serialization, which is quite common in Python. While it’s not the only and the most efficient way to make snapshots of an object’s state, it still allows storing state backups while protecting the originator’s structure from other objects.
