#_*_coding:utf-8_*_
'''
题目：
    剑指offer 55-1  二叉树的深度

    输入一颗二叉树的根节点，求该树的深度。从根节点到叶子节点依次经过的节点（包含根，叶子节点）形成树
    的一条路径，最常路径的长度为树的深度。

    例如：给定二叉树 [3,9,20,null,null,15,7]
     
        3
       / \
      9  20
        /  \
       15   7

    返回它的最大深度 3


提示：
    节点总数 <= 10000


        树的遍历方式总体分为两类，深度优先搜索（DFS） ，广度优先搜索（BFS）
        常见的DFS：pre-order in-order post-order
        常见的BFS：level-order

        求树的深度需要遍历树的所有节点，下面学习后序遍历DFS和层次遍历BFS 两种遍历
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
            后序遍历（DFS）

            树的后续遍历，深度优先搜索往往利用递归或栈实现，下面使用递归实现

            关键点：此树的深度和其左（右）子树的深度之间的关系。显然，此树的深度等于
            左子树的深度与右子树的深度中的最大值 +1

            算法解析：
                1，终止条件：当root为空，说明已越过叶子节点，因此返回深度0
                2，递推工作：本质上是对树做后序遍历
                    1，计算节点root的左子树的深度，即调用 maxDepth(root.left)
                    2，计算节点root的由子树的深度，即调用maxDepth(root.right)
                3，返回值：返回此树的深度，即 max(maxDepth(root.left), maxDepth(root.right)) + 1

            复杂度分析：
                时间复杂度O(n): n为树的节点数量，计算树的深度需要遍历所有节点
                空间复杂度O(n)：最差情况下，即树退化为链表时，递归深度可达n
        '''
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(rot.right)) + 1


class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        '''
            层次遍历（BFS）
            树的层次遍历，广度优先搜索往往利用队列实现
            关键点：每遍历一层，则计数器+1，直到遍历完成，则可以得到树的深度

            算法解析：
                1，特例处理：当root为空，直接返回深度0
                2，初始化：队列q（加入根节点root），计数器 res=0
                3，循环遍历：当 queue 为空时跳出
                    1，初始化一个空列表temp，用于临时存储下一层节点
                    2，遍历队列：遍历queue中的各节点 node，并将其左子节点和右子节点加入 temp
                    3，更新队列：执行 queue = temp，将下一层节点赋值给 queue
                    4，统计层数：执行 res +=1，代表层数+1

            复杂度分析：
                时间复杂度：O(n)   n为树的节点数量，计算树的深度需要遍历所有节点
                空间复杂度：O(n)   当树平衡时，队列queue同时存储 n/2 个节点
        '''
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            res += 1
        return res
