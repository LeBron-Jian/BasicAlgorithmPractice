# _*_coding:utf-8_*_
import time


# 给递归函数一个装饰器，它就递归的装饰！！ 所以为了防止这样我们再套一层即可
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time : %s secs' % (func.__name__, t2 - t1))
        return result

    return wrapper


# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 28, 30, 33, 36, 39, 40]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n - i))
        return res


# print(cut_rod_recurision_1(p, 9))


def cut_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurision_2(p, n - i))
        return res


# print(cut_rod_recurision_2(p, 9))

@cal_time
def c1(p, n):
    return cut_rod_recurision_1(p, n)

@cal_time
def c2(p, n):
    return cut_rod_recurision_2(p, n)


print(c1(p, 10))
print(c2(p, 10))
'''
c1 running time : 0.02000117301940918 secs
30
c2 running time : 0.0010001659393310547 secs
30
'''
@cal_time
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j]+r[i-j])
        r.append(res)
    return r[n]

print(cut_rod_dp(p, 10))

def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    # 这个循环的意思是从底向上计算
    for i in range(1, n+1):
        res_r = 0  # 用来记录价格的最优值
        res_s = 0  # 用来记录切割左边的最优长度
        for j in range(1, i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n>0:
        ans.append(s[n])
        n-= s[n]
    return ans


print(cut_rod_extend(p, 10))
# (30, [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])
print(cut_rod_solution(p, 9))
# [3, 6]