# _*_coding:utf-8_*_
'''
486 预测赢家
题目：
    给定一个表示分数的非负整数数组，玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端
拿取分数，然后玩家1拿，.......。
    每次一个玩家只能拿一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束，最终获得分数
总和最多的玩家获胜。
    给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化

示例1：
输入：[1, 5, 2]
输出：False
解释：一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。

示例2：
输入：[1, 5, 233, 7]
输出：True
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。

提示：
    1 <= 给定的数组长度 <= 20.
    数组里所有分数都为非负数且不会大于 10000000 。
    如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。

'''

from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        pass


def PredictTheWinner1(nums):
    '''
    最初想到的就是递归 给两个指针，如果左边大，则左边给玩家1，否则右边给
    然后左边大，给玩家2，否则右边给，
    然后继续循环。。。
    笨方法。。。。

    如果这样简单就好了，这个题恶心的一点不在这里。。。
    在继续看下面的，就是不止能看到眼前，还要看到未来，
    就是示例2必须看懂。可以为了下一个大数字，故意选一个小的，所以我这个方法有误
    需要改进。。。。
    :param nums:
    :return:
    '''
    i, j, res1, res2 = 0, len(nums) - 1, 0, 0
    while i < j:
        if nums[i] > nums[j]:  # 左边比右边大
            res1 += nums[i]
            if nums[i + 1] > nums[j]:  # 玩家1取了后，左边比右边大，玩家2取
                res2 += nums[i + 1]
                i += 2
            else:
                res2 += nums[j]
                i += 1
                j -= 1
        else:  # nums[i] < nums[j]
            res1 += nums[j]
            if nums[j - 1] > nums[i]:  # 玩家1取了后，右边比左边大，玩家2取
                res2 += nums[j - 1]
                j -= 2
            else:
                res2 += nums[i]
                i += 1
                j -= 1
    return res1 >= res2


def PredictTheWinner2(nums):
    '''
    改进：官方解答
    为了判断那个玩家可以获胜，需要计算一个总分，即先手得分和后手得分之差，当数组中所有数字都被
    拿走时，如果总分大于或等于0，则先手获胜，反之后手获胜
    计算总分时，需要记录当前玩家是先手还是后手，判断当前玩家的得分应该记为正还是负
    当数组中剩下的数字多于11个时，当前玩家会选择最优的方案，使得自己的分数最大化，因此对
    两种方案分别计算当前玩家可以得到的分数，其中的最大值为当前玩家最多可以得到的分数
    :param nums:
    :return:
    '''


def PredictTheWinner3(nums):
    '''
    当否定自己的想法后，果断看了解析，学习一下动态规划，看了一下dp表格
    假设我们是玩家1，对手是玩家2
    每一个格子是我作为一个玩家，设身处地的假设我和队首面对这区间（i, j），做出
    做好的选择后能领先的最多分数
    当我面对着（i, j)区间，我作为一个玩家，只能选择i或者j
    如果我选择了i,我的对手将会获得（i+1, j)格子内的分数
    而如果我选择了j，我的对手将获得（i, j-1)格子内的分数
    而这（i+1, j)格子和（i, j-1)格子内有多少分数，是我站在对手的角度为它思考最多能领先的分数

    总结：这道题的复杂度分析：
        时间复杂度：O(n^2) 其中n为数组的长度，需要计算每个子数组对应的dp的值
        空间复杂度：O(n) 其中n为数组的长度，空间复杂度取决于额外创建的数组，如果不优化
            空间，则空间复杂度为O(n^2)，使用一维数组优化之后的空间复杂度可以将到O(n)
    :param nums:
    :return:
    '''
    length = len(nums)
    dp = [[0] * length for _ in range(length)]
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i, num in enumerate(nums):
        dp[i][i] = num
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, length):
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
    return dp[0][length - 1] >= 0


def PredictTheWinner(nums):
    '''
    对上面动态规划的优化
    :param nums:
    :return:
    '''
    length = len(nums)
    dp = [0] * length
    for i, num in enumerate(nums):
        dp[i] = num
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, length):
            dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
    return dp[length - 1] >= 0


nums1 = [1, 5, 2]  # False
nums = [1, 5, 233, 7]  # True
res = PredictTheWinner(nums)
print(res)
