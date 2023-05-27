#_*_coding:utf-8_*_
'''
题目：
    剑指offer 59  队列的最大值

    请定义一个队列并实现函数 max_value 得到队列的最大值，要求函数 max_value，push_back 和 pop_front
    的均摊时间复杂度都是O(1)

    若队列为空，pop_front 和 max_value 需要返回 -1

示例1：
    输入: 
        ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
        [[],[1],[2],[],[],[]]
    输出: 
        [null,null,null,2,1,2]

示例2：
    输入: 
        ["MaxQueue","pop_front","max_value"]
        [[],[],[]]
    输出: 
        [null,-1,-1]

限制：
    1 <= push_back,pop_front,max_value的总操作数 <= 10000
    1 <= value <= 10^5
'''

import queue
class MaxQueue:

    def __init__(self):
        '''
            这是官方的暴力解法
            直接实现一个普通的队列，查询最大值时遍历计算

            复杂度分析：
                时间复杂度O(1)（插入，删除），O(n) 求最大值
                    插入和删除只需要普通的队列操作，为O(1)
                    求最大值需要遍历当前的整个队列，最坏情况下为O(n)
                空间复杂度：O(n) 需要用队列存储所有插入的元素

        '''
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1


from collections import deque
class MaxQueue1:

    def __init__(self):
        '''
            这是我的暴力解法
            复杂度分析：
                时间复杂度：插入和删除O(1)， 求最大值 O(n)
                空间复杂度：O(n)，需要用队列存储所有插入的元素
        '''
        self.q = deque()


    def max_value(self) -> int:
        if len(self.q) == 0:
            return -1
        max_value = -1
        for i in range(len(self.q)):
            if self.q[i] > max_value:
                max_value = self.q[i]
        return max_value

    def push_back(self, value: int) -> None:
        self.q.append(value)


    def pop_front(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

'''
方法二：
    维护一个单调的双端队列
    思路：
        本算法基于问题的一个重要性质：当一个元素进入队列的时候，它前面所有比他小的元素就不会再对答案产生影响
    举个例子：如果我们向队列中插入数字序列 1， 1， 1， 1， 2 ，那么在第一个数字2被插入后，数字2前面的所有数字1
    将不会对结果产生影响，因为按照队列的取出顺序，数字2只能在所有的数字1被取出之后才能被取出，因此如果数字1如果在
    队列中，那么数字2必然也在队列中，使得数字1对结果没有影响。

    按照这样的思路，我们可以设计这样的方法：从队列尾部插入元素时，我们可以提前取出队列中所有比这个元素小的元素，使得
    队列中只保留对结果有影响的数字。这样的方法等价于要求维持队列单调递减，即要保证每个元素的前面都没有比它小的元素。

    那么如何高效实现一个始终递减的队列呢？我们只需要在插入每一个元素 value时，从队列尾部依次取出比当前元素 value小
    的元素，直到遇到一个比当前元素大的元素 value即可
        上面的过程保证了只要在元素 value被插入之前队列递减，那么在value被插入之后队列依然递减
        而队列的初始状态（空队列）符合单调递减的定义
        由数学归纳法可知队列将会始终保持单调递减
    上面的过程需要从队列尾部取出元素，因此需要使用双端队列来实现，另外，我们需要一个辅助队列来记录所有被插入的值
    以确定pop_front 函数的返回值。

    保证了队列单调递减后，求最大值时只需要直接取双端队列中的第一项即可

    复杂度分析：
        时间复杂度：O(1)  插入，删除，求最大值
        删除操作与求最大值显然只需要O(1)的时间
        而插入操作，虽然看起来有循环，做一个插入操作最多会有n次出队操作，但是要注意，由于每个数字只
        出队一次，因此对所有n个数字的插入过程，对应的所有出队操作也不会大于n次，因此将出队的时间均摊
        到每个插入操作，时间复杂度为O(1)
'''
from collections import deque
class MaxQueue:

    def __init__(self):
        self.main_q = deque()
        self.aux_q = deque()
        


    def max_value(self) -> int:
        if len(self.main_q) == 0:
            return -1
        return self.main_q[0]


    def push_back(self, value: int) -> None:
        while self.main_q and self.main_q[-1] < value:
            self.main_q.pop()
        self.main_q.append(value)
        self.aux_q.append(value)


    def pop_front(self) -> int:
        if len(self.main_q) == 0:
            return -1
        ans = self.aux_q.popleft()
        if ans == self.main_q[0]:
            self.main_q.popleft()
        return ans



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
