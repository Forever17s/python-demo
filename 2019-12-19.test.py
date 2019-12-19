# encoding:utf-8
"""
author: wgc
version: 0.5
"""

# import time
# from math import sqrt
import json
import requests
"""
读写文本文件
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码），如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败。下面的例子演示了如何读取一个纯文本文件。
"""

# def main():
#     f = open('./tests/测试.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()
"""
请注意上面的代码，如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理，如下所示。
"""

# def main():
#     f = None
#     try:
#         f = open('./tests/测试a.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#     finally:
#         if f:
#             f.close()
"""
如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。
"""

# def main():
#     try:
#         with open('测试2.txt', 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
"""
除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中，代码如下所示。
"""

# def main():
#     # 一次性读取整个文件内容
#     # with open('./tests/测试.txt', 'r', encoding='utf-8') as f:
#     #     print(f.read())

#     # 通过 for - in 循环逐行读取
#     with open('./tests/测试.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()

#     # 读取文件按行读取到列表中
#     # with open('./tests/测试.txt') as f:
#     #     lines = f.readlines()
#     # print(lines)
"""
要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常。下面的例子演示了如何将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
"""

# def is_prime(num):
#     """判断是否为素数"""
#     assert num > 0  # 断言是否为正数
#     for factorial in range(2, int(sqrt(num)) + 1):
#         if num % factorial == 0:
#             return False
#     return True if num != 1 else False

# def main():
#     fileNames = ('a.text', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for fileName in fileNames:
#             fs_list.append(open('./tests/' + fileName, 'w', encoding='utf-8'))
#         for num in range(1, 10000):
#             if is_prime(num):
#                 if num < 100:
#                     fs_list[0].write(str(num) + '\n')

#                 elif num < 1000:
#                     fs_list[1].write(str(num) + '\n')

#                 else:
#                     fs_list[2].write(str(num) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误！')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成！')

# def main():
#     try:
#         with open('./tests/pic1.jpg', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))  # <class 'bytes'>
#         with open('./tests/pic2.jpg', 'wb') as fs2:
#             fs2.write(data)

#     except FileNotFoundError:
#         print('读写文件无法打开。')
#     except IOError:
#         print('读写文件时出现错误。')
#     print('程序执行结束')

# def main():
#     mydict = {
#         'name':
#         'test',
#         'age':
#         42,
#         'friends': ['testA', 'testB'],
#         'cars': [
#             {
#                 'brand': 'BYD',
#                 'max_speed': 180
#             },
#             {
#                 'brand': 'Audi',
#                 'max_speed': 280
#             },
#             {
#                 'brand': 'Benz',
#                 'max_speed': 320
#             },
#         ]
#     }
#     try:
#         with open('./tests/data.json', 'w', encoding='utf-8') as fs:
#             json.dump(mydict, fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成！')
"""
json模块主要有四个比较重要的函数，分别是：
    dump - 将Python对象按照JSON格式序列化到文件中
    dumps - 将Python对象处理成JSON格式的字符串
    load - 将文件中的JSON数据反序列化成对象
    loads - 将字符串的内容反序列化成Python对象
"""


def main():
    payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
    resp = requests.get('http://httpbin.org/get', params=payload)
    try:
        with open('./tests/request.json', 'w', encoding='utf-8') as fs:
            json.dump(json.loads(resp.text), fs)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    main()
