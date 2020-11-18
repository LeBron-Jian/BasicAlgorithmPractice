#_*_coding:utf-8_*_
'''
    题目  103  二叉树的锯齿形层次遍历


  给定一个二叉树，返回其节点值的锯齿形层次遍历。
  （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
  给定二叉树 [3,9,20,null,null,15,7],

      3
     / \
    9  20
      /  \
     15   7
  返回锯齿形层次遍历如下：

  [
    [3],
    [20,9],
    [15,7]
  ]

'''
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            if level%2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return levels


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
            从上到下打印二叉树，感觉很easy
        '''
        if not root:
            return []
        res = []
        queue = [root]
        i = 0
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(queue)
            if i%2 == 0:
                res.append(temp)
            else:
                temp.reverse()
                res.append(temp)
            i+=1
        return res


