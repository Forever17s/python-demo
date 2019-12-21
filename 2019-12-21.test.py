# encoding:utf-8
"""
author: wgc
version: 0.6
"""
import re
"""
正则表达式
验证输入用户名和QQ号是否有效并给出对应的提示信息。
"""

# def main():
#     username = input("insert username:")
#     qq = input("insert QQ:")
#     # match函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#     if not m1:
#         print('insert useable username!')
#     m2 = re.match(r'[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('insert useable QQ!')
#     if m1 and m2:
#         print('done!')
"""
从一段文字中提取出国内手机号码
"""

# def main():
#     # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''
#     # 查找所有匹配并保存到一个列表中
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('----------------------------')
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('----------------------------')
#     # 通过search函数指定搜索位置找出所有匹配
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
"""
不良信息过滤
"""

# def main():
#     reg = '[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔'
#     sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
#     purified = re.sub(reg, '*', sentence, flags=re.IGNORECASE)
#     print(purified)
"""
拆分长字符串
"""


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[,，。.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main()
