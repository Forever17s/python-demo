# encoding:utf-8
"""
author: wgc
version: 1.0
"""
"""
排序算法（选择、冒泡和归并） 和查找算法（顺序和折半）
"""
"""
lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
"""


def select_sort(origin_items, comp=lambda x, y: x < y):
    counter = 0
    # 简单选择排序
    items = origin_items[:]
    for i in range(0, len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            counter += 1
            if (comp(items[j], items[min_index])):
                min_index = j
        items[min_index], items[i] = items[i], items[min_index]
    return (items, counter)


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    # 冒泡排序
    counter = 0
    items = origin_items[:]
    for i in range(0, len(items) - 1):
        for j in range(0, len(items) - 1 - i):
            counter += 1
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return (items, counter)


def merge_sorted(items, comp=lambda x, y: x < y):
    # 归并排序（分治法）
    if len(items) < 2:
        return items[:]

    mid = len(items) // 2
    left = merge_sorted(items[:mid], comp)
    right = merge_sorted(items[mid:], comp)
    return merge(left, right, comp)


def merge(left, right, comp):
    # 合并：将两个有序的列表合并成一个有序的列表
    items = []
    leftIndex, rightIndex = 0, 0
    # 比较left和right队列中的数据
    while leftIndex < len(left) and rightIndex < len(right):
        if comp(left[leftIndex], right[rightIndex]):
            items.append(left[leftIndex])
            leftIndex += 1
        else:
            items.append(right[rightIndex])
            rightIndex += 1
    # 将left或者right余下的数据加入
    items += left[leftIndex:]
    items += right[rightIndex:]
    return items


def seq_search(items, key):
    # 顺序查找
    for index, item in enumerate(items):
        if item == key:
            return f"{key}在第{index + 1}位"
    return f"未找到{key}"


def bin_search(origin_items, key):
    items = merge_sorted(origin_items[:])
    # 折半查找, 得先排序
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return f"{key}在第{mid + 1}位"
    return f"未找到{key}"


def main():
    arr = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    print("简单选择排序: ", select_sort(arr))
    print("冒泡排序: ", bubble_sort(arr))
    print("归并排序: ", merge_sorted(arr))
    print("顺序查找", seq_search(arr, 99))
    print("顺序查找", seq_search(arr, 233))
    print("折半查找", bin_search(arr, 99))
    print("折半查找", bin_search(arr, 233))


if __name__ == '__main__':
    main()
