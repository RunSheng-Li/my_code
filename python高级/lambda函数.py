# lambda的简单例子
g = lambda x: x + 1
print(g(1))
print(g(2))


# 可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体，用函数来表示为
def g(x):
    return x + 1
# lambda简化了函数定义的书写形式,使代码更为简洁