# _*_coding:utf-8_*_

# 这是一个伪递归
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 16))


def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
