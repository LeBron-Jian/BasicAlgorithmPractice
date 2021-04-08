#_*_coding:utf-8_*_
'''
    02.03  删除中间节点

    题目：实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），
        假设你只能访问该节点。


示例：
    输入：单向链表a->b->c->d->e->f中的节点c
    结果：不返回任何数据，但该链表变为a->b->d->e->f
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
            这个题的核心就是把 node 的下一位覆盖给 node，然后跳过 node 的下一位。
            因为我们无法访问到 head 节点，所以除了直接从 node 开始往下找，其他都是
            不现实的。
            :type node: ListNode
            :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
