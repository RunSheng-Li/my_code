# 可迭代对象
# 如果对象实现了能返回迭代器的__iter__方法，那么对象就是可迭代的
# 序列都可以迭代的
# 实现了__getitem__方法，而且其参数是从零开始的索引，这种对象也可以迭代
class Foo:
    def __iter__(self):
        pass


from collections import abc

f = Foo()
print(isinstance(f, abc.Iterable))

# ------------------------------------------------------------------------------
# 迭代器
# 标准的迭代器接口有两个方法
# __next__ 返回下一个可用的元素，如果没有元素，则抛出StopIteration异常
# __iter__ 返回self，以便在应该使用可迭代对象的地方使用迭代器，例如在for循环中

s = 'ABC'

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
