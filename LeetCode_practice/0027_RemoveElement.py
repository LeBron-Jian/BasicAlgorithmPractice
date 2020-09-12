# _*_coding:utf-8_*_
'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        最容易理解的就是移除元素，当val与nums中出现的值一致时候移除即可
        需要注意的是使用for循环的话容易报错 list index out of range
        这里的问题是当我们移除列表的内容时候，新列表的长度不够了！！！
        :param nums:
        :param val:
        :return:
        '''
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)

    def removeElement1(self, nums: List[int], val: int) -> int:
        '''
        这个和上面的方法一样，只不过简洁一下代码
        '''
        while (val in nums):
            nums.remove(val)
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        '''
        这个是查看网友的解题方法，套用双指针
        '''
        j = nums.index(val) if val in nums else len(nums)


def removeElement1(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


def removeElement2(nums, val):
    while True:
        if val in nums:
            nums.remove(val)
        else:
            break
    return len(nums)


def removeElement3(nums, val):
    # 注意需要原地移除所有数值等于val的元素，并返回移除后数组的新长度
    # 还需要仅使用 O(1) 额外空间并原地 修改输入数组
    # 所以我这个是错误的，因为我只获得了数组的新长度，但是没有移除val
    # 这里做一个警示。
    length = 0
    for i in nums:
        if i != val:
            length += 1
    return length


def removeElement3_plus1(nums, val):
    # 对解法3进行改善，思路还是双指针，不过需要对元素调位置
    # 这个解法，其实与LeetCode283(moveZeroes) 有相似之处
    # 这里也是将val移动到后面（只不过val为0）
    # 这样就好了，引起其时间复杂度为O(n)，空间复杂度为O(1)
    length = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[length] = nums[i]
            length += 1
    nums[:] = nums[:length]
    return length


def removeElement3_plus2(nums, val):
    # 对解法3进行改善，思路还是双指针，不过需要对元素调位置
    # 这个解法，与上面想法相似，但是略有不同，上面是覆盖
    # 这里是交换，不过大同小异
    length = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[length], nums[i] = nums[i], nums[length]
            length += 1
    nums[:] = nums[:length]
    return length


def removeElement4(nums, val):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            # 注意这里如果将当前值赋给 n的最后一个值会报错
            # nums[n-1] = nums[i]
            n -= 1
        else:
            i += 1
    return i


def removeElement5(nums, val):
    # 题目有讲，虽然返回数值是整数，但是输出答案是数组的原因
    # 不管返回什么，调用者都可以调用里面的数组
    #
    while val in nums:  # 没有元素就结束，但是必须写while，for循环不可以
        nums.pop(nums.index(val))  # 循环结束
    return len(nums)  # 其实这个可以写，可以不写，反正本题不会调用


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement3(nums, val))  # 5

'''
总结一下：
    这里主要对指针法进行总结，也就是解法3的两种方法，覆盖和交换 和 解法4进行总结
1，快慢指针法（双指针法）：
    初始化两个指针都指向0索引，快指针一直右移动，当快指针指向的数字不等于val时，
    把该数字赋值给慢指针的指向，同时慢指针右移一位，否则慢指针一直保持原位置不变
    这样慢指针之前的所有值就是快指针之前的所有非val值
    复杂度分析：
        快指针需要一直遍历整个数组，慢指针是在出现了非val值才会移动一位，最差的情况
        是数组没有val值，快慢指针都一起移动，遍历了两次数组，每次都要做一次赋值操作
        所以执行次数为2n，时间复杂度为O(n)，没有使用新数组，空间复杂度为O(1)

2，指针法
    指针初始化指向0，若等于val，则把指针指向的值和最后一个值互换，然后把这个数组的长度减1
    这样val就被删除掉了，然后再从该指向开始遍历比较，若不等于val，右移指针，直到指针指向
    最后一个元素（这里指 数组长度变化后）
    复杂度分析：
        指针指向值不为 val 就右移，指向 val会执行一次交换同时缩短数组长度，从该位置继续遍历
        最坏情况是每次都交换，执行n次，所以时间复杂度为O(n)，空间复杂度为O(1)
'''
