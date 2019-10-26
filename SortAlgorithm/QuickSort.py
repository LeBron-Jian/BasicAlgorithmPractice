# -*- coding: utf-8 -*-
'''
            快速排序
让指定的元素归位，所谓归位，就是放到他应该放的位置
左边的元素比他小，右边的元素比他大，然后对每个元素归位，就完成了排序

正常情况下，快速排序的复杂度是O(nlogn)
快速排序存在一个最坏的情况，就是每次归位，都不能把列表分成两部分，
此时的复杂度就是O(n**2)
如果避免设计成这种最坏情况，可以在取第一个数的时候不要去取第一个元素
而是取一个列表中的随机数。
'''

# 归位函数
def partition(data, left, right): # 左右分别指向两端的元素
    # 把左边第一个元素赋值给tmp，此时left指向空
    tmp = data[left]
    # 如果左右两个指针不重合，则继续
    while left < right:  # 左右两个指针不重合，就继续
        # 当左边的元素小于右边，而且右边的元素大于tmp则不交换
        while left < right and data[right] >= tmp:
            right -= 1   # 右边的指标往左走一步
        # 如果right指向的元素小于tmp，就放到左边目前为空的位置
        data[left] = data[right]
        print('left:', li)
        # 如果left指向的元素小于tmp，则不交换
        while left < right and data[left] <= tmp:
            left += 1  # 此时left向右移动一位
        # 如果left指向的元素大于tmp，就交换到右边目前为空的位置
        data[right] = data[left]
        print('right:', li)
    # 最后把最开始拿出来的那个值，放到左右重合的那个位置上即可
    data[left] = tmp
    return left  # 最后返回这个位置


# 写好归位函数后，就可以递归调用这个函数，实现排序
def quick_sort(data, left, right):
    if left < right:
        # 找到指定元素的位置
        mid = partition(data, left, right)
        # 对左边的元素排序
        quick_sort(data, left, mid - 1)
        # 对右边的元素排序
        quick_sort(data, mid + 1, right)
    return data


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print('start:', li)
quick_sort(li, 0, len(li) - 1)
print('end:', li)

'''
start: [5, 7, 4, 6, 3, 1, 2, 9, 8]
left: [2, 7, 4, 6, 3, 1, 2, 9, 8]
right: [2, 7, 4, 6, 3, 1, 7, 9, 8]
left: [2, 1, 4, 6, 3, 1, 7, 9, 8]
right: [2, 1, 4, 6, 3, 6, 7, 9, 8]
left: [2, 1, 4, 3, 3, 6, 7, 9, 8]
right: [2, 1, 4, 3, 3, 6, 7, 9, 8]
left: [1, 1, 4, 3, 5, 6, 7, 9, 8]
right: [1, 1, 4, 3, 5, 6, 7, 9, 8]
left: [1, 2, 3, 3, 5, 6, 7, 9, 8]
right: [1, 2, 3, 3, 5, 6, 7, 9, 8]
left: [1, 2, 3, 4, 5, 6, 7, 9, 8]
right: [1, 2, 3, 4, 5, 6, 7, 9, 8]
left: [1, 2, 3, 4, 5, 6, 7, 9, 8]
right: [1, 2, 3, 4, 5, 6, 7, 9, 8]
left: [1, 2, 3, 4, 5, 6, 7, 8, 8]
right: [1, 2, 3, 4, 5, 6, 7, 8, 8]
end: [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''


# *****************方法二**********************
def quick_sort1(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]  # 第一个值

    while low < high: # 只要左右未遇见
        while low < high and array[high] > key:  # 找到列表右边比key大的值为止
            high -= 1
        # 此时直接把key(array[low]) 根比他大的 array[high]进行交换
        array[low] = array[high]
        array[high] = key

        # 这里要思考为什么是 <= 而不是 <
        while low < high and array[low] <= key: # 找到key左边比key大的值
            low += 1
        # 找到了左边比k大的值，把array[high]（此时应该换成了key）和这个比key大的array[low]进行调换
        array[high] = array[low]
        array[low] = key

    # 最后用同样的方法对分出来的左边的小组进行同上的做法
    quick_sort(array, left, low-1)
    # 再使用同样的方法对分出来的右边的小组进行同上的做法
    quick_sort(array, low+1, right)

# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# print('start:', li)
# quick_sort1(li, 0, len(li) - 1)
# print('end:', li)




def quick_sort(data):
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
print(quick_sort(li))
# [1, 2, 3, 4, 5, 6, 7]
