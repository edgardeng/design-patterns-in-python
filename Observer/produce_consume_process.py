from multiprocessing import Queue, Process


# 使用Process + Queue 实现生产/消费模式


def produce(q: Queue, name):
    for i in range(10):
        print('produce:    ', i)
        q.put('produce_%d' % i)
        # c.send(str(i))
    q.put(None)


def consume(q: Queue, name):
    while True:
        product = q.get()
        if product:
            print('consume %s' % product)
        else:
            break


if __name__ == '__main__':
    q = Queue(10)
    producer = Process(target=produce, args=(q, '生产'))
    consumer = Process(target=consume, args=(q, '消费'))
    producer.start()
    consumer.start()
