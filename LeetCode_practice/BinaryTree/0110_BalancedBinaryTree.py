# _*_coding:utf-8_*_
'''
题目：
      110  平衡二叉树


  给定一个二叉树，判断它是否是高度平衡的二叉树。
  本题中，一棵高度平衡二叉树定义为：
  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

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

示例3：
  输入：root = []
  输出：true

  平衡二叉树的定义：二叉树的每个节点的左右子树的高度差绝对值不超过1，则二叉树为平衡二叉树
  根据定义，一颗二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树，因此可以使用递归的方式判断
  二叉树是不是平衡二叉树，递归的顺序可以是自顶向下，或自底向上


方法一：从底至顶 ——提前阻断法
对二叉树做深度优先遍历DFS，递归过程中：
    终止条件：当DFS越过叶子节点时，返回高度0
    返回值：
        1，从底至顶，返回以每个节点root 为根节点的子树最大高度
        （左右子树中最大的高度值加1，max(left, right)+1)
        2，当我们发现有一例  左/右子树高度差 > 1 的情况时，代表此树不是平衡树，返回-1
    当发现不是平衡树时，后面的高度计算都没有意义了，因此一路返回 -1 避免后续多余计算。

最差的情况是对树做以便完整DFS，时间复杂度为o(N)

方法二，从顶至底 暴力法
构造一个获取当前节点最大深度的方法 depth()，通过比较左右子树最大高度差
abs(self.depth(root.left)- self.depth(root.right)) 来判断以此为根节点下是否是二叉平衡树
从顶至底DFS，以每个节点为根节点，递归判断是否是平衡二叉树：
    若所有根节点都满足平衡二叉树性质，则返回TRUE
    若其中任何一个节点作为根节点时，不满足平衡二叉树性质，则返回FALSE
此方法产生大量重复的节点访问和计算，最差情况下时间复杂度 O(N**2)

平衡二叉树：遍历每一节点对应的左右子树的高度，判定其是否符合条件，
只要发现其不符合，立即退出，判定其不是平衡二叉树；
反之，若一直都符合条件，那我们可以说他就是平衡二叉树

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
          此解是本题的最优解，但是剪枝的方法不容易想到
          实现是对二叉树做后序遍历，从底至顶返回子树深度，若判定某子树不是平衡树
          则剪枝，直接向上返回

          递归的终止条件：
            1，当root为空，说明越过叶子节点，因此返回高度0
            2，当左右子树深度为-1，代表此树的左右子树不是平衡树，因此剪枝，直接返回-1
        '''
        return self.depth(root) != -1

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        if left == -1:
            return -1
        right = self.depth(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
          此方法容易想到，但是会产生大量重复计算，时间复杂度较高
          思路是构造一个获得当前子树的深度的函数 ，通过比较某子树的左右子树的
          深度差是否成立，来判断某子树是否是二叉平衡树，若所有子树都平衡，则此树平衡

          返回值：判断当前子树是否为平衡树
                 先序遍历递归，判断当前子树的左子树是否是平衡树
                 先序遍历递归，判断当前子树的右子树是否是平衡树
        '''
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
