'''
Python自带的heapq模块
可以实现堆的算法
'''
import heapq  # q——》queue优先队列
import random

li = list(range(100))
random.shuffle(li)
# print(li)

# 建堆
heapq.heapify(li)
heapq.heappop(li)

n = len(li)
# for i in range(n):
#     print(heapq.heappop(li), end='*')


# *********************向下调整函数的实现**********************************
def sift1(li, low, high):
    '''

    :param li: 列表
    :param low:  堆的根节点位置
    :param high:  堆的最后一个元素的位置
    :return:
    '''
    i = low  # 先把根节点扒下来  i最开始指向根节点，
    j = 2 * i + 1  # j表示左节点，即左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只有j位置有数，就一直循环
        # li[j+1]代表右孩子指向的数  左右孩子比较，如果右孩子比较大
        if j + 1 <= high and li[j + 1] < li[j]:   # j + 1 <= high 是保证不要越界
            j = j + 1   # 此时j 指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j   # 往下看一层
            j = 2 * j + 1  # 孩子节点
        else:  # tmp更大，把tmp放到 i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp   # 把tmp放到叶子节点


def sift(data, low, high):
    i = low
    j = 2*i+1
    tmp = data[i]
    while j <=high:
        if j < high and data[j] < data[j+1]:
            j+=1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2*i+1
        else:
            break
    data[i] = tmp

def heap_li(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # i表示建堆的时候调整的部分的跟的下标
        sift(li, i, n - 1)
    # 建堆完成了
    print('建堆完成后的列表：',li)
    for i in range(n-1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high
    print(li)

li = [i for i in range(12)]
import random
random.shuffle(li)
print(li)

heap_li(li)
print(li)
'''
[7, 2, 4, 3, 8, 9, 0, 5, 11, 6, 10, 1]
建堆完成后的列表： [11, 10, 9, 5, 8, 4, 0, 2, 3, 6, 7, 1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
'''