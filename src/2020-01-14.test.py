# encoding:utf-8
"""
author: wgc
version: 1.6
title: Python语言进阶
"""

import concurrent.futures
import math
import asyncio
import re
import aiohttp
"""
多进程：多进程可以有效地解决GIL问题，实现多进程主要的类是Process，
其它辅助的类跟threading模块中类似，进程间共享数据可以使用管道、套接字等，
在multiprocessing模块中有一个Queue类，它基于管道和锁机制提供了多个进程共享的队列。
下面是官方文档上关于多进程和线程池的一个示例
"""
"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""

# PRIMES = [
#     1116281, 1297337, 104395303, 472882027, 533000389, 817504243, 982451653,
#     112272535095293, 112582705942171, 112272535095293, 115280095190773,
#     115797848077099, 1099726899285419
# ] * 5

# def is_prime(n):
#     # 判断素数
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def main():
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))

# if __name__ == '__main__':
#     main()
"""
多线程和多进程的比较
以下情况需要使用多线程：
    a.程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，\
        所以使用线程而不是进程维护共享状态的代价相对较小。
    b.程序会花费大量时间在 I/O 操作上，没有太多并行计算的需求且不需要占用太多内存

以下情况需要使用多进程：
    a.程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）
    b.程序的输入可以并行的分成块，并且可以将运算结果合并
    c.程序在内存使用方面没有任何限制且不依赖于 I/O 操作（如：读写文件、套接字等）        
"""
"""
异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，
我们并不能保证人为将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将 CPU 处理时间让位给另一项任务。
异步任务通常多任务协作处理的方式来实现，优于任务执行时间和顺序的不确定，
因此需要通过回调式编程或者 future 对象来获取任务的执行结果。
Python 3 通过 asyncio 模块和 await 和 async 关键字来支持异步处理
"""

# def num_generator(m, n):
#     # 指定范围的数字生成器
#     yield from range(m, n + 1)

# async def prime_filter(m, n):
#     # 素数过滤器
#     primes = []

#     for i in num_generator(m, n):
#         flag = True
#         for j in range(2, int(i**0.5 + 1)):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             print('Prime => ', i)
#             primes.append(i)
#         await asyncio.sleep(0.001)
#     return tuple(primes)

# async def square_mapper(m, n):
#     # 平方映射器
#     squares = []

#     for i in num_generator(m, n):
#         print('Square => ', i * i)
#         squares.append(i * i)

#         await asyncio.sleep(0.01)

#     return squares

# def main():
#     loop = asyncio.get_event_loop()
#     future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
#     future.add_done_callback((lambda x: print(x.result())))
#     loop.run_until_complete(future)
#     loop.close()
"""
说明：上面的代码使用 get_event_loop 函数获得系统默认的事件循环，通过 gather 函数可以获得一个 future 对象，
future 对象的 add_done_callback 可以添加执行完成时的回调函数， loop 对象的 run_until_complete 方法\
    可以等待通过 future 对象获得协程执行结果
"""
"""
Python 中有一个名为 aiohttp 的三方库，它提供了异步的 HTTP 客户端和服务端，这个三方库可以跟 asyncio 模块一块工作，
并提供了对 Future 对象的支持。Python 3.6 中引入了 async 和 await 来定义异步执行的函数以及创建异步上下文，
在 Python 3.7 中它们正式成为了关键字，下面的代码异步的从 5 个 URL 中获取页面并通过正则表达式的命名捕获提取了网站的标题
"""
# PATTERN = re.compile(r'\<titile\>(?P<title>.*)\<\/title\>')

# async def fetch_page(session, url):
#     async with session.get(url, ssl=False) as resp:
#         return await resp.text()

# async def show_title(url):
#     async with aiohttp.ClientSession() as session:
#         html = await fetch_page(session, url)
#         print(PATTERN.search(html).group('title'))

# def main():
#     urls = ('https://www.python.org/', 'https://git-scm.com/',
#             'https://www.jd.com/', 'https://www.taobao.com/',
#             'https://www.douban.com/')

#     loop = asyncio.get_event_loop()
#     tasks = [show_title(url) for url in urls]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()

# if __name__ == '__main__':
#     main()
"""
说明：异步 I/O 与多进程的比较
当程序不需要真正的并发性或并行性，而是更多的依赖异步处理和回调时，
asynio 就是一种很好的选择。如果程序中有大量的等待与休眠时，
也应该考虑 asynio，它很适合编写没有实时数据处理需求的 Web 应用服务器
"""
"""
Python还有很多用于处理并行任务的三方库，例如：joblib、PyMP等。
实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）和水平扩展（将单个节点变成多个节点）两种做法。
可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，
不同机器上的应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。
消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队列协议），
AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，最著名的实现包括：Apache的ActiveMQ、RabbitMQ等。

要实现任务的异步化，可以使用名为Celery的三方库。
Celery是Python编写的分布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理。
"""
