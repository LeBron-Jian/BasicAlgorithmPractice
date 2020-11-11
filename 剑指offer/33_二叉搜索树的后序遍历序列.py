#_*_coding:utf-8_*_
'''
题目：
    剑指offer 33  二叉搜索树的后序遍历序列

    输入一个整数数组，判断该数组是不是某二叉搜索树的后续遍历结果。
    如果是则返回true，否则返回false，假设输入的数组的任意两个数字
    都互不相同。

    参考以下这棵二叉搜索树：
        5
     /    \
    2      6
  /  \
 1    3


 示例 1：
    输入: [1,6,3,2,5]
    输出: false

示例 2：
    输入: [1,3,2,6,5]
    输出: true

限制：
    0 <= 数组长度 <= 1000
'''
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        '''
            后序遍历定义： 左子树 右子树 根节点
            二叉搜索树定义：左子树的所有节点值小于根节点的值
                          右子树的所有节点的值大于根节点的值
    
            思路：
                运用递归的思想来不断的判断子树是否是一颗二叉搜索树，运用二叉搜索树的姓周
                左子树的节点值比根节点小，右子树的节点值比根节点的大，在一个后序遍历的序列中
                位于序列最后的点是根节点。

            算法流程：
                1，找到根节点，后序遍历中最后一个数
                2，划分左子树，从头开始遍历节点，直到我们遇到比根节点大或者根节点，之前
                    那些比根节点小的值是左子树的节点
                3，划分右子树，从左子树之后开始找，大于根节点的都是右子树，如果存在后面
                    的数字小于根节点，则不符合条件
                4，如果不存在右子树中比根节点小的，递归遍历上述左右子树
        '''
        if not postorder:
            return True
        def isBinarySearchTree(postorder):
            root = postorder[-1]
            length = len(postorder)
            # 找到左子树的区间，此时注意下这样的切分不可能出现左子树的节点比根节点大
            for i in range(length):
                if postorder[i] > root:
                    break
            # 如果右子树中存在比根节点小的值，那么是不符合条件的
            for j in rnage(i, length-1):
                if postorder[i] < root:
                    return False
            left = True
            if i>0:
                # 判断左子树是否符合条件
                left = isBinarySearchTree(postorder[:i])
            right = True
            if i < length-1:
                # 判断右子树是否符合条件
                right = isBinarySearchTree(postorder[i:-1])
            return left and right
        return isBinarySearchTree(postorder)


class Solution1:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        
        def isTree(postorder):
            if len(postorder) <=1:
                return True
            root = postorder[-1]
            length = len(postorder)
            for i in range(length):
                if postorder[i] > root:
                    break
    
            for j in range(i, length-1):
                if postorder[j] < root:
                    return False

            return isTree(postorder[:i]) and isTree(postorder[i:-1])
        return isTree(postorder)

for i in range(10):
    if i > 5:

        break
print(i)
