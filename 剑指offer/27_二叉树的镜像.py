#_*_coding:utf-8_*_
'''
题目：
    剑指offer 27  二叉树的镜像

    请完成一个函数，输入一个二叉树，该函数输出它的镜像

    例如输入：

                     4
                   /   \
                  2     7
                 / \\   / \
                1   3 6   9
    镜像输出：

                     4
                   /   \
                  7     2
                 / \\   / \
                9   6 3   1


 示例 1：
    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]
 

限制：
    0 <= 节点个数 <= 1000


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        '''
            二叉树镜像定义：对于二叉树中任意节点root，设其左右子节点分别为left， right
            则在二叉树的镜像中的对应root节点，其左右子节点分别为right left

            方法一  递归：
                根据二叉树镜像的定义，考虑递归遍历dfs二叉树，交换每个节点的左右节点，
                即可生成二叉树的镜像。

            递归解析：
                1，终止条件：当节点root为空时，则返回null
                2，递推工作：
                    1，初始化节点temp，用于暂存root的左右节点
                    2，开启递归右子节点，并将返回值作为root的左子节点
                    3，开启递归左子节点，并将返回值作为root的右子节点
                3，返回值：返回当前节点root

            为什么要暂存root的左子节点：
                因为在递归右子节点的时候，我们保存在左子节点，所以此时左子节点的值已经发生变换

            复杂度分析：
                时间复杂度O(n)：其中n为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点
                空间复杂度O(n)：最差情况下，当二叉树退化为链表，递归时系统需要使用O(n)大小的栈空间
        '''
        if not root:
            return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.eft)
        return root

    def mirrorTree1(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = root.left
        root.left = self.mirrorTree1(root.right)
        root.right = self.mirrorTree1(temp)
        return temp


class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        '''
            辅助栈，或者辅助队列
            利用栈（队列）遍历树的所有节点 node，并交换每个node的左右子树节点

            算法流程：
                1，特例处理：当root为空时候，直接返回null
                2，初始化：栈，加入根节点root
                3，循环交换：当栈stack为空时跳出：
                    1，出栈：记为node
                    2，添加子节点：将node左右节点入栈
                    3，交换：交换node的左右节点
                4，返回值：返回根节点root

            复杂度分析：
                时间复杂度：O(n) n为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点
                空间复杂度：O(n) 最差情况下，栈最多同时存储n/2个结点
        '''
        if not root:
            return None
        stack = [root]
        while len(stack) != 0:
            res = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
        return root


    def mirrorTree1(self, root: TreeNode) -> TreeNode:
        '''
            辅助队列
        '''
        if not root:
            return None
        queue = [root]
        while len(queue) != 0:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            temp.left, temp.right = temp.right, temp.left
        return root

