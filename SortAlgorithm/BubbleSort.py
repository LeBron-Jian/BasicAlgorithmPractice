# -*- coding: utf-8 -*-
'''
冒泡排序 bubble sort
列表每两个相邻的数，如果前面的比后面的大，则交换着两个数
一趟排序完成后，则无序区减少一个数，有序区增加一个数

时间复杂度为n**2
'''


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def optimize_bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange =True
        if not exchange:
            return li
    return li

origin_list = [9,8,7,6,5,4,3,2,1]
print('origin_list:', origin_list)
res = optimize_bubble_sort(origin_list)
print(res)
# origin_list: [9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
