import abc

# 同一类事物：动物
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

# 动物形态之一：人
class People(Animal):
    def talk(self):
        print('我是一个人')

# 动物形态之一：狗
class Dog(Animal):
    def talk(self):
        print('我是一只狗')

# 动物形态之一:猪
class Pig(Animal):
    def talk(self):
        print('我是一只猪')

p = People()
d = Dog()
pig = Pig()


# peo、dog、pig都是动物,只要是动物肯定有talk方法
# 于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
p.talk()
d.talk()
pig.talk()

# 更进一步,我们可以定义一个统一的接口来使用
def func(obj):
    obj.talk()

# func(p)

"""
使用多态的好处：
1.增加了程序的灵活性

　　以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如func(animal)

2.增加了程序额可扩展性

　　通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用func(animal)去调用


"""


