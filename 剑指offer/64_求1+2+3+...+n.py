#_*_coding:utf-8_*_
'''
题目：
    剑指offer 64  求1+2+3+...+n

    求1+2+3+...+n 要求不能使用乘除法，for, while if else swith case 等关键字
    及条件判断语句（A？B:C）


示例 1：
    输入: n = 3
    输出: 6


示例 2：
    输入: n = 9
    输出: 45


限制：
    0 <= n <= 10000
'''
from typing import List

class Solution:
    def sumNums(self, n: int) -> int:
        '''
            迭代
            这里先写了for循环，怕自己不会。。。。

        '''
        res = 0
        for i in range(n):
            res += (i+1)
        return res


class Solution:
    def sumNums(self, n: int) -> int:
        '''
            平均计算
            此计算必须使用乘除法，因此本方法不可取，直接排除
        '''
        return (1+n)*n//2



class Solution(object):
    def sumNums(self, n):
        '''
                方法1：递归
                难点就是终止条件需要判断，即需要加if
                所以本方法不可取。

                如果不用if等判断语句外，用其他方法终止递归，就可以用了
        '''
        if n ==1:
            return 1
        n += self.sumNums(n-1)
        return n

    def __init__(self):
        self.res = 0

    def sumNums1(self, n):
        '''
           下面考虑逻辑运算符
            即考虑将if判断 替换掉，我们就可以使用递归了。
            难点在于 如果通过逻辑运算符 替换 if n==1这个语句

            时间复杂度O(n) 计算 N+(N-1)+...+1 需要开启 n个递归函数
            空间复杂度O(n) 递归深层达到n，系统使用O(n) 大小的额外空间

            if A & B：若A为False，则不会执行判断B   即与运算& 短路
            if A || B：若A为True，则不会判断B，即或运算||， 短路

            所以我们施行 n=1时候，通过短路效应实现
            
        '''
        n >1 and self.sumNums(n-1)
        self.res +=n
        return self.res
