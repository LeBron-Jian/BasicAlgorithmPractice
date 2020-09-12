# _*_coding:utf-8_*_
'''
74  搜索二维矩阵
题目：
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。
该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        可以直接搜索，也就是暴力搜索法，但是这种效率太低
        注意题目说的是高效的算法
        :param matrix:list
        :param target: int
        :return: bool
        '''
        for line in matrix:
            if target in line:
                return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        '''
        利用二分法查找，其时间复杂度为O(mn)
        注意：
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False
        上面代码可以使用下面代码替换
        if len(matrix) == 0:
            return False
        :param matrix:
        :param target:
        :return:
        '''
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False
        left = 0
        right = h * w - 1
        while left <= right:
            mid = (left + right)//2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        '''
        还有一种方法，就是从右上角开始寻找，因为是有序数组，如果当前元素比target大
        那么数目target会出现在下面的列中，反之会出现在前面的列中
        简单说，就是从右上角开始，大于target将列数减一，小于target将行数加1
        时间复杂度为O(m+n)，空间复杂度为O(1)
        '''
        if not matrix:
            return False
        raws, cols = len(matrix), len(matrix[0])
        raw, col = 0, cols-1
        while 0 <= raw < raws and 0 <= col < cols:
            if matrix[raw][col] < target:
                raw += 1
            elif matrix[raw][col] > target:
                col -= 1
            else:
                return True
        return False
