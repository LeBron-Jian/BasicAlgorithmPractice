#_*_coding:utf-8_*_

class Chaintable:
    def __init__(self, item):
        self.item = item
        self.next = None

# 链表永远有一个头结点，head

def print_linklist(lk):
    while lk:
        print(lk.item)
        lk = lk.next

# 头插法
def create_linklist_head(li):
    head = Chaintable(li[0])
    for element in li[1:]:
        node = Chaintable(element)
        node.next = head
        head = node
    return head

#尾插法
def create_linklist_tail(li):
    head = Chaintable(li[0])
    tail = head
    for element in li[1:]:
        node = Chaintable(element)
        tail.next = node
        tail = node
    return head

lk = create_linklist_head([1, 2, 3, 4])
# print(lk.item)  # 4
print_linklist(lk)  # 4,3,2,1,*********

lk = create_linklist_tail([1, 2, 3, 4, 5])
print_linklist(lk)  # 1,2,3,4,5,