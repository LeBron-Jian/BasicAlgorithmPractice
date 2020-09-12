# _*_coding:utf-8_*_
'''
1038 从二叉搜索树到更大和树
题目：
    给出二叉搜索树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node
    的新值等于原树中大于或等于 node.val 的值之和

提醒一下，二叉搜索树满足下列约束条件：
    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。

示例：
    输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


提示：
    树中的节点数介于 1 和 100 之间。
    每个节点的值介于 0 和 100 之间。
    给定的树为二叉搜索树。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        其实二叉搜索树是一种排序树，通过中序遍历就可以按照从大到小或者从小到大的顺序访问节点
        我们对例子中的二叉树排序，发现：为1，2,3,4,5,6,7,8
        找规律，可以发现用反向中序遍历即可，然后使用一个全局变量记录累加和
        递归右，根，左节点即可。
        :param root:
        :return:
        '''
        self.sum = 0
        self.in_order(root)

        return root

    def in_order(self, root):
        if root:
            self.in_order(root.right)
            root.val = root.val + self.sum
            self.sum = root.val
            self.in_order(root.left)


class Solution1:
    def in_order(self, root):
        if root:
            self.in_order(root.right)
            root.val = self.temp = root.val + self.temp
            self.temp = root.val = root.val + self.temp
            self.in_order(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        递归右子树
        对当前节点操作
        递归左子树
        :param root:  [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
        :return:
        '''
        self.temp = 0
        self.in_order(root)
        return root
