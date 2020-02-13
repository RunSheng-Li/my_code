import time
import sys
def w(func):
    def inner(*args, **kwargs):
        time1 = time.time()
        res = func(*args, **kwargs)
        time2 = time.time()
        print(time1)
        return res

    return inner


@w
def test():
    print("test")\

if __name__ == '__main__':

    test()