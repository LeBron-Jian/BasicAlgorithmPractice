#_*_coding:utf-8_*_
'''
题目：
    剑指offer 63  股票的最大利润
    
    假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次
    可能获得的最大利润是多少？

示例 1:
    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
         注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


限制：
    0 <= 数组长度 <= 10000
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            时间复杂度为：O(n)
            空间复杂度为：O(1)
        '''
        if len(prices) < 2:
            return 0
        minnum = prices[0]
        maxprofit = prices[1] - minnum
        for i in range(1, len(prices)-1):
            if prices[i] < minnum:
                minnum = prices[i]
            if maxprofit < (prices[i+1] - minnum):
                maxprofit = prices[i+1] - minnum
        return maxprofit if maxprofit > 0 else 0
        


class Soultion1:
    def maxProfit(self, prices):
        '''
            现在可能进化了，第一个都想不起暴力法了。

            下面写一下暴力法解决：
            解决方案：
                我们需要找出给定数组中两个数字之间的最大差值（即最大利润），此外第二个数字
                即卖出价格必须大于第一个数字买入价格。

                形式上，对于每组i和j（其中 j>i） 我们需要找到  max(price[j]) - prices[i]

            时间复杂度：O(n**2)
            空间复杂度：O(1) 只使用了常数个变量
        '''
        ans = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans


class Soultion2:
    def maxProfit(self, prices):
        '''
            我们遍历一次价格数组，记录历史最低点，然后考虑在最低点买入，我们统计最大值，就得到了答案
            其实这个解法和我第一个解法类似，只不过我自己做了判断
            这里使用了max，min函数

            时间复杂度：O(n)
            空间复杂度：O(1) 只使用了常数个变量
        '''
        inf = int(1e9)
        minprice, maxprofit = inf, 0
        for price in prices:
            maxprofit = max(price-minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


class Soultion3:
    def maxProfit(self, prices):
        '''
            股票问题一共有六道，买卖股票的最佳时机（1,2,3,4,），含冷冻期，含手续费
            本题是第一道，输入入门题目

            股票问题的方法就是动态规划，因为它包含了重叠子问题，即买卖股票的最佳时机是由
            之前买或不买的状态决定的，而之前买或不买又由更早的状态决定的。

            由于本题只有一次交易（买入卖出），所以除了动态规划，我们还可以使用其他方法实现

            这里学习动态规划

            动态规划一般分为一维，二维，多维（使用状态压缩），对应形式为：
                        dp[i]  dp[i][j]  dp[i][j]

            动态规划做题步骤：
            1，明确dp[i] 应该表示什么
            2，根据dp[i]和 dp[i-1]的关系得到状态转移方程
            3，确定初始条件，如dp[0]

            其实第一个解法就是由动态规划的思想演变而来

            时间复杂度为：O(n)
            空间复杂度为：O(n)
        '''
        n = len(prices)
        if n == 0:
            return 0  # 边界条件，这里统一返回0，我之前写的None，报错。。
        dp = [0]*n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)
        return dp[-1]


# print(Solution().maxProfit(prices=[7,1,5,3,6,4]))

