#_*_coding:utf-8_*_
'''
232
题目：  用栈实现队列

    请你仅使用两个栈实现先入先出队列。队列应当支持队列的支持的所有操作（push，pop，peek，empty） 
    实现MyQueue类：
        void push(int x) 将元素 x 推到队列的末尾
        int pop() 从队列的开头移除并返回元素
        int peek() 返回队列开头的元素
        boolean empty() 如果队列为空，返回 true ；否则，返回 false

    说明：
        你只能使用标准的栈操作——也就是只有 push to top，peek/pop from top，size和 is empty 操作是合法的
        你使用的语言也许不支持栈，但是可以使用list或 deque来模拟一个栈，只要是标准的栈操作即可
    
    进阶：
        你能否实现每个操作均摊时间复杂度为O(1)的队列，换句话说，执行n个操作总时间复杂度为O(n)，即使其中
        一个操作可能花费较长时间

    示例：
        输入：
        ["MyQueue", "push", "push", "peek", "pop", "empty"]
        [[], [1], [2], [], [], []]
        输出：
        [null, null, null, 1, 1, false]

        解释：
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); // queue is: [1]
        myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
        myQueue.peek(); // return 1
        myQueue.pop(); // return 1, queue is [2]
        myQueue.empty(); // return false

    提示：
        1 <= x <= 9
        最多调用100次 push pop peek 和 empty
        假设所有操作都是有效的（例如：一个空的队列不会调用 pop 或者 peek 操作）
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        因为Python没有给出栈的数据结构，所以我们用list来模拟栈操作
        append 代表栈顶加入元素
        pop 代表弹出栈顶元素
        此外还可以使用len函数计算栈的元素个数
        一般栈的性质：进展 li.append  出栈 li.pop  取栈顶 li[-1]
        """
        self.A = []  # 主栈，进入的第一个栈
        self.B = []  # 辅栈，进入的第二个栈


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        push直接往主栈末尾添加元素，利用append即可实现
        """
        self.A.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        pop的时候，我们先将主栈元素像辅栈转移，直到主栈只剩下一个元素的时候，这就是我们
        要返回的元素，然后我们再把辅栈中的元素转移回主栈即可
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                # a.pop() 表明删除列表的最后一个元素
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return self.B.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return 
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.B) == 0 and len(self.A) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
