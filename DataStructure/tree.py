#_*_coding:utf-8_*_

class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 'dir'  or ; 'file'
        self.children = []
        self.parent = None
        # 链式存储

    def __repr__(self):
        return self.name

'''
分析列表，假设hello目录下如何找到子目录world的目录呢？
n = Node('hello')
n2 = Node('world')
n.children.append(n2)

那，如何通过world目录找到父亲目录 hello呢？
n2.parent = n

那么这样做就相当于双链表
'''

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")  # 首先我们创建一个根目录
        self.now = self.root

    def mkdir(self, name):
        # 创建一个文件目录，所以我们必须保证name是以 /结尾，如果没有，我们就加
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        # 创建一个文件目录
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        # 展示当前文件夹下的文件
        return self.now.children

    def cd(self, name):
        # 切换到指定目录  注意：支持绝对路径和相对路径
        # 相对路径是从now的路径下开始，而绝对路径是从root路径下开始找
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                # 如果传入的目录名等于孩子的目录名，我们直接切换
                self.now = child
                return
        raise ValueError("invalid dir")


tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')
print(tree.ls())  # [var/, bin/, usr/]
tree.cd('bin/')
print(tree.ls())  # []
print(tree.root.children)  # [var/, bin/, usr/]