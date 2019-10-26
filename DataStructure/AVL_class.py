#_*_coding:utf-8_*_
from bst import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else :  # 插入的是g
            p.bf = 0
            c.bf = 0

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0

    def insert_no_rec(self, val):
        # 和 BST 一样，插入
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
                    node = p.lchild  # node节点存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return

        # 2，更新 balance factor
        while node.parent:  # node.parent不空
            if node.parent.lchild == node:  # 传递时从左子树来的，左子树更沉了
                # 更新node.parentde bf-=-1
                if node.parent.bf < 0:  # 原来node.parent.bf == - ,更新后变为-2
                    # 做旋转
                    # 看node那边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf >0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得：把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变为0
                    node.parent.bf = 0
                    break
                else:
                    # 原来node.parent.bf = 0 更新之后变为 -1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递时从右子树的，右子树更沉了
                # 更新node.parent.bf += 1
                if node.parent.bf >0:
                    # 原来node.parent.bf == 1, 更新之后变为2
                    # 做旋转 看node那边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        # node.bf = -1
                        n = self.rotate_left(node.parent, node)

                elif node.parent.bf < 0:
                    # 原来 node.parent.bf = -1,更新之后变为0
                    node.parent.bf = 0
                    break
                else:
                    # 原来 node.parent.bf = 0 更新之后变为1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = g
            if g:  # g不是空
                if node.parent == g.lchild:
                    g.lchild =n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
