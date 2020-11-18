#_*_coding:utf-8_*_
'''
题目：
    107   二叉树的层次遍历 II

给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        levels.reverse()
        return levels



class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        res.reverse()
        return res

