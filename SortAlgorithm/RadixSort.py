#_*_coding:utf-8_*_

def radix_sort(li):
    # 最大值的位数 9 -> 1， 99 ->2  888-> 3, 10000 ->5
    max_num = max(li)  # 先找到最大值，取位数我们可以使用log函数，当然也可以使用如下方法
    it = 0
    while 10 ** it <= max_num:  # 思考为什么是等于
        buckets = [[] for _ in range(10)]
        for var in li:  # 这个元素放到几号桶呢？
            # 当it=1的时候，我们放到10位，it=2的时候，我们放到百位
            # 987 it=1 987//10 -> 98  98%10 ->8
            # 取余运算 取第三位的时候 it=3 987//100=9  9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()  # 我们需要将结果写入原列表中，所以清空原列表
        for buc in buckets:
            li.extend(buc)
        # 把数量重新写回li
        it += 1

import random

li = list(range(100000))
random.shuffle(li)
li = radix_sort(li)
print(li)

#****************方法二 *****************

def list_to_buckets(li, base, iteration):
    buckets = [[] for _ in range(base)]
    for number in li:
        digit = (number // (base ** iteration)) % base
        buckets[digit].append(number)
    return buckets

def buckets_to_list(buckets):
    return [x for bucket in buckets for x in bucket]

def radix_sort(li, base=10):
    maxval = max(li)
    it = 0
    while base ** it <= maxval:
        li = buckets_to_list(list_to_buckets(it, base, it))
        it += 1
    return li