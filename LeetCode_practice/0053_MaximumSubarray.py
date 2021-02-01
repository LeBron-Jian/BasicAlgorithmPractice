# _*_coding:utf-8_*_
'''
题目： 53  最大自序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组
    （子数组最少包含一个元素），返回其最大和。

示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
    如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        result = nums[0]
        while i < l:
            sums = []
            temp = 0
            for j in range(i, l):
                temp += nums[j]
                sums.append(temp)
            if result < max(sums):
                result = max(sums)
            i+=1
        return result

    def maxSubArray2(self, nums: List[int]) -> int:
        '''
        暴力解法就是遍历一遍，使用两个遍历，一个记录最大的和，一个记录当前的和
        :param nums:
        :return:
        '''
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列加上此时的元素的值大于 tmp的值
            # 说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当当前序列加上此时的元素小于下一个元素的时候，当前最常序列到此为止
                # 以钙元素为起点继续找最大子序列
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_

    def maxSubArray3(self, nums: List[int]) -> int:
        sum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0:
                sum = 0
        return MaxSum

    def maxSubArray4(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            subMaxSum = max(nums[i]+nums[i-1], nums[i])
            # 将当前和最大的赋给 nums[i]， 新的nums 存储的为何值
            nums[i] = subMaxSum
        return max(nums)

    def maxSubArray5(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)