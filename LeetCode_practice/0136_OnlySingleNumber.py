# _*_coding:utf-8_*_
'''
136 只出现一次的数字
题目：
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4

'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


def singleNumber1(nums):
    '''
    这是我最初的想法，使用一次遍历，统计出现的次数，并存放在字典里面
    然后在字典中找，存在出现一次的数字，这个题和LeetCode第一题类似
    字典的键值对分别对应列表的数字，和出现的次数，最后返回出现一次的数字即可
    :param nums:
    :return:
    '''
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] not in dict1:
            dict1[nums[i]] = 1
        else:
            dict1[nums[i]] += 1
    print(dict1)
    print(dict1.values())
    for key, value in dict1.items():
        if value == 1:
            return key


def singleNumber2(nums):
    '''
    上面代码可以优化一下，使用列表生成式方便
    :param nums:
    :return:
    '''
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] not in dict1:
            dict1[nums[i]] = 1
        else:
            dict1[nums[i]] += 1

    count_dict = {value: key for key, value in dict1.items()}
    print(count_dict)
    return count_dict.get(1)


def singleNumber3(nums):
    '''
    可以准备一个列表，遍历数组，当数字不在列表中，加入列表
    如果在列表中，则弹出列表中的该数
    跑一遍后，最后只有出现过奇数次的数字留在列表中，返回该数即可。
    :param nums:
    :return:
    '''
    tmp = []
    # for i in nums:
    #     if i not in tmp:
    #         tmp.append(i)
    #     else:
    #         tmp.remove(i)
    for i in nums:
        if i in tmp:
            tmp.remove(i)
        else:
            tmp.append(i)
    print(tmp)
    return tmp[0]

def singleNumber4(nums):
    '''
    异或运算：0和任何数异或的结果都是这个数本身。。。
    相同的数异或的结果为0
    这个题目中除了一个数只出现一次，其他数都出现了两次。


    交换律： a^b == b^a
    相同数字异或为零：  a^a == 0
    数字异或为该数字：  a^0 == a
    我们可以将数组中所有数字用异或符号连接起来
    则出现偶数次的数字实效，最终结果为出现奇数的数字的异或
    :param nums:
    :return:
    '''
    res = 0
    for num in nums:
        res ^= num
        print(res, num, res ^ num)
    return res

def singleNumber(nums):
    '''
    通过数学的方法
    先通过set把数据去重，然后把所有数值相加*2，减去之前的值，剩下的就是答案
    将数据去重后，我们每个数字只剩下一次。。。。。然后乘以2
    这样上面结果就会均出现两次，我们再减去原来的数据总和
    这样，就剩下单个结果。就是单个数字就暴露出来。
    :param nums:
    :return:
    '''
    res1 = sum(nums)
    res2 = 2*sum(set(nums))
    print(res1, res2)
    return res2-res1

res = singleNumber([5, 5, 6])
print(res)
