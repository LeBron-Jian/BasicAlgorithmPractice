#_*_coding:utf-8_*_
'''
    02.06  回文链表

    题目：编写一个函数，检查输入的链表是否是回文的。


示例 1：
    输入： 1->2
    输出： false 

示例 2：
    输入： 1->2->2->1
    输出： true 
 

进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
            复杂度分析：
                时间复杂度：遍历链表并将值复制到数组中 O(n)
                空间复杂度：O(n)，其中n指的是链表元素个数，我们使用一个数组列表存放链表的元素值
        '''
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]

    def isPalindrome1(self, head: ListNode) -> bool:
        '''
            最简单的方法就是将值复制到数组中，然后使用双指针法
            确定数组列表是否回文很简单，我们可以用双指针来比较两端的元素，并向中间移动。
            一个指针从起点向中间移动，另一个指针从终点向中间移动，这需要 O(n)的时间，因为
            访问每个元素的时间是 O(1), 而有 n 个元素要访问。
            然而同样的方法在链表上操作并不简单，因为不论是正向访问还是反向访问都不是O(1)
            所以最简单的方法就是将链表的值复制到数组列表中，再使用双指针法判断。
        
        '''
        tmp = []
        move = head
        while move:
            tmp.append(move.val)
            move = move.next
        return tmp == tmp[::-1]


