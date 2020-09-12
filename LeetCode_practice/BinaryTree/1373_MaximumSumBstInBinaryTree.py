'''
1373  二叉搜索树的最大键值和
题目：
    给你一颗以 root为根的二叉树，请你返回任意二叉搜索树的最大键值和

二叉搜索树的定义如下：
    任意节点的左子树中的键值都小于此节点的键值
    任意节点的右子树中的键值都小于此节点的键值
    任意节点的左子树和右子树都是二叉搜索树

示例1：
                        1
                    /       \
                 4            3
              /    \        /   \
            2       4     2      5
                        /         \
                      4             6
输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。

示例2
                            4
                        /
                    3
                /     \
            1           2
输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。

示例 3：
输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。

示例 4：
输入：root = [2,1,3]
输出：6

示例 5：
输入：root = [5,4,8,3,null,6,3]
输出：7

提示：
    每棵树最多有 40000 个节点。
    每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        '''
        思路：
            当前节点为根的树是不是二叉搜索树和几个状态有关：
            1，左子树是不是二叉搜索树
            2，右子树是不是二叉搜索树
            3，当前 val 是不是大于左子树最大 val
            4，当前 val 是不是小于右子树最小 val
        我们确定 root 节点为根的树是不是二叉搜索树，需要其左右子树处理时返回四个值
            1，子树是不是二叉搜索树
            2，子树的最小值
            3，子树的最大值
            4，子树的sum值
        根据左右子节点返回值，构造当前节点的返回
        当左右子树的任意值为 FALSE，或者当前 val <= 左子树 或者 val >= 右子树 时
            返回 { false ，随意， 随意， 随意}
        如果判断当前树的搜索树，则返回 {true， 左子， 右子，val+左子+右子}
        另外注意的是null的处理，我们可以返回 {true int_max , int_min, 0}

        :param root:
        :return:

        dfs：在递归过程中记录每个节点所代表的子树的最大节点值，最小节点值，以及节点值的和
        是否满足搜索树。搜索数的判断在每个节点的逻辑为：
            判断左子树最大值是否小于当前节点（或者左子树不存在）
            右子树的最大值是否大于当前节点（或者右子树不存在）
            若满足则该子树为二叉搜索树
        '''
        self.res = 0

        def dfs(cur):
            if not cur:
                return [True, 0, 0]
            left = dfs(cur.left)
            right = dfs(cur.right)
            if left[0] and right[0] and (not cur.left or cur.val > left[1]) and (not cur.right or cur.val < right[2]):
                if cur.right:
                    tmp_max = right[1]
                else:
                    tmp_max = cur.val

                if cur.left:
                    tmp_min = left[2]
                else:
                    tmp_min = cur.val
                tmp_sum = left[3] + right[3] + cur.val
                self.res = max(self.res, tmp_sum)
                return [True, tmp_max, tmp_min, tmp_sum]
            # 【 是否是搜索树，最大值，最小值，所有节点的和】
            return [False, 0, 0, 0]
        dfs(root)
        return self.res


class Solution1:
    def maxSumBST(self, root: TreeNode) -> int:
        '''
        DFS 自底向上递归，通过辅助函数，把以前节点为根节点的二叉搜索树的键值和，上界，下界传出来
        值得注意的是：当前局部子树不满足二叉搜索树条件时，将上下界设置为恒不成立，一直回传
        :param root:
        :return:
        '''
        self.max_value = 0
        self.helper(root)
        return self.max_value
    def helper(self, root):
        # 返回三个变量，分别为【以当前节点为根节点的二叉搜索树的键值和，上界，下界
        if not root:
            return 0, 5e4, -5e4
        value1, min_value1, max_value1 = self.helper(root.left)
        value2, min_value2, max_value2 = self.helper(root.right)
        if max_value1 < root.val and min_value2 > root.val:
            # 则满足二叉搜索树条件
            self.max_value = max(self.max_value, value1+value2+root.val)
            return value1 + value2 + root.val, min(min_value1, root.val), max(max_value2, root.val)
        # 说明该节点无法构成二叉搜索树，返回恒不成立的条件，一直返回到顶
        return root.val, -5e4, 5e4










