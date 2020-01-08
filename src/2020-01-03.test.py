# encoding:utf-8
"""
author: wgc
version: 1.1
title: Python语言进阶
"""
import heapq
import itertools
from collections import Counter
import sys
import time

# # 使用生成式（推导式）语法

# preces = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# preces2 = {key: value for key, value in preces.items() if value > 100}
# print(preces2)

# 嵌套的列表
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# # print(scores)
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
#         print(scores)

# heapq、itertools等的用法

# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [{
#     'name': 'IBM',
#     'shares': 100,
#     'price': 91.1
# }, {
#     'name': 'AAPL',
#     'shares': 50,
#     'price': 543.22
# }, {
#     'name': 'FB',
#     'shares': 200,
#     'price': 21.09
# }, {
#     'name': 'HPQ',
#     'shares': 35,
#     'price': 31.75
# }, {
#     'name': 'YHOO',
#     'shares': 45,
#     'price': 16.35
# }, {
#     'name': 'ACME',
#     'shares': 75,
#     'price': 115.65
# }]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
"""
迭代工具 - 排列 / 组合 / 笛卡尔积
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""

# a = itertools.permutations("ABCD")
# b = itertools.combinations("ABCD", 3)
# c = itertools.product("ABCD", "123")
# for n in c:
#     print(n)

# collections模块下的工具类
"""
找出序列中出现次数最多的元素
"""

# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
#     'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
#     'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))
"""
常用算法：

穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
贪婪法 - 在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解。
分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。
"""

# 穷举法示例

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
# for x in range(100 // 5):
#     for y in range(100 // 3):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

personNum = 5
# fish = personNum + 1
# while True:
#     total = fish
#     enough = True
#     fishList = []
#     for _ in range(personNum):
#         if (total - 1) % personNum == 0:
#             average = (total - 1) // personNum
#             fishList.append(average)
#             total = average * (personNum - 1)
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish, fishList)
#         break
#     fish += personNum

# print((6 - 1) // 5 * 4)
# print((6 - 1) / 5 * 4)
"""
贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
名称	价格（美元）	重量（kg）
电脑	200	20
收音机	20	4
钟	175	10
花瓶	50	2
书	10	1
油画	90	9
"""
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
"""

# def main():
#     """主函数"""
#     max_weight = 20
#     all_things = [('电脑', 200, 20), ('收音机', 20, 4), ('钟', 175, 10),
#                   ('花瓶', 50, 2), ('书', 10, 1), ('油画', 90, 9)]
#     all_things.sort(key=lambda item: item[1] / item[2], reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing[2] <= max_weight:
#             print(f'小偷拿走了{thing[0]}')
#             total_weight += thing[2]
#             total_price += thing[1]
#     print(f'总价值: {total_price}美元，重量：{total_weight}kg')

# 分治法例子：快排
"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""

# def quickSort(arr):
#     length = len(arr)
#     if length <= 1:
#         return arr
#     midIndex = length // 2
#     midNum = arr[midIndex]
#     arr = arr[:midIndex] + arr[midIndex + 1:]
#     leftList = []
#     rightList = []
#     length = length - 1
#     for i in range(0, length):
#         if (arr[i] < midNum):
#             leftList.append(arr[i])
#         else:
#             rightList.append(arr[i])
#     result = quickSort(leftList) + [midNum] + quickSort(rightList)
#     return result

# def main():
#     arr = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
#     print(quickSort(arr))
"""
递归回溯法：叫称为试探法，按选优条件向前搜索，
当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，
比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""

# SIZE = 5
# total = 0

# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()

# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#             board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0

# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往少于朴素解法（用空间换取时间）
"""

# def fib(num, temp={}):
#     # 用递归计算Fibonacci数
#     if num in (1, 2):
#         return 1
#     temp[num] = fib(num - 1) + fib(num - 2)
#     return temp[num]

# def main():
#     print(fib(10))
"""
动态规划例子2：子列表元素之和的最大值。（使用动态规划可以避免二重循环）

说明：子列表指的是列表中索引（下标）连续的元素构成的列表；
列表中的元素是int类型，可能包含正整数、0、负整数；
程序输入列表中的元素，输出子列表元素求和的最大值，例如：
输入：1 -2 3 5 -3 2
输出：8

输入：0 -2 3 5 -1 2
输出：9

输入：-9 -2 -3 -5 -3
输出：-2
"""


def main():
    items = list(map(int, input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(partial)
    print(overall)
    print(overall[0])


if __name__ == '__main__':
    main()
