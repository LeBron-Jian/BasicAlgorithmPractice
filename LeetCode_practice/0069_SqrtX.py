# _*_coding:utf-8_*_
'''
69：x的平方根
题目：
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        我投机取巧，直接使用math这个函数库，直接求出函数，并取整
        :param x:
        :return:
        '''
        res = int(math.sqrt(int(x)))
        return res

    def mySqrt1(self, x: int) -> int:
        '''
        当不知道math函数库的时候，我们可以使用二分法搜索平方根
        类似于猜价格，高了就往低猜，低了就往高猜，范围越来越小
        所以使用二分法猜算术平方根就很自然。一个数的平方根肯定
        不会超过他自己，但是我们知道，一个数的平方根最多不会超过他的一半
        所以，此平方根肯定大于0小于他们的一半。
        " / "  表示浮点数除法，返回浮点结果;
        " // " 表示整数除法,返回不大于结果的一个最大的整数
        :param x:
        :return:
        '''
        left = 0
        right = x // 2 + 1
        while left < right:
            # 这里一定取右中位数，如果取左中位数可能进入死循环
            mid = left + (right-left+1)//2
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left
