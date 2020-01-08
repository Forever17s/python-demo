# encoding:utf-8
"""
author: wgc
version: 1.2
title: Python语言进阶
"""
from functools import partial
from threading import Lock
from abc import ABCMeta, abstractmethod
"""
函数的使用方式
  函数可以赋值给变量
  函数可以作为函数的参数
  函数可以作为函数的返回值
"""

# 高阶函数的用法（filter、map以及它们的替代品）

# items1 = list(map(lambda x: x**2, filter(lambda x: x % 2, range(1, 10))))
# items2 = [x**2 for x in range(1, 10) if x % 2]
# print(items1)
# print(items2)
"""
位置参数、可变参数、关键字参数、命名关键字参数
参数的元信息（代码可读性问题）
匿名函数和内联函数的用法（lambda 函数）
闭包和作用域问题
  global: 声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）
  nonocal: 声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）
装饰器函数（使用装饰器和取消装饰器）
"""

# 例子：输出函数执行时间的装饰器
# def record_time(func):
# 	# 自定义装饰函数的装饰器
# 	print(func)

# 	@wraps(func)
# 	def wrapper(*args, **kwargs):
# 		start = time()
# 		result = func(*args, **kwargs)
# 		print(f'{func.__name__}: {time() - start}s')
# 		return result
# 	return wrapper

# 例子：用装饰器来实现单例模式
# def singleton(cls):
# 	instance = {}
# 	@wraps(cls)
# 	def wrapper(*args, **kwargs):
# 		if cls not in instance:
# 			instance[cls] =cls(*args, **kwargs)
# 		return instance[cls]

# 	return wrapper

# @singleton
# class President():
# 	# 总统类（单例模式）
# 	pass

# 上面的代码没有实现线程安全的单例,下面再优化一下

# def singleton(cls):
# 	instance = {}
# 	locker = Lock()

# 	@wraps(cls)
# 	def wrapper(*args, **kwargs):
# 		if cls not in instance:
# 			with locker:
# 				if cls not in instance:
# 					instance[cls] = cls(*args, **kwargs)
# 		return instance[cls]
# 	return wrapper

# 面向对象相关知识：封装、继承、多态

# 例子：工资结算系统
# 月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成


class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_salary(self):
        # 结算月薪，抽象方法
        pass


class Manager(Employee):
    # 部门经理

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    # 程序猿

    def __init__(self, name, working_hours=0):
        self._working_hours = working_hours
        super().__init__(name)

    def get_salary(self):
        return self._working_hours * 200.0


class SalesMan(Employee):
    # 销售员

    def __init__(self, name, sales=0.0):
        self._sales = sales
        super().__init__(name)

    def get_salary(self):
        return self._sales * 0.05 + 1800.0


class EmployeeFactory():
    # 创建员工的工厂函数

    @staticmethod
    def create(employee_type, *args, **kwargs):
        employee_type = employee_type.upper()
        employee = None
        if employee_type == "M":
            employee = Manager(*args, **kwargs)
        elif employee_type == "P":
            employee = Programmer(*args, **kwargs)
        elif employee_type == "S":
            employee = SalesMan(*args, **kwargs)

        return employee


def main():
    employees = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]

    for employee in employees:
        print('%s: %.2f元' % (employee._name, employee.get_salary()))


if __name__ == '__main__':
    main()
