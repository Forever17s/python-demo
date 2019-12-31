# encoding:utf-8
"""
author: wgc
version: 0.8
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from base64 import b64encode
from json import dumps
from threading import Thread
from smtplib import SMTP
from email.headers import Header
from email.mime.text import MIMEText
import urllib.parse
import http.client
import json
"""
基于传输层协议的套接字编程
套接字这个词对很多不了解网络编程的人来说显得非常晦涩和陌生，其实说得通俗点，套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用。
在Python中也可以基于套接字来使用传输层提供的传输服务，并基于此开发自己的网络应用。
实际开发中使用的套接字可以分为三类：流套接字（TCP套接字）、数据报套接字和原始套接字。
"""
"""


TCP套接字


"""
"""
所谓TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口。
在Python中可以通过创建socket对象并指定type属性为SOCK_STREAM来使用TCP套接字。
由于一台主机可能拥有多个IP地址，而且很有可能会配置多个不同的服务，所以作为服务器端的程序，需要在创建套接字对象后将其绑定到指定的IP地址和端口上。
这里的端口并不是物理设备而是对IP地址的扩展，用于区分不同的服务，例如我们通常将HTTP服务跟80端口绑定，而MySQL数据库服务默认绑定在3306端口，这样当服务器收到用户请求时就可以根据端口号来确定到底用户请求的是HTTP服务器还是数据库服务器提供的服务。
端口的取值范围是0~65535，而1024以下的端口我们通常称之为“著名端口”（留给像FTP、HTTP、SMTP等“著名服务”使用的端口，有的地方也称之为“周知端口”），自定义的服务通常不使用这些端口，除非自定义的是HTTP或FTP这样的著名服务。


下面的代码实现了一个提供时间日期的服务器。
"""

# def main():
#     # 1.创建套接字对象并指定使用那种传输服务
#     # family=AF_INET - IPv4地址
#     # family=AF_INET6 - IPv6地址
#     # type=SOCK_STREAM - TCP套接字
#     # type=SOCK_DGRAM - UDP套接字
#     # type=SOCK_RAW - 原始套接字
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 2.绑定IP地址和端口（端口用于区分不同的服务）
#     # 同一时间在同一个端口只能绑定一个服务否则报错
#     server.bind(('192.168.1.2', 9527))
#     # 3.开启监听 - 监听客户端连接到服务端
#     # 参数512可以理解为连接队列的大小
#     server.listen(512)
#     print("服务器启动监听...")
#     while True:
#         # 4.通过循环接收客户端的连接并做出相应的处理（提供服务）
#         # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         # accept方法返回一个元组其中的第一个元素是客户端对象
#         # 第二个元素是连接到服务器的客户端的地址（由IP和端口两部分组成）
#         client, address = server.accept()
#         print(str(address) + '连接到了服务器。')
#         # 5.发送数据
#         client.send(str(datetime.now()).encode('utf-8'))
#         # 6.断开连接
#         client.close()
"""
当然我们也可以通过Python的程序来实现TCP客户端的功能，相较于实现服务器程序，实现客户端程序就简单多了

代码如下所示。
"""

# def main():
#     # 1.创建套接字
#     client = socket()
#     # 2.连接到服务器（需要指定IPV4和TCP协议）
#     client.connect(('192.168.1.2', 9527))
#     # 3.从服务器接收数据
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
"""
需要注意的是，上面的服务器并没有使用多线程或者异步I/O的处理方式，这也就意味着当服务器与一个客户端处于通信状态时，其他的客户端只能排队等待。
很显然，这样的服务器并不能满足我们的需求，我们需要的服务器是能够同时接纳和处理多个用户请求的。
下面我们来设计一个使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。
"""

# def main():
#     # 自定义线程类
#     class FileTransferHandler(Thread):
#         def __init__(self, cclient):
#             super().__init__()
#             self.cclient = cclient

#         def run(self):
#             my_dict = {}
#             my_dict['filename'] = 'telnet.png'
#             # JSON是纯文本不能携带二进制数据
#             # 所以图片的二进制数据要处理成base64编码
#             my_dict['filedata'] = data
#             # 通过dumps函数将字典处理成JSON字符串
#             json_str = dumps(my_dict)
#             # 发送JSON字符串
#             self.cclient.send(json_str.encode('utf-8'))
#             self.cclient.close()

#     # 1.创建套接字对象并指定使用哪种传输服务
#     server = socket()
#     # 2.绑定IP地址和端口(区分不同的服务)
#     server.bind(('192.168.1.1', 9527))
#     # 3.开启监听 - 监听客户端连接到服务器
#     server.listen(512)
#     print('服务器启动开始监听...')
#     with open('./../tests/telnet.png', 'rb') as f:
#         # 将二进制数据处理成base64再解码成字符串
#         data = b64encode(f.read()).decode('utf-8')
#     while True:
#         client, addr = server.accept()
#         # 启动一个线程来处理客户端的请求
#         FileTransferHandler(client).start()
"""
发送电子邮件
"""

# def main():
#     sender = 'test@qq.com'
#     receivers = ['test@qq.com', 'test@163.com']
#     message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
#     message['From'] = Header('TEST', 'utf-8')
#     message['To'] = Header('HI', 'utf-8')
#     message['Subject'] = Header('示例代码实验邮件', 'utf-8')
#     smtper = SMTP('smtp.126.com')
#     # 请自行修改下面的登录口令
#     smtper.login(sender, 'password')
#     smtper.sendmail(sender, receivers, message.as_string())
#     print('邮件发送完成！')
"""
发送短信
"""


def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({
        'account': '你自己的账号',
        'password': '你自己的密码',
        'content': '您的验证码是：147258。请不要把验证码泄露给其他人。',
        'mobile': '接收者的手机号',
        'format': 'json'
    })
    print(params)
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()
