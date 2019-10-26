# -*- coding: utf-8 -*-
'''
        选择排序
遍历列表一遍，拿到最小的值放到列表第一个位置，再找到剩余列表中最小的值
放到第二个位置

时间复杂度为O(n**2)
'''

# 这个便于理解，但是不好，时间复杂度高，不推荐使用
def sample_select_sort(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

li = [3,4,5,6,72,1,2]
re = sample_select_sort(li)
print(re)

def select_sort(li):
    # 遍历列表一遍
    for i in range(len(li)-1):
        # 假设当前最小的值的索引就是i
        mid_loc = i
        # 算法中能抠则抠，能省则省，所以i也可以，i+1更省
        for j in range(i+1,len(li)):
            if li[j] <li[mid_loc]:
                min_loc = j
        # mid_loc值如果发生过交换，表示最小的值的下标不是i，而是min_loc
        if mid_loc != i:
            li[i],li[mid_loc] = li[mid_loc],li[i]
    return li
