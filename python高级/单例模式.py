# 使用装饰器实现单例
# ------------------------------------------------------------------------------
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class Cls():
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


# 使用类装饰器实现单例
# ------------------------------------------------------------------------------
class Singleton():
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2():
    def __init__(self):
        pass


cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))


# 使用new关键字实现单例模式
# ------------------------------------------------------------------------------

class Stu():
    # 类属性
    # 保证对象唯一
    __single = None
    # 保证初始化唯一
    __firstinit = False

    # 控制对象唯一
    def __new__(cls, *args, **kwargs):
        # 如果__single 没有值，给__single进行赋值
        if not cls.__single:
            cls.__single = super().__new__(cls)
        # 直接返回对象值

    # 控制只初始化一次
    def __init__(self, name, age):
        # 首次根据标签的值进行初始化操作
        if not Stu.__firstinit:
            self.name = name
            self.age = age
            # 修改标签的值
            Stu.__firstinit = True


# 创建对象
a = Stu('a', 1)
b = Stu('b', 2)
c = Stu('c', 3)

print(id(a))
print(id(b))
print(id(c))
