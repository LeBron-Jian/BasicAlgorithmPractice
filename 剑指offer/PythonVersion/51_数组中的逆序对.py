#_*_coding:utf-8_*_
'''
    剑指offer  51   数组中的逆序对

    在数组中的两个数字，如果前面一个数字大于后面的数字，则
    这两个数组成一个逆序对。输入一个数组，求出这个数组中的逆
    序对的总数

示例1：
    输入: [7,5,6,4]
    输出: 5
 
    分析：（此题的逆序对为）
    [7, 5], [7, 6], [7, 4], [5, 4], [6, 4]

限制：
    0 <= 数组长度 <= 50000


*************************解题思路************************************
            归并排序
                归并排序是分治实现的典型应用，它包含这样三个步骤：
                1，分解：待排序的区间 [l, r]，令 m = (l+r)//2
                    我们把[l,r]分为[l, m], [m+1, r]
                2，解决：使用归并排序递归地排序两个子序列
                3，合并：把两个已经排好序的子序列[l,m]和 [m+1, r]合并起来

            在待排序序列长度为1的时候，递归开始回升，因为我们默认长度为1的序列
            拍好序列的。

            本题思路：
                求逆序对和归并排序由什么关系呢？
                关键就在于归并当中并的过程，我们通过一个实例来看看。假设
                我们已经有两个已排序的序列等待合并，分别为：
                L= [8, 12, 16, 22, 100]  R=[9, 26, 55, 64, 91]
                一开始我们用指针 lPtr=0指向L的首部，rPtr=0指向R的头部
                记好合并好的部分为M

            L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = []
                 |                          |
               lPtr                       rPtr
                
                我们发现 lPtr指向的元素小于 rPtr 指向的元素，于是把lPtr指向
                的元素放入答案，并把 lPtr 后移一位。
            L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8]
                    |                       |
                  lPtr                     rPtr
                这个时候我们把左边的 8 加入了答案，我们发现右边没有数比 8 小，
                所以 8 对逆序对总数的贡献为 0

                接着我们继续合并，把9加入答案，此时lPtr指向12，rPtr指向26
            L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8, 9]
                    |                          |
                   lPtr                       rPtr
                此时 lPtr 比 rPtr 小，把lPtr对应的数加入答案，并考虑它对逆序对
                总数的贡献为 rPtr 相对 R 首位置的偏移1（即右边只有一个数比12小，
                所以只有它和12构成逆序对），以此类推。

                我们发现用这种 “算贡献” 的思想在合并的过程中计算逆序对的数量的时候，
                只有 lPtr 右移的时候计算，是基于这样的事实，当前lPtr指向的数字比rPtr
                小，但是比R中 [0, rPtr-1]的其他数字大，


        逆序数 就是  mid-i+1

'''
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
            记序列长度为 n
                时间复杂度为：同归并排序O(nlogn)
                空间复杂度为：同归并排序O(n),因为归并排序需要用到一个临时数组
        '''
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n-1)

    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l+r)//2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid+1, r)
        i, j, pos = l, mid+1, l
        while i <= mid and j <=r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j-(mid+1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid+1):
            tmp[pos] = nums[k]
            inv_count += (j-(mid + 1))
            pos += 1
        for k in range(j, r+1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count


class Solution1:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        return self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, li, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(li, low, mid)
            self.merge_sort(li, mid+1, high)
            self.merge(li, low, mid, high)
        return self.count

    def merge(self, li, low, mid, high):
        i = low
        j = mid + 1
        ltmp = []
        while i <= mid and j <= high:
            if li[i] <= li[j]:
                ltmp.append(li[i])
                i += 1
            else:
                print(li[i], li[j], mid+1, i)
                self.count += (mid+1-i)
                ltmp.append(li[j])
                j += 1

        while i <= mid:
            ltmp.append(li[i])
            i += 1

        while j <= high:
            ltmp.append(li[j])
            j += 1

        li[low:high+1] = ltmp
        # return self.count



nums = [7,5,6,4]   # 5
# nums = [1,3,2,3,1]  # 4
print(Solution1().reversePairs(nums))




