#_*_coding:utf-8_*_
'''
225
题目：  用队列实现栈

    使用队列实现栈的下列操作：
        push(x) -- 元素 x 入栈
        pop() -- 移除栈顶元素
        top() -- 获取栈顶元素
        empty() -- 返回栈是否为空

注意：
    你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
    你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
    你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

示例：
    输入：
        ["MyStack","push","push","top","pop","empty"]
        [[],[1],[2],[],[],[]]
    输出：
        [null,null,null,2,2,false]

思路：
    栈是一种后进先出的数据结构，元素从顶端入栈，然后从顶端出栈
    队列是一种先进先出的数据结构，元素从后端入队，然后从前端出队
    
'''
from collections import deque

class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        这里使用了列表实现（只不过一般列表结果即可实现栈）
        """
        self.A = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.A.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        return self.A.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return 
        return self.A[-1]



    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.A) == 0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        一个队列
        使用一个队列的时候，为了满足栈的特性，即最后入栈的元素是最先出栈，同样需要满足队列
        前端的元素是最后入栈的元素。
        """
        self.queue = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        入栈操作时，首先获得入栈前的元素个数 n，然后将元素入队到队列，再将队列中的前n个元素
        （即除了新入栈的元素之外的全部元素）依次出队并入队到队列，此时队列的前端元素即为入栈
        的元素，且队列的前端和后端分别对应栈顶和栈底

        """
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return 
        return self.queue[0]



    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.A) == 0:
            return True
        else:
            return False

'''
复杂度分析：
时间复杂度：
    入栈操作O(n)，其余操作都是O(1)
    入栈操作需要将队列中的 n个元素出队，并入队 n+1 个元素到队列，共有 2n+1 次操作
    每次出队和入队操作的时间福再度都是O(1)，因此入栈操作的时间复杂度为O(n)

    出栈操作对应将队列的前端元素出队，时间复杂度为 O(1)

    获得栈顶元素操作对应获得队列的前端元素，时间复杂度为O(1)

    判断栈是否为空操作只需要判断队列是否为空， 时间复杂度为O(1)
空间复杂度：
    都为O(n)，因为n是栈内元素，需要使用一个队列存储栈内的元素
'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


from collections import deque


class MyStack3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        while len(self.q2) != 0:
            self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1
        


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        return self.q2.popleft()
                

        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return 
        return self.q2[0]



    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False

'''
复杂度分析：
    时间复杂度：入栈操作O(n)，其余操作都是O(1)
        入栈操作需要将队列q1中 n个元素出队，并入队 n+1个元素到q2中，共有 2n+1 次操作
        每次出队和入队的时间复杂度都是O(1)，因此入栈操作的时间复杂度为O(n)

        出栈操作对应将 q1 的前端元素出队，时间复杂度为O(1)

        获得栈顶元素操作对应获得 q1 的前端元素，时间复杂度为O(1)

        判断栈是否为空操作只需要判断 q1 是否为空，时间复杂度为 O(1)
    空间复杂度： O(n)
        其中 n 是栈内的元素，需要使用两个队列存储栈内的元素
'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
