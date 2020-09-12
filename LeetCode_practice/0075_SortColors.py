# _*_coding:utf-8_*_
'''
75  颜色分类
题目：
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
    使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]
    
进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
        首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？


'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        计算排序
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for _ in range(3)]
        for val in nums:
            count[val] += 1
        nums.clear()
        for ind, val in enumerate(nums):
            for i in range(val):
                nums.append(ind)
        return nums


# ****************方案二，快速排序 自己的想法 ***********************
'''
我这样写有点复杂，看了官方解释，发现简单一些，我也更新了代码
但是这里想说的是，自己写的快速排序，算是一个组件，可以随时调用
'''

def partition(data, left, right):
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return left


def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)
    return nums


def sortColors1(nums):
    left, right = 0, len(nums) - 1
    res = quick_sort(nums, left, right)
    return res


nums = [2, 0, 2, 1, 1, 0]
print(sortColors1(nums))

# ****************方案三，一次遍历  官方解法 ***********************
'''
    这道题被称为 荷兰国旗问题，最初由 Dijkstra 提出的
    其主要实现是给每个数字设定一种颜色，并按照荷兰国旗颜色的顺序进行调整
    
    我们用三个指针（P0, p1 和 curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素
    本思路是沿着数组移动 current 指针，若 nums[curr]=0，则将其与 nums[p0]互换；
    若 nums[curr]=2,则与 nums[p2] 互换
算法：
    初始化0的最右边界：P0 = 0，在整个算法执行过程中  nums[idx < p0] = 0
    初始化2的最左边界：p2=n-1，在整个算法执行过程中 nums[idx > p2] = 2
    初始化当前考虑元素序号：curr = 0
    while  curr <= p2:
        若 nums[curr] = 0  交换第 curr个和 第p0个元素，并将指针都向右移
        若 nums[curr] = 2  交换第 curr 个和 第p2个元素，并将 p2指针左移
        若 nums[curr] = 1 将指针 curr右移
    
'''


def sortColors(nums):
    curr, p0, p2 = 0, 0, len(nums) - 1
    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            # nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
    return nums

nums = [2, 0, 1]
nums1 = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))

'''
复杂度分析：
    时间复杂度：由于对长度N的数组进行一次遍历，时间复杂度为O(N)
    空间复杂度：由于只使用了常数空间，空间复杂度为O(1)
'''


'''
总结：
    实际上，原地修改，O(n) 就是双指针的特性
    虽然这道题用了三个指针，但是双指针方法的精髓不在于用了几个指针，
    而是使用一个当前指针，若干个区域指针，原地的在数组上进行区域的划分
    划分为处理过后的区域，不需要的区域，未知的区域三个概念。
    上面官方解释实际上是将原数组分为全0区域，全2区域，全1区域，未知区域
    （其中全0 和全2就是处理后的区域，全1痊愈就是不需要处理的区域
    
    双指针的做法就是在一个while里面根据当前指针所指的当前值，做出对的决策
    扩大或缩小某些区域。
    主要注意的是：
        当前值为0,0需要放到全0区域，交换当前值和p0值，然后修改区域指针
                显然全0区域要扩展，所以p0+=1， curr +=1
        当前值为1，那么不需要区域扩展，在不需要区域非空的情况下，从P0交换
                过来的值一定是1，所以P0不需要加，curr +=1
        当前值为2，那么全2区域需要扩展，同时需要将数值交换过去，这里需要考虑
                不需要区域是否扩展，不需要区域就是全1区域，但是从p2区间交换
                过来的值不能保证是1，所以不需要区域不能扩展。p2-=1即可
'''
