# _*_coding:utf-8_*_

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

# 其中x1, y1, x2, y2表示，开始的地址和结束的地址
def maze_path(x1, y1, x2, y2):
    '''
    总体思路就是有路则进栈，没有路则出栈，直到走完
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    '''
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1]  # 当前节点是 stack最后一个位置
        if curNode[0] == x2 and curNode[1] == y2:
            # 表示走到终点了
            for p in stack:
                print(p)
            return True  # 如果有路则返回TRUE，没有路则返回FALSE
        # x,y当前坐标，四个方向上下左右分别是：x-1,y  x+1,y  x, y-1  x,y+1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过了
                break
        else:  # 如果一个都找不到，就需要回退了
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()  # 栈顶出栈，也就是回退

    else:
        print("没有路")
        return False


maze_path(1, 1, 8, 8)
