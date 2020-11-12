#_*_coding:utf-8_*_
'''
442  数组中重复的数据
题目：
    给定一个整数数组 a，其中 1 <= a[i] <=n （n为数组长度）,其中有些元素出现两次
    而其他元素出现一次。
    找到所有出现两次的元素
    你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：
    输入:
    [4,3,2,7,8,2,3,1]

    输出:
    [2,3]
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
            解题思路：要不使用额外内存空间，则只能原地修改数组元素来标记是否访问过
            原理：如果是相同的元素，那么以他们为索引的元素值一定是同一值，因此可以修改
            该值来标记是否被访问过
            注意：既要原地修改元素，就不能影响其自身作为索引的访问，那么只有一种方法，那就
            是将该元素取反，或者加减某个数，在访问的时候，再通过取正或加减某个数还原回来
        '''
        if not nums:
            return []
        res = []
        for num in nums:
            # 因为我们是直接原地修改元素为负值来标记是否被访问过，因此这里的num一定要取绝对值
            index = abs(num) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为num的元素
                res.append(abs(num))
            # 原地修改访问标记
            nums[index] = -nums[index]
        return res

    
    
 class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
            同样是原地修改，这里写的简单易懂：
            [4, 3, 2, 7, 8, 2, 3, 1]
            [-4, -3, -2, -7, 8, 2, -3, -1]
        '''
        if not nums:
            return []
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                # nums[index] *= -1
                nums[index]  = - nums[index]
            else:
                # res.append(index+1)
                res.append(abs(num))
        return res
