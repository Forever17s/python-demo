# encoding:utf-8
"""
author: wgc
version: 0.1
"""
# import math
# import random

#  hi WGC!
# print('hello, world!')

# a = 321
# b = "123"
# c = False
# d = 12.3
# e = 1 + 5
# f = 2j + 3
# g = 'undefined'
# h = 'null'
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d ** %d = %d' % (a, b, a ** b))

# f = float(input('请输入华氏度： '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# radius = float(input('请输入圆的半径： '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长： %.2f' % perimeter)
# print('面积： %.2f' % area)

# # 闰年输出True,否则False
# year = int(input('set a year: '))
# # 如果代码太长不易阅读 可以使用\对代码进行折行
# is_leap = (year % 4 == 0 and year % 100 != 0) \
#   or \
#   (year % 400 == 0)
# print(is_leap)
# """
# 分段函数求值
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
# """
# 方案一
# x = float(input('x = '))
# if x > 1:
#     print(3 * x - 5)
# else:
#     if x > -1:
#         print(x + 2)
#     else:
#         print(5 * x + 3)

# # 方案二
# x = float(input('x = '))
# if x > 1:
#     print(3 * x - 5)
# elif x < -1:
#     print(5 * x + 3)
# else:
#     print(x + 2)
"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
"""

# sum = 0
# for x in range(100):
#     sum += x
# print(sum)

# sum = 0
# for x in range(0, 100):
#     sum += x
# print(sum)

# sum = 0
# for x in range(0, 100, 2):
#     sum += x
# print(sum)

# sum = 0
# for x in range(0, 100):
#     if x % 3 == 0:
#         sum += x
# print(sum)
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# answer = random.randint(0, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('数字0~100，请猜数：'))
#     if number > answer:
#         print('猜大了')
#     elif number < answer:
#         print('猜小了')
#     else:
#         print('㊗️正确！')
#         break
# print('总共猜了%d次' % counter)
# if counter > 7:
#     print('猜次数有点多哈！')

# # 输出乘法口诀表(九九表)
# for i in range(0, 10):
#     for j in range(0, i + 1):
#         print('%d * %d = %d' % (i, j, i * j), end='\t')
#     print()

# # 输入两个正整数计算它们的最大公约数和最小公倍数
# x = int(input('x = :'))
# y = int(input('y = :'))
# # 如果x大于y，就给x,y换位置
# if x > y:
#     X, Y = y, x
# else:
#     X, Y = x, y
# # 从两个数中较小数进行递减循环
# for i in range(X, 0, -1):
#     if X % i == 0 and Y % i == 0:
#         print("%d 和 %d最大公约数为：%d" % (x, y, i))
#         print("%d 和 %d最小公倍数为：%d" % (x, y, x * y // i))
#         break

# # 打印正三角
# num = int(input('输入正三角形边长：'))
# for i in range(num):
#     for _ in range(num - i):
#         print(" ", end='')
#     for _ in range(2 * i + 1):
#         print("*", end='')
#     print()

# # 正整数的反转
# num = int(input('num = '))
# reverse_num = 0
# while num > 0:
#     reverse_num = reverse_num * 10 + num % 10
#     num //= 10
# print(reverse_num)

# num1 = 123456
# num1 //= 10
# print(num1)

# num2 = 123456
# num2 /= 10
# print(num2)

# # 定义函数
# def factorial(num):
#     """
#             N
#     求阶乘 C
#             M
#         M! / N!(M - N)!
#     """
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result

# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m - n))

# def test(args=2):
#     print(args)

# def testMul(*args):
#     print(args)

# test()
# test(3)
# testMul(1, 2, 3)

# def foo():
#     print('hello, world!')

# def foo():
#     print('goodbye, world!')

# # 下面的代码会输出什么呢？
# foo()

# # 变量作用域
# def foo():
#     b = 'hello'

#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)

#     bar()

# if __name__ == '__main__':
#     a = 100
#     # print(b)
#     foo()

# # 通过函数调用修改全局变量a的值，但实际上下面的代码是做不到的。
# def foo():
#     a = 2000
#     print(a)  # 2000

# if __name__ == "__main__":
#     a = 100
#     foo()
#     print(a)  # 100
"""
在函数foo中写a = 2000的时候，
是重新定义了一个名字为a的局部变量，
它跟全局作用域的a并不是同一个变量，
因为局部作用域中有了自己的变量a，
因此foo函数不再搜索全局作用域中的a。
"""

# def foo():
#     global a
#     a = 2000
#     print(a)  # 2000

# if __name__ == "__main__":
#     a = 100
#     foo()
#     print(a)  # 2000
"""
与global关键字相对应的关键字为 nonlocal
"""
