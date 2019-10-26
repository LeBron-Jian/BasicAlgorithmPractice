'''
问题描述：大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从上往下
按照大小顺序摞着64片黄金圆盘。大梵天命名婆罗门把圆盘从下面开始按大小顺序
重新摆放在另一个柱子上。在小圆盘上不能放大圆盘，在三根柱子之间只能移动一个圆盘。
64根柱子移动完毕之日，就是世界毁灭之时。
'''
def hanoi(x,a,b,c):
    if x>0:
        # 除了下面最大的盘子，剩余的盘子从a移动到b
        hanoi(x-1,a,c,b)
        # 把最大的盘子从a移动到c
        print('%s——%s'%(a,c))
        # 把剩余的盘子 从b 移动到c
        hanoi(x-1,b,a,c)


hanoi_result = hanoi(2,'A','B','C')


# 计算次数
def cal_times(x):
    num = 1
    for i in range(x-1):
        num = 2*num +1

    print(num)
cal_times(2)

# import sys
# sys.setrecursionlimit()