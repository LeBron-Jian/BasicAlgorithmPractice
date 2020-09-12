# _*_coding:utf-8_*_
'''
415：字符串相加
题目：
给定两个字符串形式的非负整数 num1和num2，计算他们的和
提示：
    num1 和num2 的长度都小于 5100
    num1 和num2 都只包含数字 0-9
    num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式


'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pass


def addStrings1(str1, str2):
    '''
    方法1，直接偷鸡摸狗，使用人家不推荐的内建库
    当然我们写的目的是熟悉eval()方法
    '''
    return str(eval(str1) + eval(str2))


def addStrings2(str1, str2):
    '''
    字符串相加，双指针，算法流程：设定i, j两指针分别指向str1, str2
    代表当前位相加是否产生进位。
    添加当前位：计算 tmp = n1 + n2 + carry，并将当前位 tmp % 10，添加到 res头部
    索引溢出处理：当指针i 或j走过数字首部后，给n1，n2赋值为00
    相当于给str1, str2中长度较短的数字签名填00，以便后面计算。
    当遍历完 num1, num2后跳出循环，并根据 carry值决定是否在头部添加进位11
    最终返回 res即可
    :param str1:
    :param str2:
    :return:
    '''
    res = ''
    i, j, carry = len(str1) - 1, len(str2) - 1, 0
    while i >= 0 or j >= 0:
        n1 = int(str1[i]) if i >= 0 else 0
        n2 = int(str2[j]) if j >= 0 else 0
        tmp = n1 + n2 + carry
        carry = tmp // 10
        res = str(tmp % 10) + res
        i, j = i - 1, j - 1
    return "1" + res if carry else res

res = addStrings2('3133', '32313')
print(res, type(res))


def addStrings3(str1, str2):
    '''
    使用暴力破解，直接遍历两个字符串，每个乘以当前位数的10的幂，最后加一起
    时间复杂度 O(n+n)
    '''
    num11, num22 = 0, 0
    flag1, flag2 = 1, 1
    for i in num1:
        num11 += int(i)*(10**(len(num1)-flag1))
        flag1 += 1
    for i in num2:
        num22 += int(i)*(10**(len(num2)-flag2))
        flag2 += 1
    return str(num11 + num22)