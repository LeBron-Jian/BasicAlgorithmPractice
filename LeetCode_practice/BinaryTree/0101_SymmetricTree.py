# _*_coding:utf-8_*_
'''
   101  对称二叉树


    题目描述：给定一个二叉树，检查它是否镜像对称的
    例如，二叉树[1,2,2,3,4,4,3]是对称的。
        1
       / \
      2   2
     / \\ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
        1
       / \
      2   2
       \\   \
       3    3

    说明：如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        '''
        递归
        怎么判断一棵树是不是对称二叉树？ 如果所给根节点为空，那么是对称
                    如果不为空，当左右子树对称的时候，它对称
        如何知道左右子树对称呢？ 从图中我们发现，如果左树的左孩子和右树的右孩子一样
        并且左树的右孩子和右树的左孩子一样，则对称
        :param root: : TreeNode
        :return:  -> bool


        复杂度分析：
            时间复杂度为O(n)  因为要遍历n个结点
            空间复杂度O(H) 空间复杂度是递归的深度，也就是跟树的高度有关，最坏情况下树
                变为一个链表结构，高度为n
        '''

        def help(left, right):
            # left/right 都为空节点
            if not left and not right:
                return True
            # left/right 有一个为空
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            # 将左右字节对称递归比较
            return help(left.left, right.right) and help(left.right, right.left)

        return help(root.left, root.right) if root else True


    def isSymmetric1(self, root):
        '''
        迭代，层次遍历，然后检查每一层是不是回文数组
        :param root:  TreeNode
        :return: bool
        '''
        queue = [root]  # [[1, 2, 3, 4, 5]]
        # print(queue)
        while (queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)
            if layer != layer[::-1]:
                return False
            queue = next_queue
        return True


res = Solution()
print(res.isSymmetric1([1, 2, 3, 4, 5]))


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
            这里附上自己掌握的方法
        '''
        if not root:
            return True
        queue = [root]
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    temp.append(None)
                    continue
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            # print(temp, temp[::-1])
            if temp != temp[::-1]:
                return False
        return True
            




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
            队列实现：
            首先从队列中拿出两个节点left 和 right进行比较
            将left的left节点和 right的right节点放入队列
            将left的right节点和right的left节点放入队列


            时间复杂度为O(n)
            空间复杂度为O(n)
        '''
        if not root:
            return True
        q = []
        q.append(root.left)
        q.append(root.right)
        while len(q) != 0:
            L = q.pop(0)
            R = q.pop(0)
            if not L and not R:
                continue
            if not L or not R:
                return False
            if L.val != R.val:
                return False
            q.append(L.left)
            q.append(R.right)
            q.append(L.right)
            q.append(R.left)
        return True
