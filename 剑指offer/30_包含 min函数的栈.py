#_*_coding:utf-8_*_
'''
题目：
    剑指offer 30 包含 min函数的栈

    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
    调用 min, push以pop的时间复杂度都是O(1)

示例:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.min();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.min();   --> 返回 -2.
     

提示：
    各函数的调用总次数不超过 20000 次


'''
class MinStack:
    '''
        普通栈的push() 和 pop() 函数的复杂度为O(1) 而获取栈最小值 min()
        函数需要遍历整个栈，复杂度为O(n)

        难点： 将 min() 函数复杂度降为O(1)，可通过建立辅助栈实现

        复杂度分析：
            时间复杂度O(1)
            空间复杂度O(n)

    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.aux_stack = []


    def push(self, x: int) -> None:
        '''
            push(x) 终点为保持辅助栈的元素是非严格降序

            将x压入栈A
            若1栈B为空 或2 x 小于等于栈B的栈顶元素，则将x 压入栈B
        '''
        if len(self.main_stack) == 0:
            self.main_stack.append(x)
            self.aux_stack.append(x)
        else:
            self.main_stack.append(x)   
            last_value = self.aux_stack[-1]
            if last_value > x:
                self.aux_stack.append(x)
            else:
                self.aux_stack.append(last_value) 


    def pop(self) -> None:
        '''
            重点为保持栈A，B元素一致性
            即同时保持栈A，栈B出栈
        '''
        if not self.main_stack:
            return None
        self.aux_stack.pop()
        self.main_stack.pop()


    def top(self) -> int:
        '''
            直接返回主栈或者辅栈的栈顶元素
        '''
        if not self.main_stack:
            return None
        return self.main_stack[-1]


    def min(self) -> int:
        '''
            直接返回辅助栈的栈顶元素
        '''
        if not self.aux_stack:
            return None
        return self.aux_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
