# _*_coding:utf-8_*_
'''
面试题02.03  删除中间节点
题目：
    实现一种算法，删除单向链表中间某个节点（即不是第一个或最后一个节点）
    假定你只能访问该节点

示例：
    输入：单向链表a->b->c->d->e->f中的节点c
    结果：不返回任何数据，但该链表变为a->b->d->e->f

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode1(self, node):
        """
        这个题的核心实现就是把node的下一位的值覆盖给node，然后跳过node的下一位
        因为我们无法访问到head节点，所以除了直接从node开始往下找，其他都是不现实的
        即：
            （注意：首先把当前值变为d，即把c变为d，存在两个 d
            a->b->c->d->e->f 变为 a->b->d->d->e->f
            然后把第一个d的next设为e，跳过第二个d（我们需要跳过第二个d）

        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def deleteNode11(self, node, n):
        '''
        对上面代码的改进，防止报错，如给了当前节点的值 current.val
        不过思路都是一样，用当前节点取代下一个节点，跳过下一个节点
        :param node:
        :return:
        '''
        while True:
            if node.val == n:
                node.val = node.next.val
                node.next = node.next.next
                break
            else:
                node = node.next
