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

    
  class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
            解题思路：索引+1正好与值对应，进行匹配排序，如果第二次遇到相同的值则必为重复值
            复杂度分析：
                时间复杂度O(n)  最多遍历两次
                空间复杂度O(n)  若不算输出空间则为O(1)
        '''
        i = 0
        res = []
        for i in range(len(nums)):
            index = nums[i]-1
            # print('dadaasd:',index)
            # while nums[index] != nums[i]:
                # nums[index], nums[i] = nums[i], nums[index]
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i] - 1],nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        return res
