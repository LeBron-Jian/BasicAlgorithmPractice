# _*_coding:utf-8_*_

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    # 最大公约数
    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    # 最小公倍数
    def zgs(self, a, b):
        # 12 16 -> 4
        # 3 * 4 * 4=48
        x = self.gcd(a, b)
        return (a * b / x)

    # 加法的内置方法
    def __add__(self, other):
        # 1/12 + 1/20
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        femzi = a * (fenmu / b) + c * (fenmu / d)
        return Fraction(femzi, fenmu)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)


f = Fraction(30, 16)
print(f)