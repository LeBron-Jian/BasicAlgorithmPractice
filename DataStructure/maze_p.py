# _*_coding:utf-8_*_
from collections import deque

# 迷宫问题，0表示通道，1表示围墙
# 给出算法，求出一个通道

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 这里我们封装一个列表,用来表示走迷宫的四个方向
dirs = [
    lambda x, y: (x + 1, y),  # 表示向上走
    lambda x, y: (x - 1, y),  # 表示向下走
    lambda x, y: (x, y - 1),  # 表示向左走
    lambda x, y: (x, y + 1),  # 表示向右走
]

def print_r(path):
    real_path = []  # 用来存储真实的路径
    i = len(path) - 1  # 用i指向path的最后一个下标
    while i >= 0:
        real_path.append(path[i][0:2])
        i = path[i][2]
    real_path.reverse()

# 起点坐标（x1, y1)  终点坐标（x2, y2）
def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    path = []
    # -1  为当前path的路径的下标
    queue.append((x1, y1, -1))
    while len(queue) > 0:  # 当队列不空时循环
        # append是从右边加入的，popleft()从左边出去
        cur_Node = queue.popleft()
        path.append(cur_Node)
        if cur_Node[0] == x2 and cur_Node[1] == y2:
            # 如果当前节点等于终点节点，则说明到达终点
            print_r(path)
            return True

        # 队列是找四个方向，每个能走就继续
        for dir in dirs:
            # 下一个方向的节点坐标
            next_node = dir(cur_Node[0], cur_Node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path) - 1))
                maze[next_node[0]][next_node[1]] = 2  # 标记为已走过
    return False  # 如果队列结束了，空了，还没找到路径，则为FALSE


maze_path_queue(1, 1, 8, 8)
