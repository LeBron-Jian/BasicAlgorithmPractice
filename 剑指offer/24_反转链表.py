    #_*_coding:utf-8_*_
'''
题目：
    剑指offer 24  反转链表

    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点

示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL

限制：
    0 <= 链表长度 <= 5000  

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
            最简单的方法就是申请一个动态扩容
            然后不断遍历链表，将链表中的元素添加到这个容器中
            再利用容器自身的API，翻转整个容器，这就可以达到翻转的效果
            最后同时遍历容器和链表，将链表中的值改为容器中的值

            这种方法很简单，但是面试中，肯定需要更优的方法，比如不用外部空间

            输入为：[1, 2, 3, 4, 5]
            输出为：[5, 4, 3, 2, 1]
        '''
        resNode = ListNode(0)
        move = resNode
        reslist = []
        while head:
            reslist.append(head.val)
            head = head.next
        # print(reslist)  # [1, 2, 3, 4, 5]
        reslist.reverse()
        # print(reslist)  # [5, 4, 3, 2, 1]

        for i in reslist:
            move.next = ListNode(i)
            move = move.next

        # for i in range(len(reslist)):
        #     move.next = ListNode(reslist[i])
        #     move = move.next
        return resNode.next

    def reverseList(self, head: ListNode) -> ListNode:
        '''
            栈   通过栈可以创建一个新链表
        '''
        if not head:
            return head
        stack = []
        # 把head中的值加入栈里
        while head:
            stack.append(head.val)
            head = head.next
        # 去最后加入的一个，即链表尾作为新的链表头
        cur = ListNode(stack.pop())
        # 记住头部索引
        move = cur
        # 依次给新链表赋值
        while stack:
            move.next = ListNode(stack.pop())
            move = move.next
        return cur


    def reverseList1(self, head: ListNode) -> ListNode:
        '''
            双指针迭代
                我们可以申请两个指针，第一个指针叫pre，最初是指向 null 的
                第二个指针 cur 指向 head，然后不断遍历cur。
                每次迭代到cur，都将 cur的 next指向pre，然后pre和cur前进一位
                都迭代完了（cur变成null了）， pre就是最后一个节点了。
        '''
        # 申请两个节点，pre和cur，其中pre指向None
        pre, cur = None, head
        # 遍历链表，while循环里面的内容其实可以写成一行
        while cur:
            # 记录当前节点的下一个节点
            temp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            pre =cur
            cur = temp
        return pre


    def reverseList2(self, head: ListNode) -> ListNode:
        '''
            递归
                递归的终止条件就是当前为空，或者下一个节点为空

                递归的两个条件：
                    1，终止条件为当前节点或下一个节点为空
                    2，在函数内部，改变节点的指向，也就是head的下一个节点
                        指向head递归

                递归函数中每次返回的cur其实只最后一个节点，在递归函数内部，
                改变的是当前节点的指向。
                很不好理解的就是 head的下一个节点指向 head，即 head.next.next = head

        '''
        if not (head and head.next):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        head.next.next = head
        # 为了防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归都返回cur,也就是最后一个节点
        return cur
