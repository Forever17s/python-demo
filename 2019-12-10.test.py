# encoding:utf-8
"""
author: wgc
version: 0.2
"""

# import sys
# import os
# import time

# s1 = """
#   123333
#     333
#   """
# s2 = '""'
# s3 = 'hello'
# s4 = "hello"
# print(s1, s2, s3, s4, end='')

# s1 = '\'hello,world!\''
# s2 = '\n\\hello,world!\\\n'
# print(s1, s2, end='')

# s1 = r'\'hello,world!\''
# s2 = r'\n\\hello,world\\\n'
# print(s1, s2, end='')

# s1 = 'hello ' * 3
# print(s1)
# s2 = 'world'
# s1 += s2
# print(s1)  # hello hello hello world
# print('ll' in s1)
# print('good' in s1)
# str2 = 'abc1234567'
# # 从字符串中取出指定位置的字符（下标）
# print(str2[2])  # c
# # 字符串切片（从指定的开始索引到指定的结束索引）
# print(str2[2:5])  # c12
# print(str2[2:])  # c1234567
# print(str2[2::2])  # c256
# print(str2[::2])  # ac246
# print(str2[::-1])  # 7654321cba
# print(str2[-3:-1])  # 56
# print(str2[-3::-1]) # 54321cba

# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1))  # 13
# # 获得字符串首字母大写的拷贝
# print(str1.capitalize())  # Hello, world!
# # 获得字符串每个单词首字母大写的拷贝
# print(str1.title())  # Hello, World!
# # 获得字符串变大写后的拷贝
# print(str1.upper())  # HELLO, WORLD!
# # 从字符串中查找子串所在位置
# print(str1.find('or'))  # 8
# print(str1.find('shit'))  # -1
# # 与find类似但找不到子串时会引发异常
# # print(str1.index('or'))
# # print(str1.index('shit'))
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He'))  # False
# print(str1.startswith('hel'))  # True
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!'))  # True
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())

# # 之前讲过，可以用下面的方式来格式化输出字符串。
# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
# # 当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。
# print('{0}*{1}={2}'.format(a, b, a * b))
# # Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母f,类似ES6的模板函数
# print(f'{a} * {b} = {a * b}')

# # 集合
# arr1 = [1, 2, 3, 7, 100]
# print(arr1)
# # 乘号表示集合元素的重复
# arr2 = ['hello'] * 3
# print(arr2)
# # 计算数组长度
# print(len(arr1))  # 5
# # 下标（索引）运算
# print(arr1[0])
# print(arr1[4])
# # print(arr1[5])  # ERROR
# print(arr1[-1])
# print(arr1[-3])
# arr2[2] = 'test'
# print(arr2)
# # 通过循环用下标遍历数组
# for index in range(len(arr1)):
#     print(arr1[index])
# # 通过for循环遍历数组元素
# for item in arr2:
#     print(item)
# # 通过 enumerate 函数处理数组后再遍历可以同时获取元素索引和值
# for index, item in enumerate(arr1):
#     print(f'第{index+1}个元素为：{item}')

# # 向数组中添加和移除元素
# arr3 = [1, 3, 5, 7, 100]
# # 添加元素
# arr3.append(200)
# arr3.insert(1, 400)
# print(arr3)
# # 合并两个数组
# arr3.extend([1000, 2000])
# arr3 += [6666, 8888]
# print(arr3)
# # 删除，先通过成员运算判断元素是否在数组中，如果存在就删除
# if 3 in arr3:
#     arr3.remove(3)
# if 1234 in arr3:
#     arr3.remove(1234)
# print(arr3)
# # 从指定位置删除元素
# arr3.pop(0)
# arr3.pop(len(arr3) - 1)
# print(arr3)
# # 清空数组
# arr3.clear()
# print(arr3)

# # 数组排序
# arr4 = [
#     'orange', 'apple', 'zoo', "测试-2019年12月11日18:35:14", '哈哈-(¦3[▓▓] 晚安',
#     'internationalization', '测试-2019-12-11 18:35:32', 'blueberry'
# ]
# arr5 = sorted(arr4)
# print(arr5)
# """
# sorted函数返回后的数组修改后不影响母数组
# 函数的设计就应该像sorted一样尽可能不产生副作用
# """
# arr6 = sorted(arr4, reverse=True)
# print(arr6)
# arr7 = sorted(arr4, key=len)
# print(arr7)
# # 直接对数组本身进行排序
# arr7.sort(reverse=True)
# print(arr7)

