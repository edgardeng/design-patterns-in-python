"""
 单例模式 代码实例
 Singleton Factory Code Demo
"""

from threading import Lock


class Singleton(object):
    _instance_lock = Lock()
    _instance = None
    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not Singleton._instance:
            with Singleton._instance_lock:
                Singleton._instance = super().__new__(cls)
        return Singleton._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

