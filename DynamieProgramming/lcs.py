# _*_coding:utf-8_*_

def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # i j 位置上的字符匹配的时候，来自于左上方+1
                c[i][j] = c[i - 1][j - 1] + 1

    # 可以打印
    # for _ in c:
    #     print(c)
    return c[m][n]


print(lcs_length('ABCBDAB', 'BDCABA'))


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 1左上方    2上方    3左方
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # i j 位置上的字符匹配的时候，来自于左上方+1
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:  # 来自于上方
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b


def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自左上方 =>匹配
            res.append(x[i - 1])
            j -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自上方=> 不匹配
            i -= 1
        else:  # ==3  来自于左方=> 不匹配
            j -= 1
    return "".join(reversed(res))
