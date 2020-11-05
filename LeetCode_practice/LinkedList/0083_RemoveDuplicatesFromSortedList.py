    #_*_coding:utf-8_*_
'''
题目：
    83  删除排序链表中的重复元素

    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次


示例 1:
    输入: 1->1->2
    输出: 1->2

示例 2:
    输入: 1->1->2->3->3
    输出: 1->2->3


注意：链表相关题的时候，总是返回head，原因

    head是头节点，位置没变，是固定的。而其他node做了引用，我们使用node做了链表的操作，所以最后均返回头结点。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
            参考官方，直接法
            这是一个简单的问题，测试我们操作列表节点指针的能力
            由于输入的列表已经排好序列，因此我们可以通过将节点的值与它之后的节点进行比较
            来确定他是否为重复结点。如果他是重复的，我们更改当前节点的 next指针，以便它跳过
            下一个节点并直接指向下一个节点之后的节点。

            复杂度分析：
                时间复杂度O(n) 因为列表中的每个节点都检查它是否重复，所以总运行时间为O(n)
                空间复杂度O(n) 没有额外使用空间
        '''
        pass



    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        '''
            快慢指针
            思路：
                1，首先设定快慢指针
                2，快指针一直往前走
                3，当慢指针 ！= 快指针的时候，此时就要将 slow.next = fast，这样就可以去掉重复的元素
                    去掉之后，将 slow = fast，同步慢指针的位置
                4，做完这些就基本差不多了，但是还不能返回，需要断掉慢指针后的所有重复元素

            注意：
                1，注意空链表的情况
                2，在比较节点的val或滑动窗口时注意节点不能为None，这种情况下需要添加 is not None的条件判断
        '''
        # 特殊情况：如果是空链表的话
        if not head:
            return
        former = head   # 创建一个需要操作的变量，即快指针
        latter = former  # 维护一个慢指针
        former = former.next

        while former:
            # 比较 快指针和慢指针的值是否相等，直到删除到不相等为止
            while former and  former.val == latter.val:
                former = former.next
                latter.next = former
            # 指针顺序滑动
            if former:
                latter = latter.next
                former = former.next
        # 注意返回头节点，不能返回faster latter
        return head 


    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        '''
            双指针方法2
                即需要两个指针，fomer指针不断往前走，如果former和latter指针的元素相等
                则什么也不用做；
                如果former和latter指针的元素不等，则latter指针也往前走一步，并将former 
                指针的值赋给a指针
        '''
        if not (head and head.next):
            return head
        former, latter = head, head
        while former:
            # 如果latter的值不等于former的值，则latter前进一位，然后将 former的值赋给latter
            if latter.val != former.val:
                latter = latter.next
                latter.val = former.val
            # 不管former是否等于latter，former都前进一位
            former = former.next
        latter.next = None
        return head
