#_*_coding:utf-8_*_
'''
题目：
    剑指offer 53_2  0~n-1 中缺失的数字

    一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1中
    在范围 0~n-1内的 n 个数字中有且只有一个数字不再该数组中，请找出这个数字。


示例 1:
    输入: [0,1,3]
    输出: 2

示例 2:
    输入: [0,1,2,3,4,5,6,7,9]
    输出: 8

示例 3：
    输入：[0]
    输出：1

限制：

1 <= 数组长度 <= 10000


'''
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            最简单的就是顺序查找了，但是顺序查找肯定忽略了题目给出的递增排序数组了，
            不过还是写一下
    
            但是最重要的是  一定要防止缺失值是最后一个，不然。。。
        '''
        # 防止缺失的是最后一个
        # nums.append(len(nums)+1)
        for i in range(len(nums)+1):
            if i != nums[i]:
                return i

        return len(nums)


    def missingNumber1(self, nums: List[int]) -> int:    
        '''
            网上看的骚操作
        '''
        # return sum(range(len(nums) + 1)) - sum(nums)
        return len(nums)*len(nums+1)//2 - sum(nums)


    def missingNumber2(self, nums: List[int]) -> int:    
        '''
            下面看正规解法，既然题目中提到了递增排序数组，
            那么肯定二分法是我最先考虑的

                根据题意，我们可以将数组划分为左右两个数组
                    其中：右数组： nums[i] = i  左数组： nums[i] = i
                确实的数字等于 右子数组的首位元素 对应的索引

                注意：循环二分 i<=j 的意思是：闭区间为空时，

            复杂度分析：
                时间复杂度：O(logN)  二分法为对数级别复杂度
                空间复杂度：O(1)   几个变量使用常数大小的额外空间
        '''
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == mid:
                left = mid +1
            else:
                right = mid -1
        return left
