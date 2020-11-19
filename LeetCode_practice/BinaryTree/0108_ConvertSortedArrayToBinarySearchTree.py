#_*_coding:utf-8_*_
'''
题目：  108  将有序数组转换为二叉搜索树


    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:
    给定有序数组: [-10,-3,0,5,9],
    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

                      0
                     / \
                   -3   9
                   /   /
                 -10  5


    在这里，我们可能需要先理解什么是二叉搜索树
        二叉搜索树就是特殊的二叉树，他的要求就是每个节点都不比它左子树的任意元素小
        而且不必它的右子树的任意元素大。  简单来说就是右子树总大于左子树的节点

    二叉搜索树的性质：
        若左子树不为空，则左子树上所有节点值均小于或等于它的根节点的值
        若右子树不为空，则右子树上所有节点值均大于或等于它的根节点的值
        左右子树也分别为二叉搜索树

    二叉搜索树，注意树中元素的大小，二叉搜索树可以方便的实现搜索算法
        在搜索元素x的时候，我们可以将x和根节点比较
        如果x等于根节点，那么找到x，停止搜索，
        如果x小于根节点，那么搜索左子树
        如果x大于根节点，那么搜索右子树

    所以平衡二叉搜索树需要保证两点
        1，根节点大于左子树任意节点，小于右子树任意节点
        2，左右子树高度相差不超过1



        二叉搜索树的中序遍历是升序序列，题目给定的数组是按照升序排序的有序数组，因此可以确保
    数组是二叉搜索树的中序遍历序列。
        给定二叉搜索树的中序遍历，是否可以唯一的确定二叉搜索树，答案是否定的。如果没有要求二叉
    搜索树的高度平衡，则任何一个数字都可以作为二叉搜索树的根节点，因此可能的二叉搜索树有多个。
        如果增加一个限制条件，即要求二叉搜索树的高度平衡，是否可以唯一的确定二叉搜索树，答案
    仍然是否定的。
        直观的看，我们可以选择中心数字作为二叉搜索树的根节点，这样分给左右子树的数字个数相同或
    只相差1，可以使得树保持平衡，如果数组长度是奇数，则根节点的选择是唯一的，如果数组长度是偶数
    则可以选择中间位置左边的数字作为根节点或者选择中间位置右边的数字作为根节点，选择不同的数字
    作为根节点则创建的平衡二叉搜索树也是不同的。

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        根据此题，一个可行的递归条件可以得出：
        1，每次返回的根节点处于数组中间，以其左右半数组分别递归构造左右子树
        2，那么就意味着左子树小于根，右子树大于根，
        且所有节点左右子树节点相差不超过1，
        （由于递归的构造树的方式相同，所有节点都满足高度平衡）
        :param nums:
        :return:
        '''
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sortedArrayToBST, [nums[:m], nums[m+1:]])
            return r

    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        '''
        将有序数组转换成二叉搜索树
        算法思路：
        1，特殊情况：有序数组为空直接返回空树，Python使用None表示
        2，有序数组不空，递归解决问题
            1，获取有序数组的中间元素，并以其值作为实参构造二叉树的根节点
            2，以中间元素左边的数据为实参构造二叉树作为根节点的左子树
            3，以中间元素右边的数据为实参构造二叉树作为根节点的右子树
        :param nums:
        :return:

        时间复杂度 O(N) 其中N为列表中元素个数
        空间复杂度  O(logN)
        '''
        def construct(start, end):
            middle = (start + end) >> 1
            p = TreeNode(nums[middle])
            if middle > start:
                p.left = construct(start, middle-1)
            if middle < end:
                p.right = construct(middle + 1, end)
            return p

        if not nums:
            return None
        n = len(nums)
        return construct(0, n-1)

    def sortedArrayToBST3(self, nums: List[int]) -> TreeNode:
        '''
            所以有三种方法：
                1，总是选择中间位置左边的数字作为根节点
                2，总是选择中间位置右边的数字作为根节点
                3，两种方法的结合，选择任意一个中间位置数字作为根节点

            复杂度分析：
                时间复杂度：O(n)
                空间复杂度：O(logn) 
        '''
        if len(nums) == 0:
            return None
        # if len(nums) == 1:
        #     return TreeNode(nums[0])
        # if len(nums) == 2:
        #     left = TreeNonde(nums[0])
        #     root = TreeNonde(nums[1])
        #     root.left = left
        #     return root
        mid = len(nums)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST3(nums[:mid])
        root.right = self.sortedArrayToBST3(nums[mid+1:])
        return root
