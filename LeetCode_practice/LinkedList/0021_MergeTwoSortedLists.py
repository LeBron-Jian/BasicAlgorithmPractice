# _*_coding:utf-8_*_
'''
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        我们可以递归的定义两个链表的合并操作
        当链表l1为空，则不用合并直接为l2，当链表l2为空时候，则直接返回l1
        当链表l1 l2均不为空，则递归的遍历l1,l2
        :param l1:
        :param l2:
        :return:
        '''
        if l1 is None:  # 终止条件，直到两个链表都空
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        最简单的思路
        :param l1:
        :param l2:
        :return:
        '''
        results = []
        while l1:
            results.append(l1.val)
            l1 = l1.next
        while l2:
            results.append(l2.val)
            l2 = l2.next
        # 但是这里增加了一个内置的 sort() 方法，所以我不是很喜欢这个解法
        # 其实可以对 l1.val 与 l2.val 进行比较，这样就不用使用sort() 方法了
        results.sort()
        head = ListNode(0)
        dummy = head
        for i in results:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建哑节点作为 结果链表 的开头,因此是不能移动的
        # 为了把两个链表 merge 的结果放到结果链表的最后，就需要一个move游标指向 结果链表 的最后一个元素
        # 初始时，move指向哑节点，之后随着结果链表的增加而不停地向后移动，始终保持其指向结果链表 的最后一个元素
        dummy = ListNode(0)
        # 有个游标，标识 结果链表的 结尾
        move = dummy
        # l1 和 l2 都未遍历结束
        while l1 and l2:
            # 如果l1 的 数值比较小
            if l1.val <= l2.val:
                # 把 l1 头部节点拼接到 结果链表的结尾
                move.next = l1
                l1 = l1.next  # l1 指向下一个节点
            else:
                # 把 l2头部节点拼接到  结果链表 的结尾
                move.next = l2
                l2 = l2.next  # l2指向下一个节点
            # 移动 结果链表的结尾指针
            move = move.next
        # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        move.next = l1 if l1 else l2
        # 返回哑节点的下一个位置
        return dummy.next
