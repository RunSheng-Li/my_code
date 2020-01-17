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


