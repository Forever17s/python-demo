# encoding:utf-8
"""
author: wgc
version: 1.3
title: Python语言进阶
"""

from enum import Enum, unique
import random
"""
类与类之间的关系
  is-a ：继承
  has-a ：关联、聚合、合成
  use-a ： 依赖
"""

# 例子：扑克牌游戏
"""
经验：符号常量总司优于字面常量，枚举类型是定义符号常量的最佳选择
"""

# @unique
# class Suite(Enum):
#     # 花色
#     SPADE, HEART, CLUB, DIAMOND = range(4)

#     def __lt__(self, other):
#         return self.value < other.value

# class Card():
#     # 牌

#     def __init__(self, suite, face):
#         self.suite = suite
#         self.face = face

#     def show(self):
#         """显示牌面"""

#         suites = ['♠️', '♥️', '♣️', '♦️']
#         faces = [
#             '', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
#             'K'
#         ]
#         return f'{suites[self.suite.value]} {faces[self.face]}'

#     def __str__(self):
#         return self.show()

#     def __repr__(self):
#         return self.show()

# class Poker():
#     # 扑克

#     def __init__(self):
#         self.index = 0
#         self.cards = [
#             Card(suite, face) for suite in Suite for face in range(1, 14)
#         ]

#     def shuffle(self):
#         # 洗牌
#         random.shuffle(self.cards)
#         self.index = 0

#     def deal(self):
#         # 发牌
#         card = self.cards[self.index]
#         self.index += 1
#         return card

#     @property
#     def has_more(self):
#         return self.index < len(self.cards)

# class Player():
#     # 玩家
#     def __init__(self, name):
#         self.name = name
#         self.cards = []

#     def get_one(self, card):
#         # 摸一张牌
#         self.cards.append(card)

#     def sort(self, comp=lambda card: (card.suite, card.face)):
#         # 整理手上的牌
#         self.cards.sort(key=comp)

# def main():
#     poker = Poker()
#     poker.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

#     while poker.has_more:
#         for player in players:
#             player.get_one(poker.deal())

#     for player in players:
#         player.sort()
#         print(player.name, end='：')
#         print(player.cards)

# if __name__ == '__main__':
#     main()

# 对象的复制（深拷贝、浅拷贝、影子克隆？）
# 垃圾回收、循环引用和弱引用
"""
Python 使用了自动化内存管理，
这种管理机制以引用计数为基础，
同时也引入了标记-清除和分代收集两种机制为辅的策略
"""
"""
typedef struct_object {
    # 引用计数
    int ob_refcnt;
    # 对象指针
    struct_typeobject *ob_type;
} PyObject;
"""
"""
/* 增加引用计数的宏定义 */
#define Py_INCREF(op)   ((op)->ob_refcnt++)
/* 减少引用计数的宏定义 */
#define Py_DECREF(op) \ //减少计数
    if (--(op)->ob_refcnt != 0) \
        ; \
    else \
        __Py_Dealloc((PyObject *)(op))
"""
"""
导致引用计数 +1 的情况：
    对象被创建，例如 a = 23
    对象被引用，例如 b = a
    对象被作为参数，传入到一个函数中，例如 f(a)
    对象作为一个元素，存储在容器中，例如 list1 = [a, a]

导致引用计数 -1 的情况：
    对象的别名被显式销毁，例如 del a
    对象的别名被赋予新的对象，例如 a = 24
    一个对象离开它的作用域，例如 f 函数执行完毕时，f 函数中的变量（全局变量不会）
    对象所在的容器被销毁，或从容器中删除对象

引用计数可能会导致循环引用问题，而循环引用会导致内存泄漏，如下面代码所示。
为了解决这个问题，Python中引入【标记-清除】和【分代收集】。
在创建一个对象的时候，对象被放到第一代中，如果在第一代的垃圾检测中对象存活下来了，
该对象就会被放到第二代中，同理在第二代的垃圾检查中对象存活下来，该对象就会被放到第三代中
"""

# 循环引用会导致内存泄漏 Python除了引用计数还引用了标记清理和分代回收
# 在 Python 3.6 以前如果重写 __del__ 魔术方法会导致循环引用处理失效
# 如果不想造成循环引用可以使用弱引用
list1 = []
list2 = []
list1.append(list2)
list2.append(list1)
"""
以下情况会导致垃圾回收：
    调用 gc.collect()
    gc 模块的计数器达到阈值
    程序退出

如果循环引用中两个对象都定义了 __del__ 方法，gc 模块不会销毁这些不可达对象，
因为 gc 模块不知道应该先调用哪个对象的 __del__ 方法，这个问题在 Python 3.6 中得到了解决

也可以通过 weakref 模块构造弱引用的方式来解决循环引用的问题

魔法属性和方法（请参考《Python魔法方法指南》）
"""
