# _*_coding:utf-8_*_
'''
题目： 
        94   二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？



递归就是左根右

在树的深度优先遍历中（包括前序，中序，后续遍历）递归方法是最直观易懂的
但是考虑到效率，我们通常不推荐使用递归

栈迭代方法虽然提高了效率，但是起嵌套循环却非常烧脑，不易理解，容易造成一看就懂，一写就废
的情况，而且对于不同顺序的遍历，循环结构差异很大，更增加了记忆负担。

下面学习一种颜色标记法，兼具栈迭代方法的高效，又像递归方法一样简洁易懂
更重要的是，这种方法对于前序，中序，后序遍历，能够写出完全一致的代码

官方解题中有三种方法来完成树的中序遍历：
    1，递归
    2，借助栈的迭代方法
    3，莫里斯遍历

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        递归
            时间复杂度为 O(n)
            空间复杂度为 O(n)

            递归可以解决问题，但是考虑到效率，我们通常不推荐使用递归
        :param root:
        :return:
        '''
        res = []

        def helper(root):
            if not root:
                return
            if root:
                helper(root.left)
                res.append(root.data)
                helper(root.right)

        helper(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        '''
        迭代  通过栈
            时间复杂度为 O(n)
            空间复杂度为 O(n)

            但是栈有个问题，虽然栈提高了效率，但是嵌套循环非常烧脑，不易理解，容易造成一看就懂
            一写就废的情况，而且对不不同的遍历顺序（前序，中序，后续）循环结构差异很大，更增加
            了记忆负担。
        :param root:
        :return:
        '''
        res = []
        stack = []
        p = root  # 用p当做指针
        while p or stack:
            while p:  # 把左子树压入栈中
                stack.append(p)
            # 输出栈顶元素
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res


    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        '''
        其核心思想如下：
            使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色
            如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点，自身，左子节点依次入栈
            如果遇到的节点为灰色，则将节点的值输出。
        :param root:
        :return:
        '''
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, GRAY)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
