#_*_coding:utf-8_*_
'''
99：恢复二叉搜索树
题目：
二叉搜索树要求：每个节点都不比它左子树的任意元素小
    而且不比它的右子树的任意元素大

解题思路：
    中序遍历过程中，记录错误（两个错误排序节点）最后进行交换
    只需要中序遍历一遍就可以了。
    因为中序遍历，节点一定是递增的，所以通过比找出逆序对，就是被交换的节点
    有两种情况：1，中序遍历中，相邻两结点交换
                2，中序遍历中，非相邻节点交换

示例1：
输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2

示例2：
输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

进阶：使用O(n)空间复杂度的解法很容易实现
    可以想出一个只使用常数空间的解决方案吗？
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.res = []
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.mid(root)
        node1, node2 = None, None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i+1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i+1]
            elif self.res[i].val > self.res[i+1].val and node1 != None:
                node2 = self.res[i+1]
        node1.val, node2.val = node2.val, node1.val


    def mid(self, root):
        if root is not None:
            self.mid(root.left)
            self.res.append(root)
            self.mid(root.right)



class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def rootree():
    a = BiTreeNode("A")
    b = BiTreeNode("B")
    c = BiTreeNode("C")
    d = BiTreeNode("D")
    e = BiTreeNode("E")
    f = BiTreeNode("F")
    g = BiTreeNode("G")
    e.lchild, e.rchild = a, g
    a.rchild = c
    g.rchild = f
    c.lchild, c.rchild = b, d
    root = e
    return root

# print(rootree().lchild.data)

# 中序遍历
class solution:
    def __init__(self):
        self.res = []

    def run(self, root):
        self.mid_order(root)
        print(self.res)
        for i in range(len(self.res)):
            print(self.res[i].data)


    def mid_order(self, root):
        if root:
            # root.data
            self.mid_order(root.lchild)
            self.res.append(root)
            self.mid_order(root.rchild)


root = rootree()
print(root.data)
res = solution()
res.run(root)
