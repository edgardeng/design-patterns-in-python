import datetime
import functools


class CallRecord:
    CALL_INFO = {}

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        CallRecord.CALL_INFO[self.func.__name__] = str(datetime.datetime.now())
        print(CallRecord.CALL_INFO)
        return self.func(*args, **kwargs)


@CallRecord
def foo():
    print(sum([1, 2, 3, 4, 5]))


class T:
    @CallRecord
    def plus(self, a, b):
        print(a + b)


@CallRecord
class T2:
    def plus(self, a, b):
        print(a + b)


if __name__ == '__main__':
    foo()
    # T().plus(1, 2) # self 参数接收的是 CallRecord 实例，并不会像 m(self, a, b) 方法那样接收 T 实例，并且 T 实例也不会被包含在 __call__() 方法的 args 变长参数中
    T2().plus(1, 2)
