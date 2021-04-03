#_*_coding:utf-8_*_
'''

    面试题01.07  旋转矩阵

    题目：给你一幅由 N*N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像
    旋转90度。

    不占用额外内存空间能否做到？

示例 1:
    给定 matrix = 
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

    原地旋转输入矩阵，使其变为:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]

示例 2:
    给定 matrix =
        [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ], 

    原地旋转输入矩阵，使其变为:
        [
          [15,13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7,10,11]
        ]



'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        
        # 对于矩阵中的第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。
        """
        n = len(matrix)
        # 图像图像为为 N*N  的矩阵
        new_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n-i-1] = matrix[i][j]
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        print(new_matrix)
        matrix[:] = new_matrix

    def rotete2(self, matrix: List[List[int]])-> None:
        '''
            Do not return anything, modify matrix in-place instead.
        '''
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                print(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][n-j-1], matrix[n-i-1][j] )
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1]  = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1],  matrix[i][j] 
