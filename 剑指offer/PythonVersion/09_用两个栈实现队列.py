#_*_coding:utf-8_*_
'''
    剑指offer 9  用两个栈实现队列

示例 1：
    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

示例 2：
    输入：
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

'''

class CQueue:

    def __init__(self):
        self.main_stack = []
        self.aux_stack = []


    def appendTail(self, value: int) -> None:
        self.main_stack.append(value)


    def deleteHead(self) -> int:
        if not self.main_stack and not self.aux_stack:
        # if len(self.main_stack) == 0 and len(self.aux_stack)==0:
            return -1  
        if not self.aux_stack:
            while self.main_stack:
                self.aux_stack.append(self.main_stack.pop())
            return self.aux_stack.pop()
        return self.aux_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

res = CQueue()
res.appendTail(value=1)
print(res.main_stack, res.aux_stack)
res.appendTail(value=2)
print(res.main_stack, res.aux_stack)
res.appendTail(value=3)
print(res.main_stack, res.aux_stack)
res.deleteHead()
print(res.main_stack, res.aux_stack)
res.deleteHead()
print(res.main_stack, res.aux_stack)

'''
[1] []
[1, 2] []
[1, 2, 3] []
[] [3, 2]
[] [3]
'''
