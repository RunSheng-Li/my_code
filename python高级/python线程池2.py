import time
from multiprocessing.pool import ThreadPool

pool = ThreadPool(5)  # 直接使用内置线程池, 设置最大线程数


def run():
    time.sleep(1)
    print("我在跑步")


def sing(*args, **kwargs):
    time.sleep(1)
    print("我在唱歌", args, kwargs)


def play(a, b):
    time.sleep(3)
    print(a, b)


def play2(c):
    print(c / 0)


# pool.apply_async(run)
# pool.apply_async(run)
# pool.apply_async(run)
# pool.apply_async(sing, args=(1, 2), kwds={'a': 1, 'b': 2})

# pool.apply_async(play,args=(1,2))
# pool.apply_async(play2, args=("aaa"))
# pool.close()
# pool.join()
# print("hahaha")

try:
    pool.apply_async(play2, args=(1,))
    pool.close()
    pool.join()

except Exception as e:
    print(e)
