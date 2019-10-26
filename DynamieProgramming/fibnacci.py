# _*_coding:utf-8_*_
from cal_time import cal_time

@cal_time
# 子问题的重复计算
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)

# 写这个是我们会发现计算f(5) 要算两边f(4)
# f(5) = f(4)+f(3)
# f(4) = f(3)+f(2)
# f(3) = f(2)+f(1)
# f(3) = f(2)+f(1)
# f(2) = 1
# 那么同理，算f(6)，我们会计算两次f(5),三次f(4)....
# 当然不是说所有的递归都会重复计算，

# 时间随着数字越大，时间越长
# print(fibnacci(10))  # 55

@cal_time
# 动态规划（DP) 的思想 = 递归式+重复子问题
def fibnacci_n_recurision(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


# print(fibnacci_n_recurision(10))




n1 = 15
n2 = 15
fibnacci(n2)
fibnacci_n_recurision(n1)