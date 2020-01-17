# 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。 在鸭子类型中，关注点在于对象的行为，能作什么；而不是关注对象所属的类型
# 在鸭子类型中，关注点在于对象的行为，能作什么；而不是关注对象所属的类型
# 我们可以使用一个函数 makeRun() 来访问不同 Animal 子类中的相同方法。但其实对于上面的 makeRun() 函数来说，传入的参数并不一定需要是 Animal 类型的，只需要保证传入的对象有一个 run() 方法即可
# 而在静态语言中，如 Java ，如果需要传入 Animal 类型，则传入的对象就必须是 Animal 类型或者它的子类，否则，将无法调用 run() 方法。
class Animal():

    def run(self):
        print('The animal is running...')


class Dog(Animal):

    def run(self):
        print('The dog is running...')


class Cat(Animal):

    def run(self):
        print('The cat is running...')


class Person():

    def run(self):
        print('The Person is running...')


def makeRun(animalType):
    animalType.run()


dog = Dog()
cat = Cat()
person = Person()

makeRun(dog)
makeRun(cat)
makeRun(person)
