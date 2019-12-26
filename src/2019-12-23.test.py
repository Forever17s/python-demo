# encoding:utf-8
"""
author: wgc
version: 0.7
"""

from random import randint
from time import time, sleep
from multiprocessing import Process, Queue
from os import getpid
from threading import Thread, Lock
import tkinter
import tkinter.messagebox
"""
多进程
Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。
fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，而子进程中的返回值永远都是0。
Python的os模块提供了fork()函数。
由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。
"""

# 下面用一个下载文件的例子来说明使用多进程和不使用多进程到底有什么差别，先看看下面的代码。

# def download_task(fileName):
#     print('开始下载%s...' % fileName)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f"{fileName}下载完成！耗费了{time_to_download}秒")

# def main():
#     start = time()
#     download_task('测试.txt')
#     download_task('data.json')
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))
"""
从上面的例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，那么即使执行两个毫不相关的下载任务，也需要先等待一个文件下载完成后才能开始下一个下载任务，很显然这并不合理也没有效率。
接下来我们使用多进程的方式将两个下载任务放到不同的进程中，代码如下所示。
"""

# def download_task(fileName):
#     print('启动下载，进程号为【%d】。' % getpid())
#     print('开始下载%s...' % fileName)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{fileName}下载完成！耗时{time_to_download}秒。')

# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('test2019年12月23日19:52:38.text', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('test2', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总耗时为%.2f秒' % (end - start))
"""
在上面的代码中，我们通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给函数的参数。
Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。
"""
"""
多线程
在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，然而该模块过于底层，而且很多功能都没有提供，因此目前的多线程开发我们推荐使用threading模块，该模块对多线程编程提供了更好的面向对象的封装。
我们把刚才下载文件的例子用多线程的方式来实现一遍。
"""

# def download_task(fileName):
#     print('开始下载%s...' % fileName)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{fileName}下载完成！耗时{time_to_download}秒。')

# def main():
#     start = time()
#     t1 = Thread(target=download_task, args=('2019年12月24日19:24:49.txt', ))
#     t1.start()
#     t2 = Thread(target=download_task, args=('(¦3[▓▓]晚安.txt', ))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗时%.2f秒。' % (end - start))
"""
我们可以直接使用threading模块的Thread类来创建线程，但是我们之前讲过一个非常重要的概念叫“继承”，我们可以从已有的类创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。
代码如下所示。
"""

# class DownloadTask(Thread):
#     def __init__(self, fileName):
#         super().__init__()
#         self._fileName = fileName

#     def run(self):
#         print('开始下载%s...' % self._fileName)
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print(f'{self._fileName}下载完成！耗时{time_to_download}秒。')

# def main():
#     start = time()
#     t1 = DownloadTask('2019-12-24 19:44:52.txt')
#     t1.start()
#     t2 = DownloadTask('test.txt')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗时%.2f秒。' % (end - start))
"""
因为多个线程可以共享进程的内存空间，因此要实现多个线程间的通信相对简单，大家能想到的最直接的办法就是设置一个全局变量，多个线程共享这个全局变量即可。
但是当多个线程共享同一个变量（我们通常称之为“资源”）的时候，很有可能产生不可控的结果从而导致程序失效甚至崩溃。
如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。
下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。
"""

# class Account(object):
#     def __init__(self):
#         self._balance = 0

#     def deposit(self, money):
#         new_balance = self._balance + money
#         sleep(0.0001)
#         self._balance = new_balance

#     @property
#     def balance(self):
#         return self._balance

# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money

#     def run(self):
#         self._account.deposit(self._money)

# def main():
#     account = Account()
#     threads = []

#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     print(f'账户余额为：￥{account.balance}元')
"""
运行上面的程序，结果让人大跌眼镜，100个线程分别向账户中转入1元钱，结果居然远远小于100元。
之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护，
多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money这行代码，
多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果。
在这种情况下，“锁”就可以派上用场了。
我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，
而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。
下面的代码演示了如何使用“锁”来保护对银行账户的操作，从而获得正确的结果。
"""

# class Account(object):
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()

#     def deposit(self, money):
#         # 先获取锁才能执行后续代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.0001)
#             self._balance = new_balance
#         finally:
#             # 在finally中执行释放锁的操作保证正常异常锁都能释放
#             self._lock.release()

#     @property
#     def balance(self):
#         return self._balance

# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money

#     def run(self):
#         self._account.deposit(self._money)

# def main():
#     account = Account()
#     threads = []

#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     print(f'账户余额为：￥{account.balance}元')
"""
比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，这一点只要启动几个执行死循环的线程就可以得到证实了。
之所以如此，是因为Python的解释器有一个“全局解释器锁”（GIL）的东西，任何线程执行前必须先获得GIL锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，这是一个历史遗留问题，但是即便如此，就如我们之前举的例子，使用多线程在提升执行效率和改善用户体验方面仍然是有积极意义的。
"""
"""
将耗时间的任务放到线程中以获得更好的用户体验。

如下所示的界面中，有“下载”和“关于”两个按钮，用休眠的方式模拟点击“下载”按钮会联网下载文件需要耗费10秒的时间，
如果不使用“多线程”，我们会发现，当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，这显然是非常糟糕的用户体验，代码如下所示。
"""

# def download():
#     # 模拟下载任务需要花费10秒钟时间
#     sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')

# def show_about():
#     tkinter.messagebox.showinfo('关于', '时间：2019年12月25日20:17:50')

# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)

#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')

#     tkinter.mainloop()
"""
如果使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程，
修改后的代码如下所示。
"""

# def main():
#     class DownloadTaskHanlder(Thread):
#         def run(self):
#             sleep(10)
#             tkinter.messagebox.showinfo('提示', '下载完成!')
#             # 启用下载按钮
#             button1.config(state=tkinter.NORMAL)

#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程（主程序退出就不再保留执行）
#         # 在线程中处理耗时的下载任务
#         DownloadTaskHanlder(daemon=True).start()

#     def show_about():
#         tkinter.messagebox.showinfo('关于', '时间：2019年12月25日20:17:50')

#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', 1)

#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')

#     tkinter.mainloop()
"""使用多进程对复杂任务进行“分而治之”。"""
"""
我们来完成1~100000000求和的计算密集型任务，这个问题本身非常简单，有点循环的知识就能解决，
代码如下所示。
"""


def main1():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for x in number_list:
        total += x
    end = time()
    print('Execution time planA: %.3fs, total: %s' % ((end - start), total))


"""
在上面的代码中，创建了一个列表容器然后填入了100000000个数，这一步其实是比较耗时间的，
所以为了公平起见，当我们将这个任务分解到8个进程中去执行的时候，
我们暂时也不考虑列表切片操作花费的时间，只是把做运算和合并运算结果的时间统计出来，代码如下所示。
"""


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    end = time()
    print('Execution time planB: %.3fs, total: %s' % ((end - start), total))


def main2():
    number_list = [x for x in range(1, 10001)]
    list2 = number_list[200:200 + 100]
    print(list2)


if __name__ == '__main__':
    main1()
    main()
    # main2()
