# encoding:utf-8
"""
author: wgc
version: 0.4
"""

# import tkinter
# import tkinter.messagebox
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame
"""
基于tkinter模块的GUI


基本上使用tkinter来开发GUI应用需要以下5个步骤：
    1.导入tkinter模块中我们需要的东西。
    2.创建一个顶层窗口对象并用它来承载整个GUI应用。
    3.在顶层窗口对象上添加GUI组件。
    4.通过代码将这些GUI组件的功能组织起来。
    5.进入主事件循环(main loop)。
"""

# def main():
#     flag = True

#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         # color, msg = ('red', 'Hello, world!')\
#         #     if flag else ('blue', 'Goodbye, world!')
#         # label.config(text=msg, fg=color)
#         color, msg = ('red', 'hello, world!')\
#             if flag else ('blue', 'byebye, world!')
#         label.config(text=msg, fg=color)

#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('confirm', 'exit?'):
#             top.quit()

#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('960x640')
#     # 添加标题
#     top.title('TEST')
#     # 创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top,
#                           text='Hello, world!',
#                           font='Arial -32',
#                           fg='red')
#     label.pack(expand=True)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数修改绑定事件回调
#     button1 = tkinter.Button(panel, text='reset', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='exit', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
"""
使用Pygame进行游戏开发
Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，其中包含对图像、声音、视频、事件、碰撞等的支持。Pygame建立在SDL的基础上，SDL是一套跨平台的多媒体开发库，用C语言实现，被广泛的应用于游戏、模拟器、播放器等的开发。而Pygame让游戏开发者不再被底层语言束缚，可以更多的关注游戏的功能和逻辑。

下面我们来完成一个简单的小游戏，游戏的名字叫“大球吃小球”，当然完成这个游戏并不是重点，学会使用Pygame也不是重点，最重要的我们要在这个过程中体会如何使用前面讲解的面向对象程序设计，学会用这种编程思想去解决现实中的问题。
"""

# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('TEST')
#     x, y = 50, 50
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         # 设置窗口背景色
#         screen.fill((0, 222, 222))
#         # 绘制一个○，参数分别为：屏幕、颜色、圆心位置、半径、0表示填充○
#         pygame.draw.circle(screen, (
#             255,
#             0,
#             0,
#         ), (x, y), 30, 0)
#         # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
#         pygame.display.flip()
#         # 每隔50ms就改变小球的位置再刷新窗口
#         pygame.time.delay(50)
#         x, y = x + 5, y + 5
"""
添加碰撞检测
检测两个小球有没有碰撞其实非常简单，只需要检查球心的距离有没有小于两个球的半径之和。
为了制造出更多的小球，我们可以通过对鼠标事件的处理，在点击鼠标的位置创建颜色、大小和移动速度都随机的小球
"""


@unique
class Color(Enum):
    """color"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """get color"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """ball"""
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or\
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or\
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx * dx + dy * dy)
            if distance < self.radius + other.radius\
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius,
                           0)


def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))

    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获取点击鼠标位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击位置创建一个球，并赋予其属性
                ball = Ball(x, y, radius, sx, sy, color)
                # 添加到列表容器中
                balls.append(ball)
        # 重绘
        screen.fill((0, 222, 222))
        # 遍历容器中的球，如果没被吃掉就绘制，吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50ms就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 再次遍历检测是否能吃掉其它球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
