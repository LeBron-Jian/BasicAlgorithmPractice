#_*_coding:utf-8_*_
'''
001：两数之和
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个
整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


class Solution:
    def twoSum(self, nums, target):
        '''
        方法1 暴力解决，就是两个循环进行判断
        但是这样运行的时间和所占内存都是非常大的,因为我们试图通过遍历数组的其余部分
        来寻找他所对应的目标元素，这将耗费O(n)的时间，所以总的时间复杂度为O(n2)
        :param nums: List[int]
        :param target:  int
        :return: List[int]
        '''
        len_nums = len(nums)
        for i in range(0, len_nums):
            for j in range(i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums, target):
        '''
        利用哈希字典查找，通过枚举将数值对应关系放入字典中，
        然后判断目标值和每一个值得差值在不在字典中
        时间复杂度为O(n)，空间复杂度为O(n)
        通过哈希求解，这里就是字典记录了 num1和num2的值和位置，而省了再查找num2索引的步骤
        :param nums: : List[int]
        :param target: : int
        :return:  List[int]
        '''
        _dict = {}
        for ind, num in enumerate(nums):
            _dict[num] = ind
        for i, num in enumerate(nums):
            # 返回指定键的值，如果值不在字典中返回default值
            j = _dict.get(target-num)
            if j is not None and i != j:
                return [i, j]

    def twoSum2(self, nums, target):
        '''
        这方法是对上面方法的优化，当判断不符合条件时往字典中添加键值
        这样能够节省内存的消耗
        :param nums:
        :param target:
        :return:
        '''
        hashdict = {}
        for ind, m in enumerate(nums):
            if hashdict.get(target - m) is not None:
                return [ind, hashdict.get(target - m)]
            hashdict[m] = ind

    def twoSum3(self, nums, target):
        # 新建一个空字典用来保存数值及在其列表中对应的索引
        dict1 = {}
        # 遍历一遍列表对应的时间复杂度O(n)
        for i in range(0, len(nums)):
            # 相减得到另一个数值
            num = target - nums[i]
            # 如果另一个数值不在字典中，则将第一个数值及其索引保存在字典中
            if num not in dict1:
                dict1[nums[i]] = i
            # 如果在字典中则返回
            else:
                return [dict1[num], i]