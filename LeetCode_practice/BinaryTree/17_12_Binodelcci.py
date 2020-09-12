# _*_coding:utf-8_*_
'''
面试题17.12 BiNode
题目：
    二叉树数据结构 TreeNode 可用来表示单向链表（其中left置空，right为下一个链表节点）
    实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，
    转换操作应为原址的 也就是在原始的二叉搜索树上直接修改。    
    返回转换后的单向链表的头节点。

示例：
    输入： [4,2,5,1,3,null,6,0]
    输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：
    节点数量不会超过10000
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        '''
        二叉搜索树的中序遍历是有序的，所以我们只要对树进行中序遍历即可。
        利用一个前驱节点prev，记录上一个被处理的节点，当节点被遍历到的时候，
        将 prev.right指向当前节点 node，然后 node.left置空，prev指针后移动到node
        最后 node进入右子树即可
        （中序遍历：递归）
        中序遍历二叉搜索树，就相当于从小到大遍历这些节点
        对于遍历到的每个节点，将其左子树置空，右孩子置为下一个节点

        注意下面代码有问题：时间复杂度太高，会超时
        # 最后发现自己的问题：
        将 self.prev.left = None  修改为 root.left = None 即可
        可能测试的用例：[4,2,5,1,3,null,6,0] 比较短，所以没出问题，还以为是对的
        :param root:
        :return:
        '''

        def in_order(root):
            if root:
                in_order(root.left)
                # 将当前节点的左子节点置为空
                root.left = None
                # 上个节点的右子节点赋值为当前节点
                self.prev.right = root
                # 更新当前节点，注意顺序
                self.prev = root
                in_order(root.right)
        # 定义头节点，最后返回头节点的右子节点
        self.start = self.prev = TreeNode(-1)
        in_order(root)
        print(self.prev.left)
        return self.start.right

class solution:

    def convertBiNode(self, root):
        '''
        所以修改代码如下：下面代码可以运行
        :param root:
        :return:
        '''
        # 定义头节点，最后返回头节点的右子节点
        self.head = self.current = TreeNode(None)
        self.in_order(root)
        return self.head.right

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            # 将当前节点的左子节点置空
            root.left = None
            # 上个节点的右子节点赋值为当前节点
            self.current.right = root
            # 更新当前节点，注意顺序
            self.current = root

            self.in_order(root.right)

import time

class solution1:
    def __init__(self):
        self.res = []

    def test1(self):
        starttime = time.time()

        def add():
            for i in range(100000):
                self.res.append(i)
            return self.res
        add()
        stoptime = time.time()
        return stoptime-starttime

    def test2(self):
        starttime = time.time()
        self.add()
        stoptime = time.time()
        return stoptime-starttime

    def add(self):
        for i in range(100000):
            self.res.append(i)
        return self.res

res = solution1()
print(res.test1())
print(res.test2())
'''
0.009999990463256836
0.019999980926513672

做这个测试的目的是，看我们函数中序遍历函数写在里面好，还是外面
从这个测试我们发现，写在里面耗时比较短，然后我在LeetCode提交也发现了
写在里面的运行时间为：120ms  内存消耗为 20.3MB
写在外面的运行时间为：128ms  内存消耗为  20.3MB
所以写在里面快一些。。
'''

'''
下面这种方法还是中序遍历，只不过巧妙的实现了O(1)空间
不过个人不太习惯这种风格。。。。但是不失为一种好方法
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def convert(root):
            begin=end=root
            if root:
                if root.left:
                    begin, end = convert(root.left)
                    end.right = root
                    end = root
                    root.left=None
                if root.right:
                    root.right, end = convert(root.right)
            return begin, end
        return convert(root)[0]

