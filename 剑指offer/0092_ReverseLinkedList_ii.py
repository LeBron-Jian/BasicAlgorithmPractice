#_*_coding:utf-8_*_
'''
92  反转链表2
        
        题目：反转从位置 m 到 n 的链表，请使用一趟扫描完成反转。

        说明：
            1<=m<=n<=链表长度

        示例：
            输入: 1->2->3->4->5->NULL, m = 2, n = 4
            输出: 1->4->3->2->5->NULL


思路：
        一般而言，面试是不允许我们修改节点的值，而只能修改节点的指向操作。
'''

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
            复杂度分析：
                时间复杂度：O(N) 其中N为链表总节点数
        '''
            # 设置 DummyNode 是这一类问题的一般做法
            dummy_node = ListNode(-1)
            dummy_node.next = head
            pre = dummy_node
            for _ in range(left-1):
                pre = pre.next

            cur = pre.next
            for _ in range(right-left):
                # next = cur.next
                # cur.next = next.next
                # next.next = pre.next
                # pre.next = next
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

            return dummy_node.next


