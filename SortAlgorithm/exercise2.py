# _*_coding:utf-8_*_
'''
2，给定一个 m*n 的二维列表，查找一个数是否存在，列表有下列特性：

每一行的列表从左到右已经排序好

每一行第一个数比上一行最后一个数大
[[1,2,3],
[43,54,65]
如果是就返回TRUE，不是就返回FALSE
'''


def searchMatrix(matrix, target):
    for line in matrix:
        if target in line:
            return True
    return False


def searchMatrix1(matrix, target):
    h = len(matrix)
    if h == 0:
        return False  # h=0 即为 []
    # 当然也出现一种可能就是 [[],[]]
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = w * h - 1
    '''
    012
    345
    678
    第几行开始的第一个数的下标就是 num//w
    i = num //3    j=num//3
    '''
    # 直接使用二分查找的代码
    while left <= right:
        mid = (left + right) // 2
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


matrix = [[1, 2, 3], [5, 6, 7], [9, 12, 23]]
target = 32
res = searchMatrix1(matrix, target)
print(res)