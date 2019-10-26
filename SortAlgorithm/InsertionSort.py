# -*- coding: utf-8 -*-
'''
        插入排序
把列表分为有序区和无序区两个部分，最初有序区只有一个元素
然后每次从无序区选择一个元素，插入到有序区的位置，知道无序区变为空
'''

def insert_sort(li):
    for i in range(1,len(li)):
        template = li[i]
        j = i-1
        # 找到一个合适的位置插进去
        while j>=0 and template <li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = template
    return li