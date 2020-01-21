# yield
# ------------------------------------------------------------------------------
def gen():
    n = 0
    while True:
        yield n
        n += 1


g = gen()


# print(g)
# print(next(g))
# print(next(g))

# send
# ------------------------------------------------------------------------------

# 生成器函数可以不断的产出值给调用方，那如果想要调用方传递值给生成器函数呢？

def gen():
    s = yield 'hello'
    print(f'用户传进来的值为{s}')
    yield s


g = gen()
# print(next(g))
# print(g.send('world'))

# yield from
# ------------------------------------------------------------------------------
def func():
    for x in "ABC":
        yield x

for x in func():
    # print(x)
    pass

# 上面写法等同于
def func():
    yield from "ABC"

for x in func():
    # print(x)
    pass


# gevent
# ------------------------------------------------------------------------------
import gevent


def func1():
    print("func1 running")
    gevent.sleep(2)  # 内部函数实现io操作
    print("switch func1")


def func2():
    print("func2 running")
    gevent.sleep(1)
    print("switch func2")


def func3():
    print("func3  running")
    gevent.sleep(0.5)
    print("func3 done..")

gevent.joinall([gevent.spawn(func1),
                gevent.spawn(func2),
                gevent.spawn(func3),
                ])




