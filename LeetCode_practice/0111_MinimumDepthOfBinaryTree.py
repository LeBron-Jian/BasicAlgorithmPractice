# _*_coding:utf-8_*_
'''
111  二叉树的最小深度
题目：
给定一个二叉树，找出最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点
# 也就是说为零的子树代表没有结点，不能参与深度的计算
# 当左右子树都有节点的时候，才存在子树间深度大小的比较
# 有一个为零，一个不为零，说明此节点不是叶子节点，要计算深度必须还要往下

示例：
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        递归法吧
        节点不存在时，返回0
        左右子节点不存在时，说明该节点为叶子节点，返回1
        左右子节点存在一个时，返回 1+minDepth（子节点）
        左右子节点均存在时，返回1+较小的 minDepth（子节点）

        如果左子树深度，右子树深度均不为零，则用 min取其中最小值
        如果有一个为零，取其中非0的数，
        都为0，则取0
        :param root:
        :return:
        '''
        pass


class solution:
    def minDepth(self, root):
        # 当子树为空，则返回0
        if not root:
            return 0
        leftDepth, rightDepth = self.minDepth(root.left), self.minDepth(root.right)
        childDepth = min(leftDepth, rightDepth) if leftDepth and rightDepth else leftDepth or rightDepth

        return 1 + childDepth
        # 为了方便理解，上面代码可以写为：
        # 当左右子树有一个为空的时候，深度为另一棵树的深度+1
        # if leftDepth == 0 or rightDepth == 0:
        #     return leftDepth + rightDepth + 1
        # 当两个子树都不为空的时候，返回潜在的那棵树长度+1
        # return min(leftDepth + rightDepth) + 1


class solution1:
    def minDepth(self, root):
        if not root:
            return 0
        # 叶子节点，即当左右子树均为空
        if not root.left and not root.right:
            mindepth = 1
        # 当左右子树均不为空
        elif root.left and root.right:
            mindepth = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # 左子树不为空，右子树为空
        elif root.left:
            mindepth = self.minDepth(root.left) + 1
        else:
            mindepth = self.minDepth(root.right) + 1
        return mindepth



