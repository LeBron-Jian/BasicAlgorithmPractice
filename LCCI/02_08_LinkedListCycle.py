#_*_coding:utf-8_*_
'''
    02.08  环路检测

    题目：给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。

    如果链表中有某个节点，可以通过连续跟踪  next 指针再次到达，则链表中存在环，我们可以使用
    整数 pos 来标色链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1， 则在该链表中
    没有环。
    注意： pos 不作为参数进行传递，仅仅是为了表示链表的实际情况。

示例1：
    输入：head = [3,2,0,-4], pos = 1
    输出：tail connects to node index 1
    解释：链表中有一个环，其尾部连接到第二个节点。

示例2：
    输入：head = [1,2], pos = 0
    输出：tail connects to node index 0
    解释：链表中有一个环，其尾部连接到第一个节点。

示例3：
    输入：head = [1], pos = -1
    输出：no cycle
    解释：链表中没有环。

进阶：
    你是否可以不用额外空间解决此题？    


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
            链表中是否存在环路：快慢指针法
            设置两个指针从起点同时出发，慢指针每移动一步快指针移动两步，如果存在环路则他们终究会相遇

            何时相遇呢？
                首先，快指针会离慢指针越来越远，后面，经过环路后，快指针会开始追赶慢指针，假设这时两者
                相距 k 步，那么每经过一个单位时间，快指针就离慢指针近了一步，因此该时刻两者经过k个单位
                时间后相遇。
            如何知道环路起点？
                设相遇点为 node，相遇点与环路起点的距离 k=head 与环路起点的距离 k。
                用一个指针指向 head，另一个指针指向 node，以同样的速度移动 k 步之后，两者会指向环路起点。
        '''
        fast, slow = head, head
        # 开始走位
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 相遇
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

        def detectCycle(self, head):
            if not head:
                return 

            cur = head
            while cur:
                # 如果该节点被访问过，则说明有环，该节点即为环的起点
                if cur.val is True:
                    return cur
                cur.val = True
                cur = cur.next
        return cur

        def detectCycle(self, head):
            if not head:
                return 
            cur = head
            tmp =[]
            while cur:
                if cur in tmp:
                    return cur
                tmp.append(cur)
                cur = cur.next
            return 
