#_*_coding:utf-8_*_
'''
题目：
    106  根据中序遍历和后序遍历重构二叉树
    
根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

分治法的思想是：把原问题分解（Divide）成若干个与原问题结构相同
但规模更小的子问题，待子问题解决（Conquer）以后，再合并他们（Combine）原问题就得以解决
“归并排序”和“快速排序”都是分治法思想的应用，
其中归并排序先无脑地分，在合的时候就麻烦一下
快速排序开始在partition上花了很多时间，即在分上花了很多时间，然后递归处理就好了

'''
# 下面定义树的存储结构TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        rootNode = TreeNode(postorder[-1])  # 后续遍历最后一个值为根节点
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(postorder[-1])
        rootNode.left = self.buildTree(inorder[:mid], postorder[:mid])
        rootNode.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return rootNode
