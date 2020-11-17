# _*_coding:utf-8_*_
'''
题目： 104  二叉树的最大深度

    给定一个二叉树，找出其最大深度。

    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

    说明: 叶子节点是指没有子节点的节点。

示例：
    给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

'''


# 首先给出我们将要使用的树的节点，TreeNode的定义
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
            层次遍历，level order 
        '''
        levels = []
        if not root:
            return len(levels)

        def helper(node, level):
            if len(levels) == level:
                levels[level].append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return len(levels)

    def maxDepth1(self, root):
        if not root:
            return 0
        queue, res = [root], 0
        while len(queue) !=0:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = tmep
            res += 1
        return res

    def maxDepth2(self, root: TreeNode) -> int:
        '''
        下面通过递归来解决问题，这里使用了深度优先搜索策略的示例
        我们每个节点只访问一次，因此时间复杂度为O(N)
        空间复杂度：在最糟糕的情况下，树是完全不平衡的，
        例如每个结点只剩下左子结点，递归将会被调用 NN 次（树的高度），
        因此保持调用栈的存储将是 O(N)。但在最好的情况下（树是完全平衡的），
        树的高度将是 log(N)。
        因此，在这种情况下的空间复杂度将是 O(n)。

        树的后序遍历

        :param root:
        :return:
        '''
        if root is None:
            return 0
        else:
            left_height = self.maxDepth1(root.left)
            right_height = self.maxDepth1(root.right)
            return max(left_height, right_height) + 1


    def maxDepth3(self, root: TreeNode) -> int:
        '''
        时间复杂度：O(N)O(N)。
        空间复杂度：O(N)O(N)。
        :param root:
        :return:
        '''
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1), root.left)
                stack.append((current_depth+1), root.right)
        return depth
