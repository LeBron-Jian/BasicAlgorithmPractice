#_*_coding:utf-8_*_
'''
题目：
    剑指offer 42 连续子数组的最大和

    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组，求所有子数组的和的最大值

    要求时间复杂度为O(n)


示例1:
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
     

提示：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100

'''
from typing import List

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        '''
            一开始，打算使用暴力搜索，但是其时间复杂度肯定为O(n**2)
            当然还有动态规划

            动态规划解析：
                1，状态定义：设动态规划列表dp，dp[i] 代表以元素 nums[i] 为结尾
                            的连续子数组最大和。
                            为什么定义最大和 dp[i] 必须包含元素 nums[i]：我们需要
                            保证 dp[i] 递推到 dp[i+1] 的正确性，如果不包含 nums[i]
                            递推时则不满足题目的 连续子数组要求

                2，转移方程：若dp[i-1] <= 0 ,说明 dp[i-1] 对 dp[i] 产生负贡献，即
                            dp[i-1] + nums[i] 还不如 nums[i] 本身大。

                            当 dp[i-1]>0：执行 dp[i] = dp[i-1] + nums[i]
                            当 dp[i-1]<=0：执行 dp[i] = nums[i]

                3，初始状态：dp[0] = nums[0]:即以nums[0]结尾的连续子数组最大和为nums[0]

                4，返回值：返回dp列表中的最大值，代表全局最大值
        '''

        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        # 动态规划，原地修改，和上面一样
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            res = max(res, nums[i])

        return res

    def maxSubArray(self, nums: List[int]) -> int:
        '''
            前缀和，如果之前的值小于0，那么从当前位置重新计算前缀和
            需要两个变量，temp记录前缀和的最大值，res记录结果

            时间复杂度为O(n)
            空间复杂度为O(1)
        '''

        # tmp, res = float('-inf'),float('-inf')
        tmp, res = 0, 0
        for i in nums:
            tmp = max(i, tmp + i)
            res = max(res, tmp)
        return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
print(Solution().maxSubArray(nums=[1,2,3]))
