'''
折半查找算法
'''


def binarySearch(x, arr, low, high):
    # 迭代算法
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            break
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1
    return mid


def binarySearchDG(x, arr, low, high):
    # 递归算法
    if low > high:
        return -1

    mid = (low + high) // 2
    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binarySearchDG(x, arr, low, mid - 1)
    else:
        return binarySearchDG(x, arr, mid + 1, high)


arr = list(range(0, 22, 2))
print(arr)
print(binarySearch(16, arr, 2, 10))
print(binarySearchDG(16, arr, 2, 10))
