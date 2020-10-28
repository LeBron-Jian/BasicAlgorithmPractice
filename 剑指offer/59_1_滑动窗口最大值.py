#_*_coding:utf-8_*_
'''
题目：
    剑指offer 59  滑动窗口的最大值

    给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里最大值

示例：
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7] 
    解释: 

          滑动窗口的位置                最大值
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7


限制：
    1 <= push_back,pop_front,max_value的总操作数 <= 10000
    1 <= value <= 10^5
'''
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            暴力切片法  这种方法在面试会被pass......
            因为这种滑动窗口每次在取max无法降低重复操作。。。。
        '''
        if len(nums) == 0:
            return []

        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            暴力切片法  优化
            条件1：假设当前滑动窗口的最大值为x，当进行滑动时会有一个一个元素进入，首先比较退出的
                    元素是否为最大的元素，如果是的话，则需要重新找到新窗口的最大值
            条件2：如果进入的元素p是比当前最大的x大，则直接将p加入到结果中

            如果上述条件都不满足，则当前的最大值还是x，加入到结果中即可
        '''
        if len(nums) == 0:
            return []

        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
            return ans
        


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            当 Nums 为空时如果有个 max() 则会产生空值报错问题，因此需要注意
        '''
        if len(nums) == 0:
            return []

        # 初始化队列
        q = nums[:k]
        # 创建保存最大值的列表
        max_list = [max(q)]
        # 创建指针变量
        pos = k
        while pos < len(nums):
            # 开始滑动
            q.pop(0)
            q.append(nums[pos])
            # 将此最大值加入列表
            max_list.append(max(q))
            # 指针加1
            pos +=1
        return max_list



re = Solution()
print(re.maxSlidingWindow(nums= [1,3,-1,-3,5,3,6,7], k=3))
