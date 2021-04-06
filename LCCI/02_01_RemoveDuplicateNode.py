#_*_coding:utf-8_*_
'''
    02.01  移除重复节点

    题目： 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
     输入：[1, 2, 3, 3, 2, 1]
     输出：[1, 2, 3]


示例2:
    输入：[1, 1, 1, 1, 2]
    输出：[1, 2]


提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。

进阶：
    如果不得使用临时缓冲区，该怎么解决？


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        '''
            这样做，会改变链表的次序，并且使用了临时缓冲区
            虽然结果是相同的，但是顺序改变了，不满足题意
        '''

        if not head or not head.next:
            return head
        move = head
        # record 负责储存看见过的值。现在已经储存了第一个值。
        record = {head.val}
        # 只要 move 接下来还有东西，就看看下一个东西是不是已经在 record中
        while move and move.next:
            # 这里判断时要同时符合两个条件，因为如果r已经是None，判断 move.next 会报错，
            # 所以每次得先判断 move

            # 如果下一环的值没有被存储过，不用对 head 做任何修改。
            if move.next.val not in record:
                record.add(move.next.val)
                move = move.next
            else:
                move.next = move.next.next


        return head

