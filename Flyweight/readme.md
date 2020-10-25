Flyweight is a structural design pattern that allows programs to support vast quantities of objects by keeping their memory consumption low.

Usage examples: The Flyweight pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle with a shortage of RAM, then you might just ignore this pattern for a while.

Identification: Flyweight can be recognized by a creation method that returns cached objects instead of creating new.


使用共享物件，用来尽可能减少内存使用量以及分享资讯给尽可能多的相似物件；它适合用于当大量物件只是重复因而导致无法令人接受的使用大量内存。
