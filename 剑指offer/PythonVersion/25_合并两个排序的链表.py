    #_*_coding:utf-8_*_
'''
题目：
    剑指offer 25  合并两个排序的链表

    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的

示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

限制：
    0 <= 链表长度 <= 1000  

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
            递归
        '''
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
            迭代
                当l1和l2都不是空链表的时候，判断l1和l2哪一个链表的头节点的值更小
                将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表
                中的节点向后移一位。
            复杂度分析：
                时间复杂度为O(n+m)  其中m和n分别代表两个链表的长度
                空间复杂度为O(1)  我们只需要常数的空间存放若干变量

            我们可以创建一个结果节点，作为链表的开头，因此是不能移动的
            所以我们需要设置一个动量，一直移动，完成使命
        '''
        resnode = ListNode(0)
        move = resnode
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                move = move.next
                l1 = l1.next
            else:
                move.next = l2
                move = move.next
                l2 = l2.next
            # move = move.next
        if l1:
            move.next = l1
        else:
            move.next = l2
        return resnode.next
