#_*_coding:utf-8_*_
'''
题目：  剑指offer 53——1  在排序数组中查找数字 I

    统计一个数字在排序数组中出现的次数

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2

示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0
 

限制：
    0 <= 数组长度 <= 50000

 

'''
from typing import List

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        '''
            我的初次想法，找一个字典，先把list里面的次数统计出来，再通过target找
        '''
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num] +=1
            else:
                temp_dict[num] = 1
        for i in temp_dict.keys():
            if target == i:
                return temp_dict[i]
            
        return 0

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        '''
            双指针解法，从两边往中间遍历
        '''
        i, j = 0, len(nums)-1
        if target not in nums:
            return 0
        # while nums[i] != target or nums[j] != target:
        while nums[i] != nums[j] :
            if nums[i] != target:
                i+=1
            if nums[j] != target:
                j -= 1
        return j-i+1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            双指针法 根据排序数组，我们可以使用二分法分别找到左边界left和右边界right
            此数字数量为 right-left-1

            算法解析：
                1，初始化：左边界，右边界
                2，循环二分：当闭区间[i, j]无元素时跳出
                    1，计算中点 m=(i+j)/2  向下取整
                    2，若 nums[m] < target ，则target在闭区间 [m+1, j] 中，
                        则执行 i=m+1
                    3，若 nums[m] > target，则target在闭区间 [i, j+m]中，
                        则执行 j =m-1
                    4，若 muns[m] = target，则右边界right在闭区间[m+1, j]中
                        左边界left在闭区间 [i, m-1]，因此可以分为以下两种情况
                            1，查找右边界right，则执行 i=m+1  
                            2，查找左边界left，则执行 j=m-1
                            （跳出时，i,j 指向左边界，右边界）
                3，返回值，应用两次二分，分别查找right和left，最终返回right-left-1


            复杂度分析：时间复杂度O(logN)
                       空间复杂度O(1)
        '''
        i, j = 0, len(nums)-1
        while i<=j:
            m = (i+j)//2
            if nums[m] <= target:
                i = m+1
            else:
                j = m-1
        right =i
        if j>=0 and nums[j] != target:
            return 0
        i = 0
        while i<=j:
            m = (i+j)//2
            if nums[m] < target:
                i = m+1
            else:
                j = m-1
        left = j
        return right-left-1


nums = [5,7,7,8,8,10]
target = 8
res = Solution()
print(res.search(nums, target))
