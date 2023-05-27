#_*_coding:utf-8_*_
'''
题目：
    剑指offer 29  顺时针打印矩阵

    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
            方法1，模拟
            可以模拟打印矩阵的路径，初始位置是矩阵的左上角，初始方向是向右，当路径
            超出界限或者进行之前访问过的位置时，则顺时针旋转，进入下一个方向

            判断路径是否进入之前访问过的我IEhi在需要使用一个与输出矩阵大小相同的辅助矩阵
            其中每个元素表示该位置是否被访问过，当一个元素被访问时，辅助矩阵中的对应
            位置元素设为已访问。

            如何判断路径是否结束？
            由于矩阵中的每个元素都被访问一次，因此路径的长度即Wie矩阵中的
            元素数量，当路径的长度达到矩阵中的元素数量时即为完整路径，将该路径返回

            复杂度分析
                时间复杂度：O(mn) 其中m和n分别为输入矩阵的行数和列数，矩阵中的
                            每个元素都要被访问一次
                空间复杂度：O(mn) 需要创建一个大小为m*n 的矩阵来记录每个位置是否
                            被访问过
        '''
        if not matrix or matrix[0]:
            return list()
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False]*columns for _ in range(rows)]
        total = rows*columns
        order = [0]*total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow = row + directions[directionIndex][0]
            nextColumn = column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and
                not visited[nextRow][nextColumn]):
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order



class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
            大佬解法：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
            解题思路：

                我们首先可以画几个图，从图中可以看到：顺时针打印矩阵的顺序是：
                从左到右  从上到下 从右到左  从下向上 循环

                因此，考虑设定矩阵的 左，上，右，下四个边界，模拟以上矩阵遍历顺序。

            算法流程：
                1，空值处理：当 matrix 为空时，直接返回空列表 [] 即可
                2，初始化：矩阵左，右，上，下四个边界 l,r,t,b，用于打印的结果列表res
                3，循环打印：从左到右 从上到下，从右到左 从下到上 四个方向循环，每个
                    方向打印中做以下三件事（各方向的具体信息如下：）
                    1，根据边界打印，即将元素按顺序添加到列表res尾部
                    2，边界向内收缩11（代表以及被打印）
                    3，判断是否打印完毕（边界是否相遇），若打印完则跳出
                4，返回值，返回res即可


            复杂度分析：
                时间复杂度：O(mn)  M ,N 分别为矩阵行数和列数
                空间复杂度：O(1)   四个边界 l,r,t,b 使用常数空间的额外大小
                    而res是必须使用的空间

        '''
        if not matrix:
            return []
        l, r, t, b, res = 0, len(matrix[0])-1, 0, len(matrix)-1, [] 
        while True:
            for i in range(l, r+1):
                # left to right
                res.append(matrix[t][i])
            t += 1
            if t>b:
                break
            for i in range(t, b+1):
                # top to bottom
                res.append(matrix[i][r])
            r -= 1
            if l>r:
                break
            for i in range(r, l-1, -1):
                # right to left
                res.append(matrix[b][i])
            b -= 1
            if t>b:
                break
            for i in range(b, t-1, -1):
                # bottom to top
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res
