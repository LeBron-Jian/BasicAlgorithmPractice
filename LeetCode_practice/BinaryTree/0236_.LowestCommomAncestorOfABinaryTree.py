#_*_coding:utf-8_*_
'''
题目：
    236  二叉树的最近公共祖先

    给定一个二叉搜索树，找到该树中两个指定节点的最近公共祖先
    最近公共祖先的定义为：对于有根树T的两个节点p，q，最近公共祖先
    表示为一个结点x，满足x是p,q的祖先且x的深度尽可能大（一个节点也
    可以是它自己的祖先）

    例如：给定如下二叉搜索树： root = [3,5,1,6,2,0,8,null,null,7,4]

            3
          /   \
        5      1
      /  \\   /  \\
     6    2   0    8
        /  \\
       7    4

示例 1:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出: 3
    解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出: 5
    解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。




'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            祖先的定义：若节点p在节点root的左/右子树中，或者p=root，则称root 是p的祖先

            最近公共祖先的定义：设节点root为节点p,q的某公共祖先，若其左子节点root.left 和右子节点
                        root.right都不是p和q的公共祖先，则称root是“最近的公共祖先”
            根据以上定义，若root是p,q的最近公共祖先，则只可能为以下情况之一：
                1，p和q 在root的子树中，且分列root的异侧，（即分别在左，右子树中）
                2，p=root，且q在root的左子树或右子树中
                3，q=root，且p在root的左子树或右子树中
            考虑通过递归对二叉树进行后续遍历，当遇到节点p和q时返回，从底到顶回溯，当节点p,q在节点root的
            异侧时，节点root为最近公共祖先，则向上返回root

            递归解析：
            1，终止条件：
                1，当越过叶子节点，直接返回null
                2，当root等于p,q，则直接返回root
            2，递推工作：
                1，开启递归左子节点，返回值记为 left
                2，开启递归右子节点，返回值记为 right
            3，返回值：
                根据left和right可分为四种情形：
                    1，当left和right同时为空，说明root的左右子树都不包含p,q，则返回null
                    2，当left和right同时不为空，说明p,q在root的异侧，所以root为最近公共祖先，返回root
                    3，当left为空，right不为空，p,q都不在root的左子树，直接返回right，具体可分两种情况：
                        1，p,q其中一个在root的右子树中，此时right指向p（假设为p)
                        2，p,q两节点都在root的右子树中，此时的right指向最近公共祖先节点
                    4，当left不为空，right为空，与情况3同理


            复杂度分析：
                时间复杂度O(n)：其中n为二叉树节点数，最差情况下，需要递归遍历树的所有节点
                空间复杂度O(n)：最差情况下，递归深度达到N，系统使用O(n)大小的额外空间

        '''
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            情况1,2,3,4 展开写法如下
        '''
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)

        if not left and not right:
            return        # 情况1
        if not left:
            return right  # 情况3
        if not right:
            return left   # 情况4  
        return root       # 情况2，if left and right
