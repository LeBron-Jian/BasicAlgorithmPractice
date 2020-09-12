# _*_coding:utf-8_*_
'''
283：移动零
题目：
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序

示例：
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]

说明：
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


def moveZeroes1(nums):
    '''
    类比于快速排序，设置一个指针用于遍历，一个指针pos用于指示最左边的0的位置
    pos作为枢纽，所以i遍历到的非0，都弄到pos左边去
    （用交换的方式，然后pos++，保证pos指的仍然是最左边0的位置
    遍历到的0都弄到pos右边）
    因为i本身比pos快，所以我们这里不做任何事就可以达到目的
    :param nums:
    :return:
    '''
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    return nums


def moveZeroes(nums):
    """
        快慢指针，快指针不断往后遍历，找到不为0的数
        一旦找到，就把该值赋予慢指针所在的位置，然后慢指针往后走一格
        这样就保证慢指针前面全是零，等快指针遍历完后，那么直接把满指针之后的都赋予0即可
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums


nums = [6, 1, 0, 3, 12]
print(moveZeroes(nums))
# [6, 1, 3, 12, 0]

