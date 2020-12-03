#_*_coding:utf-8_*_
'''
    剑指offer  57_1   和为s的两个数字

    输入一个递增排序的数组和一个数字 s， 在数组中查找两个数，使得
    他们的和正好是 s，如果有多对数字的和等于 s，则输出任意一对即可。


示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[2,7] 或者 [7,2]

示例 2：
    输入：nums = [10,26,30,31,47,60], target = 40
    输出：[10,30] 或者 [30,10]
 

限制：
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6


'''
from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        '''
            因为它是一个递增排序的数组，所以我考虑从两边开始找，这样效率会高一些

            复杂度分析：
                时间复杂度：O(n) n为数组nums的长度，双指针共同遍历整个数组
                空间复杂度：O(1) 变量 i, j 使用常数大小的额外空间
        '''
        i, j = 0, len(nums)-1
        while i<j:
            tmp = nums[i] + nums[j]
            if target < tmp:
                j -= 1
            elif target > tmp:
                i += 1
            else:
                return [nums[i], nums[j]]
        return None
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        '''
            对上面版本进行修改，考虑到溢出问题，
            这里将判断条件改成 target-nums[i] 与 nums[j] 相比较
            严格来说，这样不会越界
        '''
        i, j = 0, len(nums)-1
        while i<j:
            if target-nums[i] < nums[j]:
                i += 1
            elif target-nums[i] > nums[j]:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return None


    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        '''
            哈希表 设一个空的哈希表hash
            如果
        '''
        tmp = {}
        for num in nums:
            if num not in tmp:
                tmp[target-num] = num
                print(tmp)
            else:
                return [num, tmp[num]]

        return None




# nums = [2,7,11,15]   
# target = 9
# [2,7]

nums = [16,16,18,24,30,32]
target = 48
# [16,32]

print(Solution().twoSum3(nums, target))

a = {1:'21', 2:'saa'}
for i in a:
    print(i)
