# _*_coding:utf-8_*_
'''
题目：
    105  从前序与中序遍历序列构造二叉树
    
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

前序遍历：遍历顺序：父节点-》左子节点->右子节点
中序遍历：遍历顺序：左子节点-》父节点-》右子节点
(先序遍历中的第一个元素一定是树的根，这个根又将中序序列分为左右两棵树
现在我们只需要将先序遍历的数组中删除根元素，
然后重复上面的过程处理左右两颗子树)

    我们会发现：前序遍历的第一个元素为根节点，
    而在中续遍历中，该根节点所在位置的左侧为左子树，右侧为右子树
    所以构建二叉树的本质问题就是：
    1，找到各个子树的根节点root
    2，构建该根节点的左子树
    3，构建该根节点的右子树
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        rootNode = TreeNode(preorder[0])  # 前序遍历第一个值为根节点
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        rootNode.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        rootNode.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return rootNode
