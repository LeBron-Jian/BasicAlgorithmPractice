# _*_coding:utf-8_*_
'''
949：给定数字能组成的最大时间
题目：
    给定一个由4位数字组成的数组，返回可以设置的符合24小时制的最大时间
    最小的 24 小时制时间是 00:00，而最大的是 23:59
    从00:00（午夜）开始算起，过得越久，时间越大
    以长度为5的字符串返回答案，如果不能确定有效时间，则返回空字符串

示例1：
    输入：[1,2,3,4]
    输出："23:41"

示例2：
    输入：[5,5,5,5]
    输出：""

提示：
    A.length == 4
    0 <= A[i] <= 9
'''
from typing import List
import itertools


class Solution1:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        '''
        四个数字的不同排列方法
        要求前两个数字构成的数字在0~23之间
        要求后两个数字构成的数字在0~59之间
        比较大小就是比较 时，再比较 分
        执行用时：
            36 ms, 在所有 Python3 提交中击败了94.10%的用户
        内存消耗：
            13.7 MB, 在所有 Python3 提交中击败了54.55%的用户
        :param A:
        :return:
        '''
        A.sort(reverse=True)  # 对A排序
        p = itertools.permutations(A)  # 对A进行排列组合
        for a, b, c, d in p:  # 遍历找到第一个小于 23:59的数
            if a * 10 + b < 24 and c * 10 + d < 60:
                return str(a) + str(b) + ':' + str(c) + str(d)
        return ''


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        '''
        我的暴力穷举
        遍历所有可能的时间，找到最大的那个
        算法：使用（i, j, k, l)表示（0， 1， 2， 3）,之后做全排列，对于每个排列，会有A[i]A[j]: A[k]A[l]
        检查每个排列对应的时间是否合法，例如检查 10*A[i]+A[j] 是否小于24,10*A[k]+A[l] 是否小于60
        最后把最大的有效时间输出就可以了。

        遍历这四个数字所有排列的可能，判断是不是一个合法的时间，如果合法且比目前存在的
        最大时间更大，就更新这个最大时间。

        执行用时：
            40 ms, 在所有 Python3 提交中击败了79.94%的用户
        内存消耗：
            13.7 MB, 在所有 Python3 提交中击败了45.45%的用户

        时间复杂度为 O(1)   空间复杂度为 O(1)
        :param A:
        :return:
        '''
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            time = hours * 60 + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time
        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ''


print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