# # 使用数组的生成式语法来创建数组
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
"""
用数组的生成表达式语法创建数组容器
用这种语法创建数组之后元素以及准备就绪所以需要耗费较多的内存空间
"""

# f = [x**2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# # print(f)

# f = (x**2 for x in range(1, 1000))
# print(sys.getsizeof(f))  # 相比生成器不占用存储数据的空间
"""
除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，
就是通过yield关键字将一个普通函数改造成生成器函数。
下面的代码演示了如何实现一个生成斐波拉切数列的生成器
"""

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a

# def main():
#     for val in fib(10):
#         print(val)

# if __name__ == '__main__':
#     main()
"""
Python中的元组与数组类似也是一种容器数据类型，
可以用一个变量（对象）来存储多个数据，
不同之处在于元组的元素不能修改
"""
# # 定义元组
# t = ('张小二', 38, True, '四川成都')
# print(t)
# # 获取元组中的元素
# print(t[0])
# print(t[3])
# # 遍历元组中的值
# for member in t:
#     print(member)
# # 重新给元组赋值
# # t[0] = '王大锤'  # TypeError
# # 变量t重新引用了新的元组原来的元组将被垃圾回收
# t = ('王大锤', 20, True, '云南昆明')
# print(t)
# # 将元组转换成数组
# person = list(t)
# print(person)
# # 作为数组是可以修改元素的
# person[0] = '李小龙'
# person[1] = '25'
# print(person)
# # 将数组转化为元组
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)
"""
有数组这种数据结构，为什么还需要元组
1.元组中的元素无法修改，安全、容易维护
2.元组在创建时间和占用空间上都优于数组
"""

# 使用集合
# # 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print(f'Length = {len(set1)}')
# # 创建集合的构造器语法
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 3, 2))
# print(set2, set3)
# # 创建集合的推导式语法
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)

# # 向集合添加元素和从集合删除元素
# set1 = {1, 2, 3, 3}
# set2 = {1, 2, 3, 3}
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# print(set1) # {1, 2, 3, 4, 5}
# print(set2) # {1, 2, 3, 11, 12}
# if 4 in set1:
#     set1.remove(4)
# print(set1) # {1, 2, 3, 5}
# print(set2.pop()) # 1
# print(set2) # {2, 3, 11, 12}

# # 集合的成员、交集、并集、差集等运算。
# set1 = {1, 2, 4, 5}
# set2 = {1, 2, 3}
# set3 = {2}
# print(set1 & set2)
# # print(set1.intersection(set2))
# print(set1 | set2)
# # print(set1.union(set2))
# print(set1 - set2)
# # print(set1.difference(set2))
# print(set1 ^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))

# # 创建字典的字面量语法
# scores = {'a': 95, "b": '78', "c": 12}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3)
# print(items1)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '1234'))
# print(items2)
# items2 = dict(zip(['a', 'b', 'c'], '12'))
# print(items2)
# # 创建字典的的推导式语法
# items3 = {num: num**2 for num in range(1, 10)}
# print(items3)
# # 通过键可以获取字典中对应的值
# print(items2['a'])
# print(items3[3])
# # 对字典中所有键值对进行遍历
# for key in items2:
#     print(f'{key}: {items2[key]}')
# # 更新字典中的元素
# scores['a'] = 100.0
# scores['c'] = 60.0
# scores.update(a=100.0, c=60.0, d=25.0)
# print(scores)
# # 获取元素
# print(scores["c"])
# print(scores.get("c"))
# # 删除元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('a', 100.0))
# # 清空字典
# scores.clear()
# print(scores)

# # 跑马灯
# def main():
#     content = "2019年12月12日14:52:42"
#     while True:
#         # 清理屏幕上的输出
#         os.system('clear')
#         print(content)
#         # 睡眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == "__main__":
#     main()
