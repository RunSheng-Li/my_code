from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(2)  # 直接使用内置线程池, 设置最大线程数


def task1():
    time.sleep(2)
    print('task1 over')


def task2(*args, **kwargs):
    time.sleep(3)
    print('task2 over', args, kwargs)


try:
    pool.apply_async(task1)
    pool.apply_async(task2, args=(1, 2), kwds={'a': 1, 'b': 2})
    print('Task Submitted')
    pool.close()  # 要点: close必须要在join之前, 不允许再提交任务了
    pool.join()
    print('Mission Complete')
except Exception as e:
    print(e)
