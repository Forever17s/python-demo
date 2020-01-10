# encoding:utf-8
"""
author: wgc
version: 1.4
title: Python语言进阶
"""

import threading

# 混入 Mixin
# 例子：自定义字典限制只有在指定的 key 不存在时才能在字典中设置键值对

# class SetOnceMappingMixin:
#     # 自定义混入类
#     __solts__ = ()

#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + ' already set')
#         return super().__setitem__(key, value)

# class SetOnceDict(SetOnceMappingMixin, dict):
#     # 自定义字典
#     pass

# my_dict = SetOnceDict()
# try:
#     my_dict['username'] = 'jack'
#     my_dict['username'] = 'hello'
# except KeyError:
#     pass
# print(my_dict)

# 元编程和元类
# 例子：用元类实现单例模式
# class SingletonMeta(type):
# 	# 自定义元类

# 	def __init__(cls, *args, **kwargs):
# 		cls._instance = None
# 		cls._lock = threading.Lock()
# 		super().__init__(*args, **kwargs)

# 	def __call__(cls, *args, **kwargs):
# 		if cls._instance is None:
# 			with cls._lock:
# 				if cls._instance is None:
# 					cls._instance = super().__call__(*args, **kwargs)

# 		return cls._instance

# class President(metaclass = SingletonMeta):
# 	# 总统（单例类）
# 	pass
"""
面向对象设计原则
    单一职责原则：一个类只做该做的事情（类的设计要高内聚）
    开闭原则：软件实体应该对扩展开发对修改关闭
    依赖倒转原则：面向抽象编程（在弱类型语言中已经被弱化）
    里氏替换原则：任何时候可以用子类对象替换父类对象
    接口隔离原则：接口要小而专不要大而专（Python中没有接口的概念）
    合成聚合复用原则：优先使用强关联关系而不是继承关系复用代码
    最少知识原则：不要给没有必要联系的对象发消息
"""
"""
GoF设计模式
    创建型模式：单例、工厂、建造者、原型
    结构性模式：适配器、外观、代理
    行为型模式：迭代器、观察者、状态、策略
"""


# 例子：可插拔的哈希算法
class StreamHasher():
    # 哈希摘要生成器（策略模式）
    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        # 生成十六进制形式的摘要
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)

        return self.hasher.hexdigest()


def main():
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')

    with open('./tests/b.txt', 'rb') as stream:
        print(hasher1.to_digest(stream))

    with open('./tests/c.txt', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()
