    #_*_coding:utf-8_*_
'''
题目：
    剑指offer 18  删除链表的节点

    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点
    返回删除后的链表的头节点



示例 1:
    输入: head = [4,5,1,9], val = 5
    输出: [4,1,9]
    解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
    输入: head = [4,5,1,9], val = 1
    输出: [4,5,9]
    解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明：
    题目保证链表中节点的值互不相同
    若使用C或者C++语言，你不需要free或delete被删除的节点


#  题目中表示链表中的节点值互不相同，也就是说最多只能删除一个。



删除单向链表节点的两种思路：
    1，搬离数据域后改变指向
    利用一个指针delete 定位到要删除的节点，接着搬移数据，最后改变指向
        1，确定一个指针 delete
        2，进行数据搬移  delete.val = delete.next.val
        3，最后改变指向 delete.next = delete.next.next

    这个方法有一个致命的缺陷：要是删除的刚好是表尾，则将面临无数据可搬移的局面，
    即 delete.next.val 会出错，因为访问了 null 的 val

    其他缺点：当数据域很庞大的时候，搬移数据将花费大量的时间

    2，直接改变指向
    利用一个空的头节点 phead和两个指针 prev和 delete
    delete 指向要删除的节点  prev指向要删除节点的前驱
    这样只要改变prev的指向就可以实现逻辑上的删除
        只需要改变前驱的指向  prev.next = delete.next

    优点：
        1，可以删除任意位置的节点，表头和表尾都不需要特殊处理
        2，只改变了一下指向，时间代码很小
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        '''
            哨兵节点

            复杂度分析：
                时间复杂度 O(n)
                空间复杂度 O(1)
        '''
        dummy = ListNode(0)
        dummy.next = head
        if head.val == val:
            return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next 
            else:
                head = head.next
        return dummy.next


    def deleteNode1(self, head: ListNode, val: int) -> ListNode:
        '''
            双指针：
                1，定位节点：遍历链表，直到 head.val == val 时跳出，即可定位目标节点
                2，修改引用：设节点 cur 的前驱节点为 pre，后继节点为 cur.next，则执行
                    pre.next = cur.next，即可实现删除 cur 节点

            算法流程：
                1，特例处理：当应删除头节点 head的时候，直接返回 head.next 即可
                2，初始化： pre = head，cur = head.next
                3，定位节点：当 cur 为空 或 cur 节点值等于 val 时跳出
                    1，保存当前节点索引，即 pre = cur
                    2，遍历下一节点，即 cur = cur.next
                4，删除节点：若 cur 指向某节点，则执行 pre.next = cur.next
                    （若cur指向null，则代表链表中不包含值为val的节点
                5，返回值：返回链表头部节点 head即可

            复杂度分析：
                时间复杂度O(n) ： n为链表长度，删除操作平均需循环 N/2次，最差n次
                空间复杂度O(1)： cur,pre 占常数大小额外空间
        '''
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        if cur.val == val:   # if cur:
            pre.next = cur.next
        return head
        
        def deleteNode1(self, head: ListNode, val: int) -> ListNode:
            '''
                更新上面的代码
            '''
            pre = cur = head
            if cur.val == val:
                return head.next
            while cur and cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            return pre

        def deleteNode2(self, head: ListNode, val: int) -> ListNode:
            '''
                递归：链表具有天然的递归性

                    递归的终止条件：
                        1，该节点为空，直接返回
                        2，该节点就是要删除的节点，返回该节点的下一个节点
            '''
            if not head:
                return head
            if head.val == val:
                return head.next
            head.next = self.deleteNode2(head.next, val)
            return head
