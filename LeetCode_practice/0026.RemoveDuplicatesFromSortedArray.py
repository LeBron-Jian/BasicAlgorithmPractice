#_*_coding:utf-8_*_
'''
题目：
    26  删除排序数组中的重复项

    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，
    返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并使用O(1)额外空间的条件下完成


示例 1:
    给定数组 nums = [1,1,2], 

    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

    你不需要考虑数组中超出新长度后面的元素。


示例 2:
    给定 nums = [0,0,1,1,1,2,2,3,3,4],

    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

    你不需要考虑数组中超出新长度后面的元素。

说明：
    为什么返回值是整数，但是输出的答案是数组呢？
        请注意：输入数组是以引用的方式传递的，这意味着在函数里修改输入数组
        对于调用者是课件的。
'''

from typing import List


class Solution1:
    def removeDuplicates1(self, nums: List[int]) -> int:
        '''
            双指针
                快慢指针
                快指针与慢指针指向数字相同时，快指针 +1
                快指针与慢指针指向数字不同时，慢指针 +1，且将快指针指向数值
                    赋给慢指针指向的数值
                当快指针长度与数组长度相同时跳出循环，返回慢指针长度+1

            复杂度分析：
                时间复杂度O(n)
                空间复杂度O(1)
        '''
        i, j = 0, 1
        while j<len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i+1

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


nums1 = []
nums = [0,0,1,1,1,2,2,3,3,4]
print('origin nums: ', nums)
print(Solution().removeDuplicates(nums))
print('finally nums: ', nums)
'''
    origin nums:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    5
    finally nums:  [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

'''
