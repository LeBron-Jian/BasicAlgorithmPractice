# _*_coding:utf-8_*_
'''
56 合并区间
题目：
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

首先按照位置进行排序，不然这个集合都是乱序的，都没法判断重叠区间 
    排序的时候，需要按照列表中区间的左端点升序排序：intervals.sort(key=lambda x: x[0])
    当然也可以不用写key，它是默认按照左端点升序排序（不放心的话可以写，无所谓）
其次，两个区间是否重叠
    如果当前区间的做断电在数组中最后一个区间的右端点之后，那么他们不会重合，我们可以直接将这个区间加入数组的末尾
    否则他们重合，我们需要用当前区间的右端点更新数组中最后一个区间的右端点，将其置为二者中的较大值
    但是如何找出这个区间。首先我们新生成一个res列表，并将排好序的列表的第一个元素放进去
    那么左边位置就固定了，然后从1开始，遍历剩下的区间，所以说右边的位置就变换
    一个固定，遍历另一个，不是很简单了。

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <2:
            return intervals
        # 先按区间左边界值由小到大排序，sort函数默认从小到大排序
        # 当然也可以使用sort(reverse=True) 表示翻转，意思从大到小排序
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], intervals[i][-1])
            else:
                res.append(intervals[i])
        return res

    
# 复杂度的分析
# 时间复杂度：O(nlogn)，其中n为区间的数量，除去排序的开销，我们只需要一次线性扫描，所以时间开销为排序的O(nlogn)
# 空间复杂度：O(logn) 其中n为区间的数量，这里计算的是存储答案之外，使用的额外空间，所以排序所需的空间开销为O(logn)
    
    
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        官方答案
        '''
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if merged is None or merged[-1][-1] < intervals[interval][0]:
                merged.append(intervals[interval])
            else:
                # 否则的话，我们就可以与上一区间进行合并
                # merged[-1][-1] = max(merged[-1][-1], intervals[interval][-1])
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
         return merged
                
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        在看大神的解析，找到了栈的使用，这里用一次，熟悉一下栈的操作
        操作如下：
            1，排序
            2，判断是否非空
            3，初始化空栈，遍历intervals，如果栈为空，则将intervals元素添加到栈中
                否则提取栈顶元素和intervals当前元素，如果栈顶元素的第二个数字大于等于intervals
                当前元素的第一个元素，则对栈采用pop运算和push，就是先出再进

            不过栈的操作比起上面列表麻烦。
        '''
        intervals.sort()
        if not intervals:
            return []
        stack_res = []
        for i in range(len(intervals)):
            if not stack_res:
                stack_res.append(intervals[i])
            else:
                left_fix = stack_res[-1]
                right_run = intervals[i]
                if left_fix[-1] > right_run[0]:
                    stack_res.pop()
                    stack_res.append([min(left_fix[0], right_run[0]), max(left_fix[1], right_run[1])])
                else:
                    stack_res.append(right_run)
        return stack_res
