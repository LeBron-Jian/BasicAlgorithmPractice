#_*_coding:utf-8_*_
'''
题目：
    剑指offer 39  数组中出现次数超过一半的数字

    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素
    

示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2


限制：
    0 <= 数组长度 <= 10000
'''

from typing import List
import collections

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            我的思路是首先统计出现的次数，然后通过哈希表去找对应的大于数组长度一半的数字

            这个应该算是哈希表统计法
            通过哈希映射来存储每个元素以及出现的次数，对于哈希映射中的每个键值对，键表示
            一个元素，值表示该元素出现的次数。

            我们使用一个循环遍历数组 nums 并将数组中的每个元素加入哈希映射中，在这之后，我们
            遍历哈希映射中所有的键值对，返回值为最大的键。

            时间复杂度为O(n)
            空间复杂度为O(n)
        '''
        res = {}
        for num in nums:
            if num in res.keys():
                res[num] +=1
            else:
                res[num] = 1
        for key, value in res.items():
            if value > len(nums)/2:
                return key

    def majorityElement1(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            数组排序法，将数组 nums 排序，数组中点的元素一定为众数

            如果将数组 nums 中所有元素按照单调递增或单调递减的顺序排序，那么下标为中间
            的元素一定是众数。

            对于这种算法，我们先将 nums 数组排序，然后返回上文所说中的下标对应的元素
            考虑一种情况：
                当n为奇数时候： 中位数一般为 中间的一个数
                当n为偶数时候： 中位数一般为 中间的两个数

            对于每种情况，众数都在中间，所以无论众数是多少，返回第一个中间的数都是对的

            复杂度分析：
                时间复杂度为 O(nlogn)
                空间复杂度为 O(logn)
                    如果使用语言自带排序算法，则使用O(logn)的栈空间
                    如果自己编写堆排序，则只需要使用O(1)的额外空间
        '''
        nums.sort()
        return nums[len(nums)//2]


class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            摩尔投票法 核心理念为票数正负抵消。此方法时间复杂度为O(N)，空间复杂度为O(1)
            为本题的最佳解法

            思路：
                推论1：若记众数的票数为+1，非众数的票数为-1，则一定有所有数字的票数和>0
                推论2：若数组的前a个数字的票数和=0，则数组剩余（n-a）个数字的票数和一定
                        仍然>0，即后（n-a)个数字的众数仍然为x

                根据以上推理，假设数组首个元素n1为众数，遍历并统计票数，当发生票数和=0时
                剩余数组的众数一定不变，这是由于：
                    当n1=x：抵消的所有数字，有一半是众数x
                    当n1!=x：抵消的所有数字，少于或等于一半是众数x
                利用此特性，每轮假设发生票数和=0 都可以缩小剩余数组区间，当遍历完成时，最后
                一轮假设的数字记为众数

            算法流程：
                1，初始化，票数统计 votes=0，众数x
                2，循环：
                    遍历数组nums中的每个数字num：
                        1，票数 votes=0，则假设当前数字 num 是众数
                        2，当 num=x时，票数 votes自增1，当num !=x，票数votes自减1
                3，返回x即可
        '''
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes +=1
            else:
                votes -=1
        return x

    def majorityElement1(self, nums: List[int]) -> int:
        '''
            由于题目说明：给定的数组总是存在多数元素，因此本题不用考虑数组不存在众数的情况
            若考虑，则需要加入一个验证环节，即遍历数组nums统计x的数量
                若x的数量超过数组长度的一半，则返回x
                否则返回未找到众数

            这样做后，时间复杂度与空间复杂度不变仍然为O(n)和O(1)
        '''
        votes, count = 0, 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        # 验证x是否为众数
        for num in nums:
            if num == x:
                count +=1
        # 当无众数时返回0
        return x if count > len(nums)//2 else 0

nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# res = {}
# for num in nums:
#     if num in res.keys():
#         res[num] += 1
#     else:
#         res[num] = 1
# print(res)
# for key, value in res.items():
#     if value > len(nums)/2:
#         print(key)

# counts = collections.Counter(nums)
# print(counts)
# print(counts.keys())
# print(max(counts.keys(), key=counts.get))

