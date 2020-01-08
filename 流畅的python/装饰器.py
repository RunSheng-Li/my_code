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


# ------------------------------------------------------------------------------
# 如果是多个或者不定长参数，要怎么处理

def w(func):
    def inner(*args, **kwargs):
        print("w inner")
        func(*args, **kwargs)

    return inner


@w
def print1(a, b):
    print(f"参数是{a},{b}")


@w
def print2(a, b, c):
    print(f"参数是{a},{b},{c}")


print1(1, 2)
print2(1, 2, 3)


# ------------------------------------------------------------------------------
# 对带有返回值的函数进行装饰

def w(func):
    def inner():
        print("w inner 开始")
        func()
        print("w inner 结束")

    return inner


@w
def test():
    print("test函数被调用")
    return "test"


res = test()
print(f"res,{res}")  # res,None


# 这是因为在inner函数中对test进行了调用，但是没有接受不了返回值，也没有进行返回，那么默认就是None了
# 那么对上面的代码进行修改
def w(func):
    def inner():
        print("w inner 开始")
        str = func()
        print("w inner 结束")
        return str

    return inner


@w
def test():
    print("test函数被调用")
    return "test"


res = test()
print(f"res,{res}")  # res,test


# 这样就达到预期，完成对带返回值参数的函数进行装饰。

# ------------------------------------------------------------------------------
# 带参数的装饰器

def w(pre="sam"):
    def outter(func):
        def inner():
            print(f"我的参数是{pre}")
            func()

        return inner

    return outter


@w('haha')
def test():
    print("test")


test()


# ------------------------------------------------------------------------------
# 通用装饰器

def w(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return inner


@w
def test():
    print("这是test函数")


test()

# ------------------------------------------------------------------------------
# 类装饰器

class Test():
    def __init__(self,func):
        print('test init')
        print(f"func name is {func.__name__}")
        self._func = func
    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self._func()

@Test
def test():
    print('test')

test()

# ------------------------------------------------------------------------------
