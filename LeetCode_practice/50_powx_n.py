#_*_coding:utf-8_*_
'''
题目：
    剑指offer 50   pow(x, n)

    实现  pow(x, n) ，即计算 x 的 n 次幂函数 即(x**n)


示例 1：
    输入：x = 2.00000, n = 10
    输出：1024.00000

示例 2：
    输入：x = 2.10000, n = 3
    输出：9.26100

示例 3：
    输入：x = 2.00000, n = -2
    输出：0.25000
    解释：2-2 = 1/22 = 1/4 = 0.25
 

提示：
    -100.0 < x < 100.0
    -231 <= n <= 231-1
    -104 <= xn <= 104



'''
class Solution:
    import math
    def myPow1(self, x: float, n: int) -> float:
        '''
            最简单的API求解，面试官肯定不想要
        '''
        return math.pow(x, n)

    def myPow2(self, x: float, n: int) -> float:
        return x**n

    def myPow3(self, x: float, n: int) -> float:
        '''
            暴力求解法，既然是 n 个元素连乘，就直接遍历循环 n 次进行求解
            但是这种循环，时间复杂度为O(n)

            但是会超时。。。。
        '''
        res = 1
        if n<0:
            return 1/self.myPow3(x, -n)
        for i in range(n):
            res = res*x
        return  res

    def myPow4(self, x, n):
        '''
            如果 n 是偶数，我们将 n 折半，底数变为 x^2
            如果 n 是奇数， 我们将 n 减去 1 ，底数不变，得到的结果再乘上底数 x
        '''
        res = 1
        if n < 0:
            x, n = 1/x, -n
        # 通过折半计算，每次把 n 减半，降低时间复杂度
        while n:
            if n%2 == 0:
                x *= x
                n /=2
            else:
                res *=x
                n -= 1
        return res
