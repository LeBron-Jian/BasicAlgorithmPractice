#_*_coding:utf-8_*_
'''
题目：
    剑指offer 32_2  从上到下打印二叉树

    从上到下打印二叉树的每个节点，同一层的节点按照从左到右的顺序打印。每层打印到一行

例如：
    给定二叉树: [3,9,20,null,null,15,7],

                3
               / \
              9  20
                /  \
               15   7

返回：
        [
          [3],
          [9,20],
          [15,7]
        ]



限制：
    0 <= 节点个数 <= 1000

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # queue = [root]
        queue = deque()
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                # node = queue.pop(0)
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(queue)
            res.append(temp)
        return res
