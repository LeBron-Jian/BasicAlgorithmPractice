#_*_coding:utf-8_*_
'''
题目：
        122   买卖股票的最好时机

    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出,
            这笔交易所能获得利润 = 5-1 = 4 。随后，在第 4 天（股票价格 = 3）的时候买入，
            在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
    输入: [1,2,3,4,5]
    输出: 4
    解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出,
          这笔交易所能获得利润 = 5-1 = 4 。
         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''
from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        '''
            贪心
        股票买卖策略
            单独交易日：设今天价格为p1，明天价格为p2，则今天买入，明天卖出
                可赚取金额p2-p1（负值代表亏损）
            连续上涨交易日：设此上涨交易日股票价格分别为p1, p2, pn，则第一
                天买最后一天卖收益最大，即 pn-p1,；等价于每天都买卖，即
                pn-p1 = p2-p1 + p3-p3+...+pn-pn-1
            连续下降交易日：则不买卖收益最大，即不会亏钱

        算法流程：
            遍历整个股票交易日价格列表price，策略是所有上涨交易日都买卖（转到
            所有的利润），所有下降交易日都不买卖（永不亏钱）

            1，设tmp为第 i-1 日买入与第 i 日卖出赚取的利润，
            2，当该天利润为正 tmp>0，则将利润加入总利润profit，当利润为0或
                利润为负，则直接跳过
            3，遍历完成后，返回总利润 profit

        复杂度分析：
            时间复杂度：O(n)  只遍历一次prices
            空间复杂度：O(1)  遍历使用常数额外的空间
        :param prices:
        :return:
        '''
        maxprofit = 0
        for i in range(i, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp>0:
                maxprofit += tmp
        return maxprofit

    def maxProfit2(self, prices: List[int]) -> int:
        '''
            动态规划
        我们思考用什么状态描述每个点。对于day i 要么持有股票，要么手里没股票
        因为不能同时参与多笔交易，那么当天交易完成后，手里持有股票直接能是0支
        或者1支。
            dp[i][0] 表示：第i天手里没股票，至今（第i天）的最大收益
            day i 手里没股票，有两种可能：
                昨天也没持有股票：dp[i-1][0]
                昨天买了股票，今天卖了：dp[i-1][1] + prices[i]
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] 表示：第i天手里有股票，至今（第i天）的最大收益
            day i 手里有股票，有两种可能：
                昨天也有股票：dp[i-1][1]
                昨天卖了，今天买了：dp[i-1][0] - prices[i]
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            目标是求出：dp[prices.length-1][0] 和 dp[prices.length-1][1]的较大者
                前者肯定 》= 后者， 求 dp[prices.length-1][0]
        定义状态：
            base case:
                day0 没买，不持有股票，day0无交易： dp[0][0] = 0
                day0 买了，持有股票，但是day1将其卖出，获取利润： dp[0][1] = -prices[0]

        复杂度分析：
            时间复杂度：O(n)  只遍历一次prices
            空间复杂度：O(n)  
        '''
        if len(prices) <2:
            return 0
        dp = [[0, 0]]*len(prices)
        # 0表示交易完成后手里不持有股票的最大金额数；1表示完成交易后手里持有股票的最大金额数
        dp[0][0], dp[0][1] = 0, -prices[0]
        
        for i in range(1, len(prices)):
            # 状态转移
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[len(prices)-1][0]


    def maxProfit3(self, prices: List[int]) -> int:
        '''
            对上面动态规划进行优化
            我们可以发现当前的状态只与前一天的状态值有关，那么这个可以优化
            用两个变量来存储前一天的状态，用以计算后一天的状态值，然后取维护
            更新这两个变量
        '''
        if len(prices) < 2:
            return 0
        dp0, dp1 = 0, -prices[0]
        for i in range(1, len(prices)):
            # 这里维护更新两个变量
            # 其中dp1需要用到前一天dp0的值，但是dp0还会变换，这里tmp先进行暂存
            tmp = dp0
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, tmp-prices[i])
        return dp0



prices =  [7,6,4,3,1]  # [7,1,5,3,6,4]
print(Solution().maxProfit2(prices))
