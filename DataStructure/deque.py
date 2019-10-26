# _*_coding:utf-8_*_

# 创建双向队列
from collections import deque

d = deque()

# append（往右边添加一个元素）
d.append(1)
d.append(2)
print(d)  # deque([1, 2])

# appendleft（往左边添加一个元素）
d.appendleft(11)
d.appendleft(22)
print(d)  # deque([22, 11, 1, 2])

# clear清空队列
d.clear()
print(d)  # deque([])

# 浅copy copy
d.append(1)
new_d = d.copy()
print(new_d)  # deque([1])

#  count(返回指定元素的出现次数)
d.append(1)
d.append(1)
print(d)  # deque([1, 1, 1])
print(d.count(1))  # 3

# extend(从队列右边扩展一个列表的元素)
d.append(2)
d.extend([3, 4, 5])
print(d)  # deque([1, 1, 1, 2, 3, 4, 5])

# extendleft(从队列左边扩展一个列表的元素)
d.extendleft([3, 4, 5])
print(d)  # deque([5, 4, 3, 1, 1, 1, 2, 3, 4, 5])

#  index（查找某个元素的索引位置）
d.clear()
d.extend(['a', 'b', 'c', 'd', 'e'])
print(d)
print(d.index('e'))
print(d.index('c', 0, 3))  # 指定查找区间
'''
deque(['a', 'b', 'c', 'd', 'e'])
4
2
'''

#  insert（在指定位置插入元素）
d.insert(2, 'z')
print(d)
# deque(['a', 'b', 'z', 'c', 'd', 'e'])

# pop（获取最右边一个元素，并在队列中删除）
x = d.pop()
print(x)
print(d)
'''
e
deque(['a', 'b', 'z', 'c', 'd'])
'''

# popleft（获取最左边一个元素，并在队列中删除）
print(d)
x = d.popleft()
print(x)
print(d)
'''
deque(['a', 'b', 'z', 'c', 'd'])
a
deque(['b', 'z', 'c', 'd'])
'''

# remove（删除指定元素）
print(d)
d.remove('c')
print(d)
'''
deque(['b', 'z', 'c', 'd'])
deque(['b', 'z', 'd'])
'''

# reverse（队列反转）
print(d)
d.reverse()
print(d)
'''
deque(['b', 'z', 'd'])
deque(['d', 'z', 'b'])
'''

# rotate（把右边元素放到左边）
d.extend(['a', 'b', 'c', 'd', 'e'])
print(d)
d.rotate(2)  # 指定次数，默认1次
print(d)
'''
deque(['d', 'z', 'b', 'a', 'b', 'c', 'd', 'e'])
deque(['d', 'e', 'd', 'z', 'b', 'a', 'b', 'c'])
'''
