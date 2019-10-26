# _*_coding:utf-8_*_
'''
3，给定一个列表和一个整数，设计算法找到两个数的下标，
使得两个数之和为给定的整数。保证肯定仅有一个结果。

例如，列表[1,2,5,4] 与目标整数3,1+2=3，结果为（0,1）
'''


def TwoSum(nums, target):
    '''

    :param nums:  nums是代表一个list
    :param target: target是一个数
    :return: 结果返回的时两个数的下标
    '''
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)


def TwoSum1(nums, target):
    # 新建一个空字典用来保存数值及在其列表中对应的索引
    dict1 = {}
    for i in range(len(nums)):
        # 相减得到另一个数值
        num = target - nums[i]
        if num not in dict1:
            dict1[nums[i]] = i
        # 如果在字典中则返回
        else:
            return [dict1[num], i]

def binary_search(li,left, right, val):
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid +1
        else:
            right = mid -1
    else:
        return None

def TwoSum2(nums, target):
    for i in range(len(nums)):
        a = nums[i]
        b = target - a
        if b >=a:
            j = binary_search(nums, i+1, len(nums)-1, a)
        else:
            j = binary_search(nums, 0, i-1, b)
        return (i, j)



nums = [1, 2, 5, 4]
target = 3
res = TwoSum1(nums, target)
print(res)
