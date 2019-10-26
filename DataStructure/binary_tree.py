#_*_coding:utf-8_*_

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e
# print(root.lchild.rchild.data)

# 二叉树的前序遍历
def pre_order(root):
    if root:
        print(root.data)  # 先打印根节点
        pre_order(root.lchild)
        pre_order(root.rchild)

# pre_order(root)
'''
E
A
C
B
D
G
F
'''

# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data)
        in_order(root.rchild)

# in_order(root)
'''
A
B
C
D
E
G
F
'''

# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data)

# post_order(root)
'''
B
D
C
A
F
G
E
'''

from collections import deque

def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()
        print(node.data)
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

level_order(root)
'''
E
A
G
C
F
B
D
'''