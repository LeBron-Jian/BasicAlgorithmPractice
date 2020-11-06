#_*_coding:utf-8_*_
'''
    剑指offer 52   两个链表的第一个公共节点

    输入两个链表，找到他们的第一个公共节点

示例1：
    输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
    在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


示例2：
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Reference of the node with value = 2
    输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
    在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

注意：

    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
    本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            双指针法:
                我们使用两个指针 node1，node2分别指向两个链表 headA， headB的头结点
                然后同时分别逐个结点遍历，当node1到达链表 headA的末尾时，重新定位到链表
                headB的头节点；当 node2 到达链表 headB的末尾时，重新定位到链表 headA 的
                头结点。这样当他们相遇时，所指向的节点就是第一个公共结点。

            时间复杂度为O(n+m)
            空间复杂度为O(1)
        '''
        node1, node2 = headA, headB
        if not node1 or not node2:
            return 
        while node1 != node2:
            node1 = node1.next if node1 else headB 
            node2 = node2.next if node2 else headA
        return node1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            对上面的解法进行简单易懂的解释
        '''
        node1, node2 = headA, headB
        if not node1 or not node2:
            return 
        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = headB
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        return node1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            双指针的另一种写法
        '''
        # 双指针分别指向两个链表
        node1, node2 = headA, headB
        while node1 or node2:
            # 如果指针走到了头，则分别指向另一个链表的表头
            if not node1:
                node1 = headB
            if node node2:
                node2 = headA
            # 如果两个指针相遇了，则找到相交点
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            暴力解法

            我们知道两个链表如果有重复的节点，则从第一个重复结点之后就都相同了。
            暴力解法很简单，就是在第一个链表headA 上遍历每一个节点，每遍历到一个节点时，
            就对headB 整个遍历一次，知道出现相同的节点 

            时间复杂度为 O(m*n)
            空间复杂度为 O(1)
        '''
        pass


    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            双栈法

                这个方法的思路是，我们需要两个栈来保存两个链表，由于栈的特性，保存完之后
                栈顶元素是链表的最后一个元素
                我们知道如果存在重复的节点，那么这两个栈中的上面几个元素是相同的
                同时从两个栈顶弹出元素，直到弹出的两个元素不相等时，那么前一个元素就是我们
                要找的重复结点

            这个就是空间换时间

            时间复杂度为 O(m+n)
            空间复杂度为 O(m+n)
        '''
        # stackA, stackB = [], []
        # while headA:
        #     stackA.append(headA)
        #     headA = headA.next
        # while headB:
        #     stackB.append(headB)
        #     headB = headB.next
        # res = []
        # while stackA.pop() == stackB.pop():
        #     # print(stackA.pop())
        #     res.append(stackA.pop())
        #     print(res)
        # if res:
        #     return res.pop()
        # else:
        #     return 
        pass

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            我们知道，两个链表的第一个公共节点到尾巴节点的长度一定相同，因此我们需要先对齐
            两个链表，再一起往后走找到第一个公共节点即可

            1，找到两个链表长度 n1， n2，长的链表先走 n1-n2步
            2，一起往后走，找到第一个公共节点

        '''
        node1, count1 = headA, 0
        node2, count2 = headB, 0
        while node1:
            node1 = node1.next
            count1 += 1
        while node2:
            node2 = node2.next
            count2 += 1

        node1, node2 = headA, headB
        if count2 > count1:
            res = count2 - count1
            for _ in range(res):
                node2 = node2.next
        else:
            res = count1 - count2
            for _ in range(res):
                node1 = node1.next
        while node1 and node2:
            if node1 == node2:
                return node1
            else:
                node1 = node1.next
                node2 = node2.next
        return None
