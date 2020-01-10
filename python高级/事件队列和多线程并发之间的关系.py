import queue
import threading
import time
import random


def Producer(name, que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            print(f'{name}做了一个包子')
        else:
            print('还有三个包子')
        time.sleep(random.randrange(3))


def Consumer(name, que):
    while True:
        try:
            que.get_nowait()
            print(f'{name}拿到一个包子')
        except Exception:
            print('没有包子了')
        time.sleep(random.randrange(2))


# 线程间通信
q = queue.Queue()
p1 = threading.Thread(target=Producer, args=['chef1', q])
p2 = threading.Thread(target=Producer, args=['chef2', q])
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer, args=['大明', q])
c2 = threading.Thread(target=Consumer, args=['小红', q])
c1.start()
c2.start()

# 多线程可以独立运行，事件队列是线程之间传递信息的一种方式
# 使用事件队列在线程之间传递信息的好处是并发(高效率)和解耦
