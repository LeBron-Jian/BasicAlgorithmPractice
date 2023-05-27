#_*_coding:utf-8_*_
'''
题目：
    剑指offer 3  数组中重复的数字
    
    找出数组中重复的数字

    在一个长度为n的数组 nums里的所有数字都在0~n-1的范围内，数组中某些数字是重复的
    但不知道有几个数字重复了，也不知道每个数组重复了几次，请找出数组中任意重复的数字

示例：
    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3 

限制：
2 <= n <= 100000

'''

from typing import List
# Definition for a binary tree node.
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        '''
        找到任意个重复的数组即可，首先可以暴力遍历
        但是暴力遍历肯定会存在内存溢出的问题，即超时
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

    def findRepeatNumber1(self, nums: List[int]) -> int:
        '''
            暴力遍历肯定不可取，
            下面想新的办法
            由于只需要找到数组中任意一个重复的数字，因此遍历数组，遇到重复的数字即返回
            为了判断一个数字是否重复遇到，使用列表存储已经遇到的数字，如果遇到数字已经在
            列表里面，则当前数字是重复数字

                初始化列表为空列表
                遍历数组中每个元素
                    判断是否在此列表中，如果存在则退出，并结束遍历，如果不存在则加入

            时间复杂度：
                O(n)  遍历一次数组，所以为O(n)
            空间复杂度：
                O(n)：不重复的每个元素都可能存在集合，因此占用O(n)的额外空间
        '''
        res = []
        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else:
                return nums[i]
            

    def findRepeatNumber2(self, nums: List[int]) -> int:
        '''
            还可以继续减少空间复杂度，即原地置换
            
            为什么呢？ 题目说 在一个长度为n的数组nums里，所有数都在0~n-1范围内，说明数组元素的索引和值是一对多关系
            因此可以遍历数组并交换操作，使元素的索引与值一一对应即可。

            思路：
                如果没有重复的数字，那么正常排序后，数字i应该在下标为i的位置，所以思路是重头扫描数字
                遇到下标为i的数字，如果不是i的话，我们可以做一个标记

                也就是说遍历中，第一次遇到数字x时，将其交换到索引x处，当第二次遇到数字x时，一定有 nums[x] = x
                此时即可得到一组重复数字

            算法流程：
                1，遍历数组nums，设索引初始值为 i=0
                    1，若 nums[i] = i，说明此数字已经在对应索引位置，无需交换，因此跳过
                    2，若 nums[nums[i]] = nums[i] ，代表索引 nums[i] 除和索引i处的元素值都为 nums[i]，
                        即找到一组重复值，返回此值 nums[i]
                    3，否则：交换索引为i和nums[i]的元素值，将此数字交换至对应索引位置
                2，若遍历完毕尚未返回，则返回 -1

            时间复杂度：O(n)
            空间复杂度：O(1)

            在Python中 a,b = c, d 操作原理是先暂存元组(c, d)，然后按照左右顺序复制给a,b
        '''
        i= 0
        while i< len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            # 如果索引与开始元素不相等则，交换索引与开始元素，将元素放到应该放的地方
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


    def findRepeatNumber3(self, nums: List[int]) -> int:
        '''
            排序做法：
                时间复杂度为：O(nlogn)
                空间复杂度为：O(1)
        '''
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre
            pre = nums[i]


a = [0, 1,2,3,4,5]
print(a[0], a[a[0]])
        
