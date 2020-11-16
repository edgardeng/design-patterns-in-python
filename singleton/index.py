import functools


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# use metaclass
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass  # TODO Finally, some business logic executed on its single instance.


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.obj:
            wrapper.obj = cls(*args, **kwargs)
        return wrapper.obj

    wrapper.obj = None
    return wrapper


# use decorator
@singleton
class Singleton2():
    def some_business_logic(self):
        pass  # TODO Finally, some business logic executed on its single instance.


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    s3 = Singleton2()
    s4 = Singleton2()

    if id(s3) == id(s4):
        print("Singleton with decorator works, both variables contain the same instance.")
    else:
        print("Singleton with decorator failed, variables contain different instances.")
