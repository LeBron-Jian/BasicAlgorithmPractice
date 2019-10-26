# _*_coding:utf-8_*_

# 修改插入排序，加入一个区间，即gap
def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1  # j指的是手里的牌
        while tmp < li[j] and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j指的是手里的牌
        while tmp < li[j] and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >=1:
        insert_sort_gap(li, d)
        d //= 2

li = list(range(10))
import random
random.shuffle(li)
shell_sort(li)
print(li)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]