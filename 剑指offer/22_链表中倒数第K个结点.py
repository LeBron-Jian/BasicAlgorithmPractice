    #_*_coding:utf-8_*_
'''
题目：
    剑指offer 22  链表中倒数第K个结点

    输入一个链表，输出该链表中倒数第k个结点，
    为了符合大多数人的习惯，本题从1开始计数，即链表的尾巴节点是倒数第一个结点，
    例如一个链表由六个节点，从头开始它的值一次是1,2,3,4,5,6，这个链表的倒数第
    三个节点是值为4的节点

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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        '''
            第一时间想到的解法：
                1，通过遍历统计链表长度，记为 n
                2，设置一个指针走（n-k)步，即可找到链表倒数第k个结点
                    （因为题目说了，计算从 1 开始，所以指针为（n-k）

        '''
        count = 0
        tempNode = head
        while tempNode:
            tempNode = tempNode.next
            count += 1
        res = head
        for i in range(count-k):
            head = head.next
        return res.next


    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        '''
            使用双指针则可以不用统计链表长度，只遍历一次链表

            算法流程：
                1，初始化：前指针 fromer，后指针 latter，双指针都指向头节点 head
                2，构建双指针距离：前指针 former 先向前走 k 步（结束后，双指针 former和
                    latter间相距 k 步）
                3，双指针共同移动：循环中，双指针 former和latter每轮都向前走一步，直至former
                    走过链表尾结点时跳出（跳出后，latter与尾结点距离为 k-1，即latter指向倒数
                    第k个结点）
                4，返回值：返回 latter即可。

            复杂度分析：
                时间复杂度为 O(n)：n为链表长度，总体看former走了n步，latter走了（n-k）步
                空间复杂度为 O(1)：双指针 former latter 使用常数大小的额外空间

                控体重没有k大于链表长度的case，因此不用考虑越界问题，也可以考虑后面补充代码

        '''
        former = latter = head
        for i in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

        
    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        '''
            考虑越界问题
        '''
        former = latter = head
        for _ in range(k):
            if not former:
                return 
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter


    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        '''
            python也可以这样写，但是不建议
            1，时间复杂度为O(n) 空间复杂度为O(n)
            2，当链表足够大的时候，新list占用的空间太大，导致后面慢
        '''
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[-k]
