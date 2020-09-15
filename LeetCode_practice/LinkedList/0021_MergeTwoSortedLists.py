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
            不过我们要判断 l1 和 l2 哪一个链表的头节点的值更小，然后递归的决定
            下一个添加到结果里的节点。如果两个链表有一个为空，递归结束。
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
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' 
            对上面方法的改进，将判断放入else里面，我发现无论是时间，还是空间
            都应该更快，从提交结果来看。
            但是两种方法的时间复杂度都为O(n)，空间复杂度为O(n)
            
            对复杂度的分析：
            时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。每次调用都会取掉l1或者l2的头结点
                        （直到至少有一个链表为空），函数mergeTwoList至多只会递归调用每个节点依次，
                        因此，时间复杂度取决于合并后的链表长度，即O(n+m)
            空间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。递归调用 mergeTwoLists 函数时需要
                        消耗空间，栈空间的大小取决于递归调用的深度。结束递归调用时mergeTwoLists函数最多
                        调用 n+m 次，因此空间复杂度为O(n+m)
        '''
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        最简单的思路：
        这里新增了一个list，并且使用了sort()内置方法。。。。
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
        '''
            我们也可以使用迭代的方法来实现上述算法，当l1和l2都不是空链表时，判断 l1 和 l2 哪一个
            链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应
            链表中的节点向后移一位。
            
            复杂度分析：
                时间复杂度：O(n+m)，其中n和m分别为两个链表的长度，因为每次循环迭代中，l1和l2只有一个
                        元素会被放进合并链表中，因此while循环的次数不会超过两个链表的长度之和，所有其
                        它的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)
                空间复杂度：O(1)，我们只需要常数的空间存放若干变量
        '''
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
