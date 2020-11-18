#_*_coding:utf-8_*_
'''
    题目：  102  二叉树的层次遍历（按层打印）

    给定一个二叉树，返回其按层次遍历的节点值。
    （即逐层地，从左到右访问所有节点）。

例如:
    给定二叉树: [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
    返回其层次遍历结果：
        [
          [3],
          [9,20],
          [15,7]
        ]

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
        '''
            最简单的解法就是递归，首先确认树非空，然后调用递归函数，参数是当前节点和节点的层次
            输出列表称为 levels，当前最高层数就是列表的长度len(levels)
            比较访问节点所在的层次 level 和当前最高层次 len(levels)的大小，
            如果前者更大就向levels添加一个空列表。
            将当前节点插入到对应层的列表 levels[level]中
            递归非空的孩子节点  helper(node.left / node.right, level + 1)
            :param root:
            :return:
            '''
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node val
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        '''
        上述的递归方法也可以写成迭代的形式
        我们将树上顶点按照层次一次放入队列结构中，队列中的元素满足先进先出的原则
        在Python中如果使用Queue结构，可以使用Python库函数deque中的append和popleft
        :param root:
        :return:

        第0层只包含根节点root，实现算法如下：L
        当对垒非空的时候：
            在输出结果levels中插入一个空列表，开始当前层的算法
            计算当前层有多少个元素：等于队列的长度
            将这些元素从队列中弹出，并加入levels当前层的空列表中
            将他们的孩子节点作为下一层亚茹队列中
            进入下一层level++
        '''
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1
        return levels



from collections import deque
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
            自己写的。。。
        '''
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
