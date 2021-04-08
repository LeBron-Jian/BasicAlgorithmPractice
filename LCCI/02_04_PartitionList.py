#_*_coding:utf-8_*_
'''
    02.04  分割链表

    题目：编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
        如果链表中包含 x ，x 只需出现在小于 x 的元素之后（如下所示）。分割元素 x 只需处
        于 “右半部分”即使，其不需要被置于左右两部分之间。


示例：
    输入: head = 3->5->8->5->10->2->1, x = 5
    输出: 3->1->2->10->5->5->8
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
            直观来说，我们只需要维护两个链表 small，large。
            small 链表按顺序存储所有小于 x 的节点。
            large 链表按顺序存储所有大于等于 x 的节点。
            遍历完原链表后，我们只要将 small 链表尾节点指向 large链表的头节点
            即能完成对链表的分割。
            为了实现其思路，我们设 smallHead，largeHead 分别为两个链表的哑节点。
            即他们的 next 指针指向链表的头节点。
        '''
        small, large = ListNode(0), ListNode(0)
        smallmove, largemove = small, large
        while head:
            if head.val < x:
                smallmove.next = head
                smallmove = smallmove.next
            else:
                largemove.next = head
                largemove = largemove.next
            head = head.next
        largemove.next = None
        smallmove.next = large.next
        return small.next
