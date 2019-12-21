# encoding:utf-8
"""
author: wgc
version: 0.3
"""

# from math import sqrt
# from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod

# # 定义类
# class Student(object):
#     # __init__是一个特殊方法用于创建对象时进行初始化操作
#     # 通过这个方法我们可以为 Student 类对象绑定name 和 age两个属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course):
#         print(f'{self.name} 正在学习{course}')

#     # PEP 8要求标识符的名字用全小写多个单词用下划线链接
#     # 但是部分程序猿和公司更倾向于使用驼峰命名法
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s 只能观看《熊出没》。' % self.name)
#         else:
#             print('%s 正在观看岛国爱情大电影。' % self.name)

# def main():
#     # 创建对象
#     stu1 = Student('test', 32)
#     stu1.study('python')
#     stu1.watch_movie()

#     stu2 = Student('test2', 12)
#     stu2.study('荷塘月色')
#     stu2.watch_movie()

# if __name__ == '__main__':
#     main()
"""
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，
下面的代码可以验证这一点。
"""

# class Test:
#     def __init__(self, foo):
#         self.foo = foo

#     def __bar(self):
#         print(self.foo)

# def main():
#     test1 = Test("hello")
#     # test1.__bar() # 'Test' object has no attribute '__bar'
#     print(test1.foo)

# if __name__ == "__main__":
#     main()
"""
但是，Python并没有从语法上严格保证私有属性或方法的私密性，
它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
实上如果你知道更换名字的规则仍然可以访问到它们，下面的代码就可以验证这一点。
之所以这样设定，可以用这样一句名言加以解释，就是"We are all consenting adults here"。
因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。
"""

# class Test:
#     def __init__(self, foo):
#         self.__foo = foo

#     def __bar(self):
#         print(self.__foo)

# def main():
#     test2 = Test("hello")
#     test2._Test__bar()
#     print(test2._Test__foo)

# if __name__ == "__main__":
#     main()
"""
在实际开发中，我们并不建议将属性设置为私有的，
因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
本类之外的代码在访问这样的属性时应该要保持慎重。
"""
"""
虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，
代码如下所示。
"""

# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#         # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age

#     # 修改器 - setter方法
#     @age.setter
#     def age(self, value):
#         self._age = value

# def main():
#     person = Person('test', 25)
#     print(person.age)
#     person.age = 22
#     print(person.name)
#     # person.name = 'test222'  # can't set attribute

# if __name__ == '__main__':
#     main()
"""
Python是一门动态语言。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
"""

# class Person(object):

#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)

# def main():
#     person = Person('王大锤', 22)
#     person.play()
#     person._gender = '男'
#     # AttributeError: 'Person' object has no attribute '_is_gay'
#     # person._is_gay = True

# if __name__ == '__main__':
#     main()
"""
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，
但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，
这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），
所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，
代码如下所示。
"""

# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     def perimeter(self):
#         return self._a + self._b + self._c

#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * (half - self._b) *
#                     (half - self._c))

# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#     else:
#         print('无法构成三角形.')

# if __name__ == '__main__':
#     main()
"""
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
"""

# class Clock(object):
#     """数字时钟"""
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)

# def main():
#     # 通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == '__main__':
#     main()
"""继承和多态"""

# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         self._age = value

#     def play(self):
#         print('%s正在愉快的玩耍。' % self._name)

#     def watch_movie(self):
#         if self._age >= 18:
#             print('%s正在看爱情动作片。' % self._name)
#         else:
#             print('%s只能看《熊出没》。' % self._name)

# class Student(Person):
#     """学生"""
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade

#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, value):
#         self._grade = value

#     def study(self, course):
#         print('%s%s正在学习%s.' % (self._grade, self._name, course))

# class Teacher(Person):
#     """老师"""
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, title):
#         self._title = title

#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))

# def main():
#     stu = Student('王学生', 15, '初三')
#     stu.study('math')
#     stu.watch_movie()

#     teacher = Teacher('李老师', 52, '专家')
#     teacher.teach('python')
#     teacher.watch_movie()

# if __name__ == '__main__':
#     main()


# 多态
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickName):
        self._nickName = nickName

    @abstractmethod
    def make_voice(self):
        """发出声响"""
        pass


class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickName)


class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickName)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
"""
在上面的代码中，我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
上面的代码中，Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，当我们在main函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。
"""
