
# 使用send + yield 实现生产/消费模式

def produce(c):
    for i in range(10):
        print('produce:    ', i)
        c.send(str(i))


def consume():
    while True:
        res = yield
        print('consume:    ', res)


if __name__ == '__main__':

    c = consume()
    next(c)  # 先跑到 yield 那一步
    produce(c)
