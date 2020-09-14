# _*_coding:utf-8_*_
'''
2：两数相加
题目：
    给出两个非空的链表用来表示两个非负的整数，其中，他们各自的位数是按照逆序的方式存储的
    并且他们的每个节点只能存储一位数字。
    如果我们将这两个数字加起来，则返回一个新的链表来表示他们的和
    你可以假设除了0之外，这两个数字都不会以0开头
示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
'''


# 当我们存储一大波数据时，我们很多时候使用数组，但是当我们执行插入操作的时候就是非常麻烦
# 比如有一堆数据1,2,3,4,5,6，我们要在3和5之间插入4，如果使用数组，我们需要将5之后的数据退一位，再插入4
# 上面非常麻烦，但是如果使用链表，就直接在3和5之间插入4即可。
# Definition for singly-linked list.
class ListNode:
    '''
    链表是由一系列节点组成的元素集合，每一个节点包含两部分，
    数据域val和指向下一个节点的指针next,通过节点之间的相互连接
    最终串联成一个链表，所以链表的节点结构如下：data next
    其中data为自定义的数据，next为下一个节点的地址，head保存首位节点的地址
    '''

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        正向思维，根据题意直推法，先将两个链表转换成列表形式
        为了计算两个链表之和，将列表转成字符串形式，再将字符串转成 int型
        此时计算出和，因为最后返回的是链表形式，所以计算出和之后，将和值转为字符串
        然后再从后往前遍历字符串，并插入空链表，最后可返回结果链表
        地址：https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-xing-yun-de-bei-ji-lang/
        # 注意此思路没问题，结果有问题。。。。
        :param l1:
        :param l2:
        :return:
        '''
        # 链表转成列表
        a1, a2 = [], []
        while(l1):
            a1.append(l1.val)
            l1 = l1.next
        while(l2):
            a2.append(l2.val)
            l2 = l2.next

        # 列表转换为字符串
        s1 = ''
        for i in range(len(a1)-1, -1, -1):
            s1 = s1 + str(a1[i])
        s2 = ''
        for j in range(len(a2)-1, -1, -1):
            s2 = s2 + str(a2[j])

        # 字符串转为整数
        m1, m2 = int(s1), int(s2)
        # 整数之和转成字符串
        m3 = str(m1 + m2)

        # 新建两个空链表
        tmp_node = ListNode(None)
        node = ListNode(None)
        # 从后面往前面遍历和字符串，插入链表
        for x in m3[::-1]:
            if not tmp_node.val:
                tmp_node.val = int(x)
                node = tmp_node
            else:
                tmp_node.next = ListNode(int(x))
                tmp_node = tmp_node.next
        return node



    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        这是一个关于链表的问题，逆序存储，即我们的遍历顺序是将个位，十位，百位
        所以我们只需要从个位开始，诸位相加就好，同时注意进位问题，设置一个carry变量
        最后注意一个问题，就是可能存在最终得到的数比l1 l2的长度都大的情况
        所以最后需要检查一下 carry的值，如果carry>0，则再构建一个值为1的节点
        :param l1:
        :param l2:
        :return:
        '''
        # 表示构造一个值为0的头节点
        pNode = ListNode(0)
        # 我们自己构建一个值为0的头结点，将其存储为头结点
        # 注意这里，需要提醒的是 肯定有人问设置一个不行吗？非要定义head和node两个
        # 其实设置PHead就是为了方便return。
        # 因为链表的设计是由我们来决定的，有的链表存在表头节点，就是链表的第一个节点
        # 用来存放链表的长度之类的数据或者空着不用，而不用于其他用途，有些链表直接从
        # 第一个结点就开始存放我们想要的数据。
        # 而题中，我们head是指向第一个节点，即头节点，但是头节点没有存放数据，
        # 所以从第二个节点开始才是我们要存的数据，这时候应该用 head.next 所指向的节点存放数据
        pHead = pNode
        carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next
            sum = sum + carry
            carry = sum // 10
            pNode.next = ListNode(sum % 10)
            pNode = pNode.next
        if carry > 0:
            pNode.next = ListNode(carry)
        return pHead.next
    
    def addTwoNumbers22(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
            自己默写一遍，同时写成自己熟悉的代码
        '''
        pnode = ListNode(0)
        phead = pnode
        carry = 0
        while l1 or l2:
            sums = 0
            if l1:
                sums = sums + l1.val
                l1 = l1.next
            if l2:
                sums = sums + l2.val
                l2 = l2.next
            pnode.next = ListNode((sums+carry)%10)
            carry = (sums+carry) // 10
            pnode = pnode.next
        if carry != 0:
            pnode.next = ListNode(carry)
        return phead.next


data1 = ListNode([1, 2, 3])
data2 = ListNode([1, 2, 3])
a1 = []
while (data1):
    a1.append(data1.val)
    data1 = data1.next
print(a1)


a1 = [[1, 2, 3, 4, 5]]

s1 = ''
for i in range(len(a1[0])-1, -1, -1):
    # print(a1[0][i])  # 51  41 31 21 11
    s1 = s1 + str(a1[0][i])

# print(s1)  # 5141312111
m3 = str(int(s1) + int(s1))
# print(m3)  # 10282624222

tmp_node = ListNode(None)
node = ListNode(None)
# 从后面往前面遍历和字符串，插入链表
for x in m3[::-1]:
    print(x)
    if not tmp_node.val:
        tmp_node.val = x
        node = tmp_node
    else:
        tmp_node.next = ListNode(x)
        tmp_node = tmp_node.next
print(node.val)


'''
# 继续补充解法:
    链表由节点构成，每个节点分为数据域和指针域，数据域存放元素，指针域存放下一个节点的地址
    Python没有指针，所有变量都是对象，因此只能模拟一个链表。
    模拟的 val 就是节点数据， next 就是下一个节点
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
        # 思路就是就是补头，然后分情况讨论输出
        # 为了节省内存，结果存储在链表l1中
        
        if l1 == None and l2 == None and carry==0:
            return None
        if l1 == None and  l2 == None  and carry == 1:
            return ListNode(1)
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        
        l1.val , carry = (l1.val + l2.val + carry)%10, (l1.val + l2.val + carry)//10
        l1.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return l1
