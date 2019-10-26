# -*- coding: utf-8 -*-
'''
二分查找，又叫折半查找，从有序列表的厨师候选区li[0:li]开始
通过对待查找的值与候选区中间值的比较，可以使候选区减少一半

空间复杂度：用来评估算法内存占用大小的式子
空间复杂度的表示方式与时间复杂度完全一样
    算法使用了几个变量：O(1)
    算法使用了长度为n的一维列表：O（n）
    算法使用了m行n列的二维列表：O（mn）

如何简单快速地判断算法复杂度
    确定问题的规模n
    循环减半过程logn
    k层关于n的循环 n**k
'''

def binary_search(data_set,value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            high = mid-1
        else:
            low = mid + 1
    else:
        return None



def bin_search(data_set,value,low,high):
    if low <high:
        mid = (low+high)//2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] >value:
            return bin_search(data_set,value,low,mid-1)
        else:
            return bin_search(data_set,value,mid+1,high)
    else:
        return None