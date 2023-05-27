#_*_coding:utf-8_*_
'''
题目：
    剑指offer 61  扑克牌中的顺子

    从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是连续的
    2~10为数字本身，J为11，Q为12，K为13，而大小王为0
    可以看成任意数字，A不能视为14，为1

示例 1:
    输入: [1,2,3,4,5]
    输出: True
 

示例 2:
    输入: [0,0,1,2,5]
    输出: True
 

限制：
    数组长度为 5 

    数组的数取值为 [0, 13] .

'''

class Solution:
    def isStraight1(self, nums: List[int]) -> bool:
        '''
            根据题意，此5张牌是顺子的充分条件如下：
                1，除大小王外，所有牌无重复
                2，设此55张牌中最大的牌为max，最小的牌为min（大小王除外），则需要满足：
                        max-min < 5

            因而可以将问题转换为：此5张牌是否满足以上两个条件？

            很容易证明 顺子中无重复的牌，因此假设无重复的牌（大小王除外）
            并将五张牌排序，则根据大小王的数量，可分为以下三种情况：
                没有大小王，一个大小王，两个大小王
            所以我们发现：无论是否有大小王，三种情况判断条件一致：
                1，当最大牌-最小牌 <5 则可以构成顺子
                2，当最大牌-最小牌 >=5  则不可以构成顺组


            所以这里使用集合set+遍历
                遍历到五张牌，遇到大小王直接跳过
                判别重复：利用set实现遍历判重，set的查找方法的时间复杂度为O(1)
                获取最大/最小牌：借助辅助遍历 max,min，遍历统计即可。

            复杂度分析：
                时间复杂度：O(N)=O(5)  其中 N 为 nums 的长度，本题N=5，所以遍历
                            数组使用O(N)时间
                空间复杂度：O(N)=O(5)=O(1)  用于判重的辅助Set使用O(N)额外空间
        '''
        repeat = set()
        maxnum, minnum = 0, 14
        for i in nums:
            if i == 0:
                continue
            if i < minnum:
                minnum = i
            if i > maxnum:
                maxnum = i
            if i in repeat:
                return False
            repeat.add(num)
        return bool(maxnum-minnum<5)


    def isStraight2(self, nums: List[int]) -> bool:
        '''
            排序+遍历

            先对数组执行排序
            判别重复：排序数组中的相同元素位置相邻，因此可通过遍历数组，判断
                nums[i] = nums[i+1]  是否成立来判重
            获取最大/最小的牌：排序后，数组末位元素 nums[4]为最大牌；元素
                nums[joker]为最小牌，其中 joker为大小王的数量

            复杂度分析：
                时间复杂度O(nlogn)=o(5*log5)=O(1)  其中 n为nums长度，
                        比如本题N=5，数组排序使用O(nlogn)时间
                空间复杂度O(1)  变量 joker 使用O(1) 大小的额外空间
        '''
        joker = 0
        nums.sort()  # 数组排序
        for i in range(len(nums)):
            # 统计大小王的数量
            if nums[i] == 0:
                joker += 1
            # 若有重复，提前返回 False
            elif nums[i] == nums[i+1]:
                return False
        # 最大牌-最小牌<5 则可构成顺子
        return nums[-1] - nums[joker] <5
