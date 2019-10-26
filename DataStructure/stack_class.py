#_*_coding:utf-8_*_

class Stack:
    def __init__(self):
        self.stack = []

    # 进栈操作（压栈）  push
    def push(self, element):
        self.stack.append(element)

    # 出栈操作  pop
    def pop(self):
        # 移除列表中的一个元素（默认最后一个），并返回该元素的值
        # 因为栈是先进后出，出栈肯定走的是最后一个元素
        return self.stack.pop()

    # 取栈顶
    def gettop(self):
        # 取栈顶的元素我们需要考虑是否有元素
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(1)
stack.push(0)
stack.push(2)
print(stack.pop())  # 2