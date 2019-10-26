#_*_coding:utf-8_*_

def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()  # 原列表清空，这样就不用建新列表，省内存
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0, 19) for _ in range(30)]
print(li)
count_sort(li)
print(li)
'''
[1, 4, 13, 6, 19, 4, 9, 14, 10, 15, 7, 1, 1, 9, 3, 8, 17, 3, 18, 1, 8, 17, 14, 2, 10, 0, 5, 8, 12, 15]
[0, 1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 9, 10, 10, 12, 13, 14, 14, 15, 15, 17, 17, 18, 19]
'''