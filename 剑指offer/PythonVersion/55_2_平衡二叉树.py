#_*_coding:utf-8_*_
'''
题目：
    剑指offer 55-2  平衡二叉树

    输入一颗二叉树的根节点，判断该树是不是平衡二叉树，如果某二叉树中任意节点的
    左右子树的深度相差不超过1，那么它就是一颗平衡二叉树

示例 1:
    给定二叉树 [3,9,20,null,null,15,7]

        3
       / \
      9  20
        /  \
       15   7
    返回 true 。

示例 2:
    给定二叉树 [1,2,2,3,3,null,null,4,4]

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    返回 false 。


提示：
    节点总数 <= 10000


此树的深度等于左子树的深度与右子树的深度中最大值 +1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
            后序遍历 + 剪枝  从底至顶

            此方法为本题的最优解法，但是剪枝的方法不容易第一时间想到

            思想是对二叉树做后序遍历，从底至顶返回子树的深度，若判断某子树不是
            平衡树则剪枝，直接向上返回。

            算法流程：
            recur(root)函数：
                返回值：
                    1，当节点root左右子树的深度差<1，则返回当前子树的深度，即节点
                        root的左右子树的深度最大值 +1，
                    2，当节点root 左右子树的深度差>2，则返回-1，代表此子树不是平衡树
                终止条件：
                    1，当root为空：说明越过叶子节点，因此返回高度0
                    2，当左右子树深度为-1，代表此树的左右子树不是平衡树，因此剪枝，直接返回-1
            isBalanced(root)函数：
                返回值：若recur(root) !=-1，则说明此树平衡，返回True，否则返回False

            复杂度分析：
                时间复杂度O(n) n为树的节点数，最差情况下，需要递归遍历树的所有节点
                空间复杂度O(n) 最差情况下（树退化为链表时），系统递归需要使用O(n)的栈空间     
        '''
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1

        return recur(root) != -1

class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
            先序遍历 + 判断深度（从顶至底）

            思想是构造一个获取当前子树的深度的函数 depth(root)，通过比较某子树
            的左右子树的深度差 abs(depth(root.left) - depth(root.right)) <=1 是否成立
            来判断某子树是否是二叉平衡树。若所有子树都平衡，则此树平衡。

            算法流程：
            isBalanced(root) 函数： 判断树root是否平衡
                特例处理：若树根节点root为空，则直接返回True
                返回值：
                    所有子树都需要满足平衡树性质，因此以下三者使用与逻辑 & 连接
                    1，abs(self.depth(root.left) - self.depth(root.right)) <=1:
                        判断当前子树是否平衡树
                    2，self.isBalanced(root.left)：先序遍历递归，判断当前子树的左子树
                        是否平衡树
                    3，self.isBalanced(root.right)：先序遍历递归，判断当前子树的右子树
                        是否平衡树

            depth(root) 函数：计算树root的深度
                终止条件：当root为空，即越过叶子节点，则返回高度0
                返回值：返回左/右子树的深度的最大值 +1

            复杂度分析：
                时间复杂度O(nlogn)
                空间复杂度O(n)   
        '''
        if not rot:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <=1 and 
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        return max(self.depth(root.left), self.depth(root.right)) + 1
