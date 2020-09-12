# _*_coding:utf-8_*_
'''
1382  将二叉搜索树变平衡
题目：
给你一颗二叉搜索树，请你返回一颗平衡后的二叉搜索树，新生成的树应该与原来的树有着相同的节点值
如果一颗二叉搜索树中，每个节点的两颗子树高度差不超过1，我们就称这棵二叉搜索树是平衡的。
如果有多种构造方法，请你返回任意一种
示例：
1
    \
        2
            \
                3
                    \
                        4

        2
    /       \
1               3
                    \
                        4

输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。

提示：

树节点的数目在 1 到 10^4 之间。
树节点的值互不相同，且在 1 到 10^5 之间。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        '''
        我的想法是首先，对 这个二叉搜索树进行中序遍历，然后取出最中间的值
        取根节点，为中心的点，然后再左右依次给予左右节点即可,就是重新建树
        即将排好序的数组通过二分的方案进行切分，中间的点是跟节点，左边是左子树
        右边是右子树，然后递归将左子树切分，右子树切分
        感觉是AVL树，但是我。。。。

        :param root:
        :return:
        '''

        def in_order(root):
            res = []
            if root:
                res += in_order(root.left)
                res.append(root.val)
                res += in_order(root.right)
        res = in_order(root)
        def rebuild(nums):
            length = len(nums)
            answer = None
            if length > 0:
                mid = length // 2
                answer = TreeNode(nums[mid])
                answer.left = rebuild(nums[:mid])
                answer.right = rebuild(nums[mid+1:])
            return answer
        return rebuild(res)


class Solution2:
    '''
    依然尝试了这种方法的函数外写，还是慢一些，但是我觉得这样好看一些。。。
    '''
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = self.in_order(root)
        return self.rebuild(res)


    def in_order(self, root):
        res = []
        if root:
            res += self.in_order(root.left)
            res.append(root.val)
            res += self.in_order(root.right)
        return res

    def rebuild(self, nums):
        length = len(nums)
        answer = None
        if length > 0:
            mid = length // 2
            answer = TreeNode(nums[mid])
            answer.left = self.rebuild(nums[:mid])
            answer.right = self.rebuild(nums[mid+1:])
        return answer

'''
效果对比：
    solution： 运行时间 296ms   内存消耗 19.8MB
    silution2: 运行时间 320ms   内存消耗 20MB
    
    
'''

'''
新方法：其实思路按照上面的想法，只是核心想法是在BST的构建
继续重述一遍步骤：
    1，中序遍历获得到排序好的结果
    2，将排好序的数组通过二分的方法进行切分，中间的点是根节点，
        左边是左子树，右边是右子树，然后递归将左子树切分，右子树切分
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.res = []
            self.mid_sort(root)
            return self.createBST(self.res, 0, len(self.res)-1)
    
    def mid_sort(self, root):
        if root:
            self.mid_sort(root.left)
            self.res.append(root)
            self.mid_sort(root.right)
    
    # 创建 BST
    def createBST(self, res, left_ind, right_ind):
        mid = (left_ind + right_ind) // 2
        mid_point = res[mid]
        mid_point.left = None
        mid_point.right = None
        if left_ind < mid:
            mid_point.left = self.createBST(res, left_ind, mid-1)
        if right_ind > mid:
            mid_point.right = self.createBST(res, mid+1, right_ind)
        return mid_point
        


