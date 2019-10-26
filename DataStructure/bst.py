# _*_coding:utf-8_*_
import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):
        # 第一种情况：node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是他父亲的左孩子
            node.parent.lchild = None
            node.parent = None  # 可以不写
        else:  # node是他父亲的右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2.1:node只有一个孩子，且为左孩子
        if not node.parent:  # 根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # node 是它父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：node只有一个孩子，且为右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:  # 不存在
                return False
            if not node.lchild and not node.rchild:  # 1，叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 2.1 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 2.2 只有一个右孩子
                self.__remove_node_22(node)
            else:
                # 3,两个孩纸都有
                min_node = node.rchild
                while min_node.lchild:  # 有左孩子
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


    def printTree(self, root):
        # 打印二叉搜索树（中序打印，有序数列—）
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end=',')
        self.printTree(root.right)

# 删除
tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
tree.in_order(tree.root)
print(" ")
tree.delete(4)
tree.delete(1)
tree.delete(8)
tree.in_order(tree.root)

'''
# 插入操作
tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print(" ")
tree.in_order(tree.root)
print(" ")
tree.post_order(tree.root)
print(" ")
'''
4, 2, 1, 3, 6, 5, 7, 9, 8,
1, 2, 3, 4, 5, 6, 7, 8, 9,
1, 3, 2, 5, 8, 9, 7, 6, 4,
'''

# 查询操作
li = list(range(0, 500, 2))
random.shuffle(li)

tree = BST(li)
print(tree.query_no_rec(4).data)
# 4

'''
