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
        


class Solution2:
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


class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            滑动窗口解题思路：官方解法：单调队列
            
            设窗口区间为[i, j]，最大值为x_j。当窗口向前移动一格，则区间变为[i+1, j+1]，即添加了
            nums[j+1]，删除了 nums[i]
            
            若只向窗口[i, j] 右边添加数字 nums[j+1]，则新窗口最大值可以通过一次对比，使用O(1)时间得到：
            x_j+1 = max(x_j， nums[j+1])
            
            而由于删除的 nums[i] 可能恰好是窗口内唯一的最大值 x_j，因此不能通过上述方法计算x_j+1，而必须使用O(j-i)时间
            遍历整个窗口区间获取最大值，即：
            x_j+1 = max(nums(i+1), nums(j+1))
            根据以上分析，可得暴力法的时间复杂度为O(n-k+1)k  约等于 O(nk)
                设数组 nums 的长度为n，则共有 n-k+1 个窗口
                获取每个窗口最大值需详细遍历，时间复杂度为O(k)
                
               获取窗口很简单，但是难的是：如何每次窗口滑动后，将“获取窗口内的最大值” 的时间复杂度从O(k) 降低到 O(1)
        '''
        from collections import deque
        q = deque()
        res, n = [], len(nums)
        for i,j in zip(range(1-k, n+1-k), range(n)):
            if i>0 and q[0] == nums[i-1]:
                q.popleft()  # 删除 q中对应的 nums[i-1]
            while q and q[-1] < nums[j]:
                q.pop()  # 保持q递减
            q.append(nums[j])
            if i >= 0:
                res.append(q[0])  # 记录窗口最大值
        return res
        
        
        def maxSlidingWindow(self, nums, k):
            if not nums or k==0:
                return []
            deque = deque()
            for i in range(k):  # 未形成窗口
                while deque and deque[-1] < nums[i]:
                    deque.pop()
                deque.append(nums[i])
            res = deque[0]
            for i in range(k, len(nums)):
                if  deque[0] == nums[i-k]:
                    deque.popleft()
                while deque and deque[-1] < nums[i]:
                    deque.pop()
                deque.append(nums[i])
                res.append(deque[0])
            return res
                    

re = Solution()
print(re.maxSlidingWindow(nums= [1,3,-1,-3,5,3,6,7], k=3))
