# _*_coding:utf-8_*_
'''
面试题17.04：消失的数字
题目：
数组 nums 包含从 0 到 n 的所有整数，但其中缺了一个。
请编写代码找出缺失的那个数字，你有办法在O(n)时间内完成吗

示例 1：
输入：[3,0,1]
输出：2

示例 2：
输入：[9,6,4,2,3,5,7,0,1]
输出：8

示例3：
输入：[1]
输出：0

示例4：
输入：[0]
输出：1

示例5：
输入：[0,1]
输出：2
'''

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        我的想法是 在数组中找到最小值，然后找到最大值
        然后通过位运算，找出那个缺失的值
        :param nums:
        :return:
        '''


def missingNumber1(nums):
    '''
    越做越错，很多不对的
    从新审题，我发现是数组 nums 包含从 0 到 n 的所有整数
    所以不需要找到最小值，最小值一直是零。。。而且找最大值好像没有用处
    我们要找的是长度+1，然后里面缺一个数
    :param nums:
    :return:
    '''
    # max_num = max(nums)
    # print(max_num)
    # res1 = [i for i in range(max_num)]
    # 这种看似是对的但是会出问题，就是当输入[0] 的时候，输出为0，但是预期输出为1.
    # 这种方法有问题，但是我还是希望留在这里，不过我这里的目的不是这个，
    # 是希望通过位运算来计算。
    # return sum(res1) - sum(nums)
    res1 = [i for i in range(len(nums)+1)]
    print(res1, nums)
    # 这样后可以直接使用sum函数，找到那个单的。这里不这样做
    res1.extend(nums)
    print(res1)
    bit = 0
    for i in res1:
        bit ^= i
    return bit


def missingNumber2(nums):
    '''
    本来求和值：sum(range(len(nums)+1))
    输入求和值：sum(nums)
    缺失值：sum(range(len(nums)+1)) - sum(nums)
    :param nums:
    :return:
    '''
    return sum(range(len(nums) + 1)) - sum(nums)


nums1 = [3, 0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums2 = [0]
res = missingNumber1(nums2)
print(res)

'''
注意这里算是等差数列求和。
等差数列的求和性质：和＝（首项＋末项）* 项数 ÷ 2
这里就是等差数列求和，然后减去集合总和就可以知道丢失的数据
'''

def missingNumber3(nums):
    '''
    之前的也可以，只是想寻找新的方法，寻找新的思路
    :param nums:
    :return:
    '''
    n = len(nums)
    return (n*(n+1))//2 - sum(nums)
