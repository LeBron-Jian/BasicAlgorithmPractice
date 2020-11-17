#_*_coding:utf-8_*_
'''
    题目： 111   二叉树的最小深度
    

    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    说明: 叶子节点是指没有子节点的节点。

示例1:
    给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回它的最小深度  2.

    输入：root = [3,9,20,null,null,15,7]
    输出：2

示例2：

    输入：root = [2,null,3,null,4,null,5,null,6]
    输出：5


解题思路：
    首先，定义树节点结构TreeNode
    其次，最简单的方法是使用递归，我们使用深度优先搜索来解决这个问题

    使用层次遍历二叉树，如果树为空，直接返回0，否则将树和深度值1入队列
    逐一弹出队列中节点，若某节点左右子树均为空，此节点即为最小深度的叶子节点
    返回其深层即可。若其存在子树，则将其存在的子树和子树深度入队列
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        children = [root.left, root.right]
        # if we are at left node
        if not any(children):
            return 1
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

from collections import deque

class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        de = deque()
        de.append((root, 1))
        while de:
            p, dep = de.popleft()
            if not p.left and not p.right:
                return dep
            if p.left:
                de.append((p.left, dep+1))
            if p.right:
                de.append((p.right, dep+1))


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        '''
            深度优先搜索
            首先可以想到使用深度优先搜索的方法，遍历整棵树，记录最小深度

            对于每个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度
            这样就将一个大问题转换为了小问题，可以递归的解决其问题
        '''
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        mindepth = 10**9
        if root.left:
            mindepth = min(self.minDepth(root.left), mindepth)
        if root.right:
            mindepth = min(self.minDepth(root.right), mindepth)
        return mindepth + 1


class Solution3:
    def minDepth(self, root: TreeNode) -> int:
        '''
            广度优先搜索
                我们可以使用广度优先搜索的方法，遍历整棵树
                当我们找到一个叶子节点时，直接返回这个叶子节点的深度。
                广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小
        '''
        if not root:
            return 0
        queue = [root]
        res = 1 
        while queue:
            flags = False
            for i in range(len(queue)):
                temp = queue.pop(0)
                if not temp.left and not temp.right:
                    flags = True
                    break
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if flags:
                break
            else:
                res += 1
        return res
