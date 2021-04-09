#_*_coding:utf-8_*_
'''
    02.07  链表相交

    题目：给定两个（单向）链表，判定他们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是
        基于节点的值。换句话说，如果一个链表的第 k 个节点与另一个链表的 j 个节点是同一个节点（引用
        完全相同），则这两个链表相交。



示例 1：
    输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
    在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


示例 2：
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Reference of the node with value = 2
    输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
    在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
    输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    输出：null
    输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，
    所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
    解释：这两个链表不相交，因此返回 null。

注意：
    如果两个链表没有交点，返回 null 。
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            根据题意，两个链表相交的点是指：该节点即在A链表上又在B链表上，说明A和B是相交的。
            而对相交的情况，两条链表一定是这种结构。

            如果链表A和链表B相较于D的话，那么说明D节点即在A上又在B上，而D之后的元素自然也就
            均在A和B上了，因为他们是通过 next 指针相连的。

            如果有相交的节点D的话，每条链的头节点先走完自己的链表长度，然后回头走另外一条链表
            那么两节点一定为相较于 D 点，因为这时每个头节点走过的距离都是一样的，都是AD+BD+DC
            而他们每次都是前进1，所以距离相同，速度又相同，固然一定会在相同的时间走到相同的节点上
            即D点。 

            双指针法：
                如果两个链表相交，他们在末尾的节点也必然相同，若最后元素不相同，则两个链表不相交。

            复杂度分析：
                时间复杂度：O(m+n)
                空间复杂度：O(1)

        '''
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        # return a
        return b

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            哈希表：遍历链表A，并将每个节点的地址/引用存储在哈希表中，然后检查链表B中的
                    每个节点 bi 是否在哈希表中，若在，则Bi为相交节点。
            因为给列表中保存的是链表，如果链表太长的话，会超时，所以这种方法并不好
            复杂度分析：
                    时间复杂度：O(m+n)
                    空间复杂度：O(m)O(n)
        '''
        res = []
        movea, moveb = headA, headB
        while movea:
            res.append(movea)
            movea = movea.next
        print(res)
        while moveb:
            if moveb in res:
                return moveb
            moveb = moveb.next
        return None


    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        counta, countb = 0, 0
        #print(counta, countb)
        while a:
            # counta += 1
            a = a.next
            counta += 1
        while b:
            # countb += 1
            b = b.next
            countb += 1
        
        #print(countb, countb)
        aa, bb = headA, headB
        if countb > counta:
            res = countb - counta
            for _ in range(res):
                bb = bb.next
        else:
            res = counta - countb
            for _ in range(res):
                aa = aa.next
        while aa and bb:
            if aa == bb:
                return aa
            else:
                aa = aa.next
                bb = bb.next
        return None
