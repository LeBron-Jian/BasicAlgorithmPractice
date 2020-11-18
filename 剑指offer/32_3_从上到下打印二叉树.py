#_*_coding:utf-8_*_
'''
题目：
    剑指offer 32_3  从上到下打印二叉树

    请实现一个函数按照之字型顺序打印二叉树，即第一行按照从左到右的顺序打印
    第二行按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推

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
          [20, 9],
          [15,7]
        ]



限制：
    0 <= 节点个数 <= 1000

'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


