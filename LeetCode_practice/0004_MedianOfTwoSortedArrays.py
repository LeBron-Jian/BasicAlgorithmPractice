# _*_coding:utf-8_*_
'''
004：寻找两个正序数组的中位数
题目：
给定两个大小为m和n的正序（从小到大）数组 nums1  和 nums2
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m+n))
你可以假设 Nums1 和  nums2  不能同时为空

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5


'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        这是我最先想到的方法，一次性就写出来了，但是题目难度设置为困难，就让我头疼了。
        需要好好看一下 复杂度的问题。。
        :param nums1:
        :param nums2:
        :return:
        '''
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            ind1, ind2 = int(length / 2 - 1), int(length / 2)
            return (nums1[ind1] + nums1[ind2]) / 2
        if length % 2 == 1:
            ind = length // 2
            return nums1[ind]


'''
参考：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/cong-yi-ban-dao-te-shu-de-fang-fa-dai-ma-jing-jian/
了解题目中说到的 时间复杂度为 O（log(m+n)）的关键点。。。
问题分析：
    题目要求我们找的是中位数，由于中位数存在一个边界情况：
        奇数取中间，偶数取中间两个数除2
        所以我们可以先实现一个找第k个小数的方法
找第k个小数
    对于两个有序数组，我们要找第k小的数
    由于时间复杂度为 log，所以自然而言的想法就是对两个数组每次切一半
    假设我们取两个数组 k/2,位置上的数（暂且不考虑上溢）
    如果 nums1[k/2] >= nums2[k/2] 这意味着 nums2数组的左半边都不需要考虑了
    因为肯定会比第k小的数是要来得小。所以我们可以切掉 nums2数组的一半，如此递归
    每次都能切走一半，自然能达到 O(log(m+n)) 复杂度的要求了。
    在具体的代码实现中，为了方便处理边界情况，我们可以令 nums1 始终是长的那个数组，我们
    可以令 nums1 始终是长的那个数组，然后令 t = min(k/2, len(nums2))便可以防止上溢的发生
'''


def helper(nums1, nums2, k):
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1  # 保持 nums1 比较长
    if len(nums2) == 0:
        return nums1[k - 1]  # 短数组空，直接返回
    if (k == 1):
        return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
    t = min(k // 2, len(nums2))  # 保证不上溢
    if nums1[t - 1] >= nums2[t - 1]:
        return helper(nums1, nums2[t:], k - t)
    else:
        return helper(nums1[t:], nums2, k - t)


'''
找中位数
    为了处理奇偶时候中位数不同的计算方法，这里可以采用一个小技巧
    令 k1 = ( len(nums1) + len(nums2) + 1 ) // 2
    令 k2 = ( len(nums1) + len(nums2) + 2 ) // 2
    对于偶数情况，k1对应中间左边，k2对应中间右边
    对于奇数情况，k1，k2都对应中间
    所以我们得到了获得中位数的统一方法：(helper(k1)+helper(k2))/2
    缺点是：用了两倍的计算量；优点是：代码统一、清晰。

'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        def helper(nums1, nums2, k):  # 本质上是找第k小的数
            if (len(nums1) < len(nums2)):
                nums1, nums2 = nums2, nums1  # 保持 nums1比较长
            if (len(nums2) == 0):
                return nums1[k - 1]  # 短数组空，直接返回
            if (k == 1):
                return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
            t = min(k // 2, len(nums2))  # 保证不上溢
            if (nums1[t - 1] >= nums2[t - 1]):
                return helper(nums1, nums2[t:], k - t)
            else:
                return helper(nums1[t:], nums2, k - t)

        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2
