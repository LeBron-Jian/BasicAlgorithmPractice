#_*_coding:utf-8_*_

class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针  队尾指针是进队的
        self.front = 0  # 队首指针  队首指针是出队的

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

q = Queue(5)
for i in range(4):
    q.push(i)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
'''
0
1
2
3
'''
