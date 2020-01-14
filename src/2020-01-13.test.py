# encoding:utf-8
"""
author: wgc
version: 1.5
title: Python语言进阶
"""

import glob
import os
import threading
import time
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep
"""
迭代器和生成器
  和迭代器相关的魔术方法（ __iter__ 和 __next__ ）
  两种创建生成器的方式（生成器表达式和 yield 关键字）
"""

# def fib(num):
#     a, b = 0, 1
#     for _ in range(num):
#         print(a, b)
#         a, b = b, a + b
#         yield a

# class Fib(object):
#     # 迭代器

#     def __init__(self, num):
#         self.num = num
#         self.a, self.b = 0, 1
#         self.idx = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.idx < self.num:
#             self.a, self.b = self.b, self.a + self.b
#             self.idx += 1
#             return self.a

#         raise StopIteration()

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)

# def testYield():
#     g = foo()
#     print(next(g))
#     print("*" * 20)
#     print(next(g))

# def main():
#     # testYield()

#     for i in fib(8):
#         print(i)
"""
并发编程
    Python 中实现并发编程的三种方案：多线程、多进程和异步I/O
    并发编程的好处在于可以提升程序的执行效率以及改善用户体验；
    坏处在于并发的程序并不容易开发和调试，同时对其他程序来说它不友好
"""
"""
多线程：

Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier
Python中有GIL来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的
因为CPython的内存管理并不是线程安全的，因为GIL的存在多线程并不能发挥CPU的多核特性
"""
"""
知识点：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位。一个进程可以包含一个或多个线程
线程 - 操作系统分配cpu的基本单位

并发编程 concurrent programming
1.提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2.改善用户体验 - 让耗时间的操作不会造成程序的假死
"""

# PREFIX = './tests/thumbnails'

# def generate_thumbnail(infile, size, format='PNG'):
#     # 生成指定图片文件的缩略图
#     file, ext = os.path.splitext(infile)
#     file = file[file.rfind('/') + 1:]
#     outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'

#     img = Image.open(infile)
#     img.thumbnail(size, Image.ANTIALIAS)
#     img.save(outfile, format=format)

# def main():
#     if not os.path.exists(PREFIX):
#         os.mkdir(PREFIX)

#     for infile in glob.glob('./tests/images/*.png'):
#         for size in (32, 64):
#             # 创建并启动线程
#             threading.Thread(target=generate_thumbnail,
#                              args=(infile, (size, size))).start()

# 多个线程竞争资源的情况
"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是别多个线程竞争的资源
"""

# class Account(object):
#     # 银行账号
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()

#     def deposit(self, money):
#         # 通过锁保护临界资源
#         with self.lock:
#             new_balance = self.balance + money
#             time.sleep(0.001)
#             self.balance = new_balance

# class AddMoneyThread(threading.Thread):
#     # 自定义线程类
#     def __init__(self, account, money):
#         self.account = account
#         self.money = money
#         # 自定义线程的初始化方法中必须调用父类的初始化方法
#         super().__init__()

#     def run(self):
#         # 线程启动后要执行的操作
#         self.account.deposit(self.money)

# def main():
#     account = Account()
#     # 创建线程池
#     pool = ThreadPoolExecutor(max_workers=100)
#     futures = []
#     for _ in range(100):
#         # 创建线程的第一种方式
#         # threading.Thread(target=account.deposit, args=(1, )).start()

#         # 创建线程的第二种方式
#         AddMoneyThread(account, 1).start()

#         # 创建线程的第三种方式：调用线程池中的线程来执行特定任务
#         future = pool.submit(account.deposit, 1)
#         futures.append(future)

#     # 关闭线程池
#     pool.shutdown()

#     for future in futures:
#         future.result()

#     print(account.balance)
"""
修改上面的程序，启动5个线程向账户中存钱，5个线程从账户中取钱，
取钱时如果余额不足就暂停线程进行等待。
为了达到上述目标，需要对存钱和取钱的线程进行调度，在余额不足时取钱的线程暂停并释放锁，
而存钱的线程将钱存入后要通知取钱的线程，使其从暂停状态被唤醒。
可以使用threading模块的Condition来实现线程调度，该对象也是基于锁来创建的，
代码如下所示：
"""


class Account():
    """银行账户"""
    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, ':', money, '====>',
              account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, ':', money, '<====',
              account.balance)
        sleep(1)


def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()
