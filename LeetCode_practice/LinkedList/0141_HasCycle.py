# _*_coding:utf-8_*_
'''
141  环形链表
题目：
    给定一个链表，判断链表中是否有环。

    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
    （索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

进阶：
    你能用 O(1)（即，常量）内存解决此问题吗？
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 链表是由一系列节点组成的元素集合，每个节点包含两部分，数据域和指向下一个节点的指针next
    # 通过节点之间的相互连接，最终串联成一个链表
    def hasCycle(self, head: ListNode) -> bool:
        # 置空法  时间消耗很长，但是没有消耗内存
        if not head:
            return False
        while head.next and head.val != None:
            head.val = None  # 遍历的过程中将值置空
            head = head.next
        if not head.next:  # 如果碰到空发现一家结束，则无环
            return False
        return True  # 否则有环

    def hasCycle1(self, head: ListNode) -> bool:
        '''
        快慢指针，快指针走两步，慢指针走一步
        如果有环，则两者能相遇，如果无环，那么快指针先到达终点
        :param head:
        :return:
        '''
        # 节点不存在或下一个节点不存在
        if not head or not head.next:
            return False
        # 起点错开，防止下面循环判断出问题
        slow, fast = head, head.next
        # 快指针和快指针的下一个节点不为空
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def hasCycle11(self, head: ListNode) -> bool:
        # 如果上面快慢指针不容易理解，请看这个代码，总有一款适合自己理解
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle111(self, head: ListNode) -> bool:
        slow, fast, = head, head
        # 没有必要这样写，加入while循环判断更加简洁
        # if not head:
        #     return False

        # 防止head为空和出现空指针的next的情况
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # if slow == fast:
                return True
        return False

'''
快慢指针的理解：
    定义一个快指针和一个慢指针，每次快指针走两步，慢指针走一步，判断快指针是否
    与慢指针重逢，时间复杂度为O(n+k)
    
    情况1：链表部分成环O(n)
        部分成环时，快指针先于慢指针进入环，慢指针进环时间O(n)；当快慢指针都进入
        环，假设环节点数量为K，当快慢指针第一次相遇时，快指针至少已经在环内已经比
        慢指针多走一圈（多走的这一圈是当慢指针进入后开始计算的），时间复杂度为O(k)
        综上，时间复杂度为O(k+n)，即O(n)
    
    情况2：链表完全成环O(n)
        同起点，第一次相遇时，快指针已经在环内比慢指针多走一圈，时间复杂度为O(n)
'''
