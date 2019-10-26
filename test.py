# _*_coding:utf-8_*_
'''


class Shape:
    pass


# 顺序查找也叫线性查找，从列表第一个元素开始，顺序进行搜索
# 知道找到元素或者搜索到列表最后一个元素为止
def linear_search(li, val):
    for i in li:
        if val == li[i]:
            return i


# 二分查找又叫折半查找，从有序列表的初始候选区开始，通过对待查找
# 的值与候选区中的值的比较，可以使得候选区减少一半
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if val == li[mid]:
            return mid
        elif val < li[mid]:  # 如果val在中间数左边，移动high下标
            right -= 1
        else:
            left += 1  # 如果val在中间数右边，移动low下标

    return False


# 冒泡排序：像开水烧起泡一样，把最大的元素冒泡到最上面，一趟就把最大的冒到最上面
# 冒到最上面的区域叫有序区，下面叫无序区
# 简单来说，列表每相邻的数，如果前面比后面的大，则交换这两个数
# 一趟排序完成后，则无序区减少一个数，有序区增加一个数
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j + 1] > li[j]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


# 冒泡排序存在一个最好的情况就是列表本身已经排好序了，所以可以加一个优化
# 即如果没有出现交换的情况，说明列表已经有序，可以直接结束算法，则直接return
def optimize_bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            li[j], li[j + 1] = li[j + 1], li[j]
            exchange = True
        if not exchange:
            return li
    return li


# 选择排序：一趟排序记录最小的数，放到第一个位置
# 再一趟排序记录列表无序区最小的数，放到第二个位置
def select_sort(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort_optimize(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li


# 插入排序 把列表分为有序区和无序区两个部分，最初有序区只有一个元素
# 然后每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空
def insert_sort(li):
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        if j > 0 and temp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp
    return li


# for i in range(1, 5):
#     print(i)

def quick_sort1(data):
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选择基准数，也可以选取第一个或最后一个
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


li = [3, 2, 4, 5, 6, 7, 1]
# print(quick_sort(li))
# [1, 2, 3, 4, 5, 6, 7]

def partition1(data,left,right):
    # 把左边第一个元素赋值给tmp，此时left指向空
    tmp = data[left]
    # 如果左右两个指针不重合，则继续
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]

        while left<right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: #从右面找比tmp小的数
            right -= 1      # 往左走一步
        li[left] = li[right] #把右边的值写到左边空位上
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] #把左边的值写到右边空位上
        # print(li, 'left')
    li[left] = tmp      # 把tmp归位
    return left

def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)
    return data

li1 = [3, 2, 4, 5, 6, 7, 1]
# print(quick_sort(li, 0, len(li1)-1))
# [1, 2, 3, 4, 5, 6, 7]

a = input("请输入数字：")
b = input("请输入数字：")
print("a+b=",(int(a)+int(b)))
'''
