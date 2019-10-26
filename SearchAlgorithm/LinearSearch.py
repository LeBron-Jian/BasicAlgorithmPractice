# -*- coding: utf-8 -*-
'''
顺序查找，也叫线性查找，从列表第一个元素开始，
顺序进行搜索，直到找到元素或者搜索到列表最后一个元素为止
时间复杂度为O(n)

'''


def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return None


data_set = [1, 4, 5, 6, 7, 1]
value = 6
a = linear_search(data_set, value)
print(a)
