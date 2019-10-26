# -*- coding: utf-8 -*-
'''
列表分成两段有序，然后分解成每个元素后，再合并成一个有序列表
这种操作就叫做一次归并

应用到排序就是，把列表分成一个元素一个元素的，一个元素当然有序，
将有序列表一个一个合并，最终合并成一个有序的列表

归并排序的时间复杂度是O(nlogn)

特殊的，归并排序还有一个O(n)的空间复杂度
'''


# 先考虑列表有数的情况
def merge(li, low, mid, high):
    i = low  # i为左边列表开头元素的坐标
    j = mid + 1  # j为右边列表开头元素的坐标
    ltmpd = []  # 临时列表
    # 只要两边都有数
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmpd.append(li[i])
            i += 1
        else:
            ltmpd.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数字了，就是两个箭头肯定有一个指向没数了
    while i <= mid:
        ltmpd.append(li[i])
        i += 1
    while j <= high:
        ltmpd.append(li[j])
        j += 1
    li[low:high + 1] = ltmpd
    # return ltmpd


# 此处要求前后两部分有序
li = [2, 4, 6, 8, 1, 3, 6, 7]
rs = merge(li, 0, 3, 7)
# print(rs)


def merge_sort(li, low, high):
    if low < high:  # 列表中至少两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)

li = list(range(10))
import random
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)

# 打印归并排序的过程
def merge_sort_sample(li, low, high):
    if low < high:  # 列表中至少两个元素，递归
        mid = (low + high) // 2
        merge_sort_sample(li, low, mid)
        merge_sort_sample(li, mid + 1, high)
        print(li[low:high+1])
        # merge(li, low, mid, high)

li = list(range(10))
import random
random.shuffle(li)
print(li)
merge_sort_sample(li, 0, len(li)-1)
print(li)

'''
[6, 1, 4, 2, 9, 8, 7, 3, 0, 5]
[6, 1]
[6, 1, 4]
[2, 9]
[6, 1, 4, 2, 9]
[8, 7]
[8, 7, 3]
[0, 5]
[8, 7, 3, 0, 5]
[6, 1, 4, 2, 9, 8, 7, 3, 0, 5]
[6, 1, 4, 2, 9, 8, 7, 3, 0, 5]
'''