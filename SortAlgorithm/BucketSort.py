#_*_coding:utf-8_*_

# 假设我们知道数组的最大值为10000，那么我们将其分为100个桶
def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶 也就是100个空列表
    for var in li:
        # 一个桶里放入 var//（maxnum//n)个数  那最后一个数，也就是num=10000的时候，我们会发现越界了！
        # 0 -》 0号桶， 86 ->
        i = min(var // (max_num // n), n-1)  # i表示var放到几号桶里
        buckets[i].append(var)  # 把var加入到桶里，也就是将数组放入每个桶里
        # [0, 2, 4] 就像数组已经有序了，但是下面我们插入3，即为 [0,2,4,3]然后我们进行排序，冒泡排序
        # 保持桶内的顺序，也就是对每个桶进行排序即可
        for j in range(len(buckets[i])-1, 0, -1):  # 从数组的后面往前找数
            if buckets[i][j] < buckets[i][j-1]:  # 如果后面一个数比前面的大，那么就交换他们
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)  # 将buc这个列表加入分类好的列表后面
    return sorted_li

import random

li = [random.randint(0, 10) for i in range(10)]
# print(li)
li = bucket_sort(li)
print(li)