#_*_coding:utf-8_*_
'''
  题目 121  买卖股票的最佳时机

  给定一个数组，它的第i个元素是一支给定股票第i天的价格
  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计
  一个算法来计算你所能获得的最大利润。

  注意：你不能再买入股票前卖出股票

示例 1:
  输入: [7,1,5,3,6,4]
  输出: 5
  解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
       注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
  输入: [7,6,4,3,1]
  输出: 0
  解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
          暴力解法

          暴力解法固然可以解决问题，但是时间复杂度就爆炸了
          时间复杂度为：O(mn)
          空间复杂度为：O(1)
        '''
        maxprofit = 0
        for i in range(len(prices)):
          for j in range(i, len(prices)):
            tmp = prices[j] - prices[i]
            if  tmp>0 and tmp > maxprofit:
              maxprofit = tmp
        return maxprofit

    def maxProfit1(self, prices: List[int]) -> int:
      '''
        时间复杂度为O(n)
        空间复杂度为O(1)
      '''
      if len(prices) < 2:
        return 0
      minprice = prices[0]
      maxprofit = prices[1] - minprice
      for i in range(1, len(prices)-1):
        if prices < minprice:
          minprice = prices
        if prices[i+1]-minprice > maxprofit:
          maxprofit = prices[i+1]-minprice
      return maxprofit if maxprofit>0 else 0


    def maxProfit2(self, prices: List[int]) -> int:
      '''
        是上面例子的改写，只不过这里使用了库函数
      '''
      minprice, maxprofit = 1e9, 0
      for price in prices:
        maxprofit = max(price-maxprofit, maxprofit)
        minprice = min(minprice, price)

      return maxprofit


    def maxProfit3(self, prices: List[int]) -> int:
      '''
        动态规划：
          时间复杂度为O(n)
          空间复杂度为O(n)
      '''
      n = len(prices)
      if n == 0:
        return 0
      dp = [0]*n
      minprice = prices[0]
      for i in range(1, n):
        minprice = min(minprice, prices[i])
        dp[i] = max(dp[i-1], prices[i]-minprice)
      return dp[-1]


prices = [7,1,5,3,6,4]   # [7,6,4,3,1]
print(Solution().maxProfit1(prices))
