# _*_coding:utf-8_*_
'''
剑指offer 22：链表中倒数第k个结点
题目：
    输入一个链表，输出该链表中倒数第k个结点。为了符合大多数的习惯。
    本题从1开始计数，即链表的尾结点为倒数第一个节点。例如，一个链表
    有六个节点，从头开始，他们的值一次为1,2,3,4,5,6，这个链表的倒数
    第3个节点的值为4的节点

示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        '''
        双指针两步走：
            先遍历统计链表长度，记为n
            设置一个指针走 n-k步，即可找到链表倒数第k个结点
        而且使用双指针不用统计链表长度
        算法流程：
            1，初始化：前指针 former，后指针latter，双指针都指向头结点head
            2，构建双指针距离：前指针former先向前走k步（结束后，双指针之间
                差k步）
            3，双指针共同移动：循环中，双指针former和latter每轮都向前走一步
                直到former走过链表尾节点时跳出（跳出后，latter与尾节点距离为
                k-1，即latter指向倒数第k个结点
            4，返回值：返回latter即可
        :param head:
        :param k:
        :return:
        复杂度分析：
            时间复杂度为O(n)：n为链表长度，总体看，former走了N步，latter走了（N-k）步
            空间复杂度为O(1)：双指针 former，latter使用常数大小的额外空间
        '''
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

    def getKthFromEnd11(self, head: ListNode, k: int) -> ListNode:
        '''
        对上问题，如果考虑到越界，也就是k大于链表的长度，则可以增加条件
        :param head:
        :param k:
        :return:
        '''
        former, latter = head, head
        for _ in range(k):
            if not former:
                return
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[-k]
