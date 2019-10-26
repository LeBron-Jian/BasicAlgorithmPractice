#_*_coding:utf-8_*_

# t表示商店有的零钱的面额
t = [100, 50, 20, 5, 1]

# n 表示n元钱
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money  # 除法向下取整
        n = n % money  # 除法取余
    return m, n

print(change(t, 376)) # ([3, 1, 1, 1, 1], 0)
