# 引入装饰器
def w1(func):
    def inner():
        print('验证权限')
        func()

    return inner


@w1
def f1():
    print('f1函数被调用')


@w1
def f2():
    print('f2函数被调用')


# f1()
# f2()

# ------------------------------------------------------------------------------
# 装饰器的执行时机
def w1(func):
    print('装饰器开始装饰')

    def inner():
        print('验证权限')
        func()

    return inner


@w1
def test():
    print('test函数被调用')


# test()
"""
装饰器开始装饰
验证权限
test函数被调用
"""


# 由此可以发现，当python解释器执行到@w1时，就开始进行装饰了

# ------------------------------------------------------------------------------
# 两个装饰器执行流程和装饰结果

def w1(func):
    print("进入w1装饰器")

    def inner():
        print("进入w1的inner")
        func()

    return inner


def w2(func):
    print("进入w2装饰器")

    def inner():
        print("进入w2的inner")
        func()

    return inner


@w1
@w2
def test():
    print("test")


# test()
"""
进入w2装饰器
进入w1装饰器
进入w1的inner
进入w2的inner
test
"""


# 可以发现，先用第二个装饰器(w2)进行装饰，接着再用第一个装饰器(w1)进行装饰，而在调用过程中，先执行第一个装饰器(w1)，接着再执行第二个装饰器(w2)。

# ------------------------------------------------------------------------------
# 对有参数函数进行装饰

def w_hello(func):
    """
    如果原函数有参数，那闭包必须保持参数个数一致，并且将参数传递给原方法
    """
    def inner(name):
        """
        如果被装饰的函数有形参，那么闭包函数必须有参数
        """
        print("w_hello inner")
        func(name)
    return inner

@w_hello
def hello(name):
    print(f"hello,{name}")

hello("sam")
