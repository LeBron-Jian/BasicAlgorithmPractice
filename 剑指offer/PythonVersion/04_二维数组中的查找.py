#_*_coding:utf-8_*_
'''
题目：
    剑指offer 04  二维数组中的查找

    在一个 n*m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照
    从上到下递增的顺序排序，请完成一个高效的函数，输入这样一个二维数组和一个整数
    判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

    给定 target = 5，返回 true。

    给定 target = 20，返回 false。

 
限制：
    0 <= n <= 1000

    0 <= m <= 1000



'''
from typing import List

class Solution:
    def findNumberIn2DArray1(self, matrix: List[List[int]], target: int) -> bool:
        '''
            日常暴力，虽然没用
        
        复杂度分析：
            时间复杂度：O(MN)  最好情况O(1)
            空间复杂度：O(1)
        '''
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False

    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        '''
            也可以这样查找，但是针对性不强，因为对于二维矩阵，我们只使用了行，或者列

            复杂度分析：
                时间复杂度：O(nlogn)
                空间复杂度：O(1)
        '''
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        
        left, right = 0, len(matrix[0])-1
        for i in range(len(matrix)):
            while left <= right:
                mid = (left + right+1)//2
                if target > matrix[i][mid]:
                    left = mid +1
                elif target < matrix[i][mid]:
                    right = mid-1
                else:
                    return True
            left = 0
        return False

    def findNumberIn2DArray3(self, matrix: List[List[int]], target: int) -> bool:
        '''
            下面这种针对性比较强，即从右上角往左下角查找。

        标志位法
            选左上角，往右走和往下走都增大，不能选
            选右下角，往上走和往左走都减小，不能选
            选左下角，往右走增大，往上走减小，可选
            选右上角，往下走增大，往左走减小，可选

        复杂度分析：
            时间复杂度：O(N+M)
            空间复杂度：O(1)
        '''
        # 针对[] 和 [[]] 这种特殊情况
        if len(matrix) == 0 or len(matrix[0]) ==0:
            return False

        # 矩阵尺寸
        height = len(matrix)
        width = len(matrix[0])

        # 右上角开始检索
        row, col=0, width-1
        while row < height and col >=0:
            if matrix[row][col] > target:
                col -=1
            elif matrix[row][col] > target:
                row += 1
            else:
                return True

        return False
