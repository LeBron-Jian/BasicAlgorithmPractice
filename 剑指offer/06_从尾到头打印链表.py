#_*_coding:utf-8_*_
'''
题目：
    剑指offer 6  从尾到头打印链表

    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）



示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]
 

限制：
    0 <= 链表 的长度 <= 10000

'''
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        '''
            第一反应是栈  将链表的元素入栈，再出栈即可
            栈的特点是后进先出，即最后压入栈的元素是最先弹出。考虑到栈的这个特性，使用栈将链表元素
            顺序倒置，从链表的头节点开始，依次将每个节点压入栈内，然后依次弹出栈内的元素并存储到数组中

            算法步骤：
                1，创建一个栈，用于存储链表的节点
                2，创建一个指针，初始时指向链表的头节点
                3，当指针指向的元素非空时，重复以下操作
                    将指针指向的节点压入栈内
                    将指针移到当前节点的下一个节点
                4，获得栈的大小 size，创建一个数组 res，其大小为size
                5，创建下标并初始化 index=0
                6，重复 size次下面操作
                    从栈内弹出一个节点，将该节点的值存储到 res[index]
                    将index的值+1
                7，返回res

            复杂度分析：
                时间复杂度：O(n)
                空间复杂度：O(n)

        '''
        stack_res, res = [], []
        node = head
        while node:
            stack_res.append(node.val)
            node = node.next
        while len(stack_res) != 0:
            res.append(stack_res.pop())
        return res

        def reversePrint(self, head: ListNode) -> List[int]:
            '''
                上述写法的简洁写法
            '''
            stack_res = []
            while head:
                stack_res.append(head.val)
                head = head.next
            return stack_res[::-1]


        def reversePrint1(self, head: ListNode) -> List[int]:
            '''
                递归法
                    利用递归：先走至链表末端，回溯时依次将节点值加入列表，这样就可以实现链表值的倒序输出
                    假设 head.next 已经排好序，那么只需将 head添加到末尾即可，

                算法流程：
                    1，递推阶段：每次传入 head.next，以 head=None （即走过链表尾部节点）为递归终止条件
                            此时返回空列表 []
                    2，回溯阶段：利用Python语言特性，递归回溯时每次返回 当前list + 当前节点值 [head.val]
                            即可实现节点的倒序输出

                算法复杂度
                    时间复杂度O(N)  遍历链表，需要递归n次
                    空间复杂度O(n) 系统递归需要使用O(n)的栈空间

            '''
            return self.reversePrint(head.next) + [head.val] if head else []



res = [1,2,3]
res.reverse()
print(res)
