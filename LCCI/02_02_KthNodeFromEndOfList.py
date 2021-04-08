#_*_coding:utf-8_*_
'''
    02.02  返回倒数第 k 个节点

    题目： 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

示例：
    输入： 1->2->3->4->5 和 k = 2
    输出： 4


说明：
    给定的 k 保证是有效的。

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        former = latter = head
        for _ in range(k):
            former = former.next

        while head:
            former = former.next
            latter = latter.next
        return latter.val
    
    
    def kthToLast2(self, head: ListNode, k: int) -> int:
        count = 0
        move = head
        while move:
            count += 1
            move = move.next
        res = count - k
        for _ in range(res):
            head = head.next
        return head.val
