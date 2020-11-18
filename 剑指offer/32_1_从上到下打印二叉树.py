#_*_coding:utf-8_*_
'''
题目：
    剑指offer 32_1  从上到下打印二叉树

    从上到下打印二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如：
    给定二叉树: [3,9,20,null,null,15,7],

                3
               / \
              9  20
                /  \
               15   7

返回：
    [3,9,20,15,7]



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
    def levelOrder(self, root: TreeNode) -> List[int]:
        '''
            第一反应，这就是一个 level order，直接写

            二叉树的从上至下打印（即按照层打印），又称为二叉树的广度优先搜索（BFS）
            BFS通常借助队列的先入先出特性来实现
        '''
        if not root:
            return []
        res = [root.val]
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                res.append(node.left.val)
            if node.right:
                queue.append(node.right)
                res.append(node.right.val)
        return res


    def levelOrder1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(root.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
