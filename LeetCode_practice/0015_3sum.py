# _*_coding:utf-8_*_
'''
15 三数之和
题目：
    给定一个包含 n 个整数的数组 nums 和一个目标值 target
    判断 nums 中是否存在3个元素a, b, c,使得 a+b+c=0
    找出所有满足条件且不重复的三元组。
注意：
    答案中不可以包含重复的三元组

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        因为看到这个题，其实第一想到的就是两数相加。
        最简单的就是暴力搜索法，但是三数相加的话，暴力搜索法的时间复杂度为O(N^3)
        但是暴力解法这个复杂度太高了，感觉肯定会超时。
        不过我还是打算先写出来。。。
        '''
        # 注意：答案中不可以包含重复的三元组
        # 如果说没有这行注意，则下面代码就是暴力解法。但是我们需要加条件
        # nums.sort()
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.append([nums[i], nums[j], nums[k]])
        # return res
        # 注意 sort()内置函数的时间复杂度为O(nlogn) 空间为O(n)
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i >= 1:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] == nums[j-1] and j >= i+1+1:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[k] == nums[k-1]  and k >= j+1+1:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        首先要熟悉求两数之和的写法，然后在N>2的时候，采用递归处理，一次减少1
        关键点是：
            1，先对 nums 排序
            2，递归处理时的剪枝处理
        '''
        nums.sort()
        ans = set()
        N, target = 3, 0
        self.find_sum(nums, 0, N, target, [], ans)
        return list(ans)

    def find_sum(self, nums, start, N, target, path, ans):
    	if len(nums) < N or N<2:
    		return
    	if N == 2:
    		d = set()
    		for j in range(start, len(nums)):
                if target - nums[j] in d:
                    ans.add(tuple(path + [target - nums[j], nums[j]]))
                else:
                    d.add(nums[j])
        else:
            for i in range(start, len(nums)):
                # 剪枝1: target比剩余数字能组成的最小值还要小 或 比能组成的最大值还要大，就可以停止循环了
                if target < nums[i] * N or target > nums[-1] * N: break
                # 剪枝2: 去重
                if i > start and nums[i] == nums[i - 1]: continue
                # drill down
                self._find_sum(nums, i + 1, N - 1, target - nums[i], path + [nums[i]], ans)
        return

# 链接：https://leetcode-cn.com/problems/3sum/solution/jian-ji-tong-yong-xie-fa-nshu-zhi-he-pythonxiang-x/

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
             本题的难点就是  如何去除重复解，因为是list套用list
             所以不能用set吧。。。
             算法流程：
             1，特判，对于数组长度n，如果数组是null或者数组小于2，则返回空list
             2，对数组进行排序
             3，遍历排序后数组：
                     若 Nums[1] > 0，右指针 R=n-1，当L<R时，执行循环
                     对于重复元素，跳过，避免出现重复解
                     令左指针L=i+1，右指针R=n-1，当L<R时，执行循环
                             当nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界
                             是否和下一位置重复，去除重复解，并同时将L，R移到下一位置，寻找新解
                             若和大于0，说明 nums[R]太大，R左移
                             若和小于0，说明 nums[L]太小，L右移
        '''
        n = len(nums)
        res = []
        if (not nums or n<3):
            return []
        for i in range(n):
            # 因为三个数字相加要等于0
            if (nums[i]>0):
                return res
            if (i>0 and nums[i]==nums[i-1]):
                continue
            L = i+1
            R = n-1
            while (L<R):
                if (nums[i]+nums[L]+nums[R]==0):
                    res.append(nums[i], nums[L], nums[R])
                    while(L<R and nums[L]== nums[L+1]):
                        L = L+1
                    while(L<R adn nums[R]==nums[R+1]):
                        R = R+1
                    L = L+1
                    R = R+1
                elif (nums[i]+nums[L]+nums[R]>0):
                    R=R+1
                else:
                    L=L+1
        return res


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            对数组进行遍历，因为是求三个数，所以需要三个下标，left为i的下一个
            当这三个数相加为0时，将三个数保存下来
            然后移动left和right，这是因为数组已经是从小到大进行排序了，
                当left增大时，right队应要减少
            中间把重复的值过滤掉即可
        '''
        # 双指针，外部时间复杂度为O(n)，sort内置函数的时间复杂度为O(nlogn) 空间为O(n)
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        return result