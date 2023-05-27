#_*_coding:utf-8_*_
'''
    剑指offer  54   二叉搜索树的第k大节点

    给定一颗二叉搜索树，请找出其中第k大的节点。

示例 1:
    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 4


示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 4


限制：
    1 <= k <= 二叉搜索树元素个数
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        '''a
            想法：直接中序遍历，找倒数第k个结点即可。
            或者将排序好的数组翻转，找第k个结点即可。
        '''
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)
        # print(res)
        return res[len(res)-k]

    def kthLargest1(self, root: TreeNode, k: int) -> int:
        '''
            改进：二叉搜索树的中序遍历为递增序列，所以二叉搜索树第k大
            节点可转换为此树中序遍历倒数第k个结点。
            所以为了求第k个结点，我们不需要全部遍历，只需要做如下事情：
                1，递归遍历时计数，统计当前节点的序号
                2，递归到第k个节点时，应记录结果res
                3，记录结果后，后续的遍历即失去意义，应该提前终止。

            复杂度分析：
                时间复杂度O(n)：当树退化为链表时（全部为右子节点），无论
                    k的值大小，递归深度都为n
                空间复杂度O(n)：当树退化为链表时（全部为右子节点），系统
                    使用O(n)大小的栈空间。

            题目说：1<=k<=N，所以无需考虑k大于总节点的情况
                如果考虑，可以在中序遍历完成后，判断k>0，若成立说明k>N
        '''
        def inorder(root):
            if root:
                inorder(root.right)
                if self.k == 0:
                    return
                self.k -= 1
                if self.k == 0:
                    self.res = root.val
                inorder(root.left)
        self.k = k
        inorder(root)
        return self.res
