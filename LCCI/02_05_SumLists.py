#_*_coding:utf-8_*_
'''
    02.05  链表求和

    题目：给定两个用链表表示的整数，每个节点包含一个数位。这些数位是反向存放的，也就是
        个位排在链表首部。编写函数对这两个整数求和，并用链表形式返回结果。

示例：
    输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
    输出：2 -> 1 -> 9，即912


进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?


示例：
    输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
    输出：9 -> 1 -> 2，即912

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        move = head
        carry = 0
        while l1 or l2:
            '''
                x = l1.val if  l1 else 0
                y = l2.val if  l2 else 0
            '''
            if  l1:
                x = l1.val
            else:
                x = 0
            if  l2:
                y = l2.val
            else:
                y = 0
        
            res = x + y + carry
            move.next = ListNode(res%10)
            carry = res//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            move = move.next
        if carry == 1:
            move.next = ListNode(1)
        return head.next
