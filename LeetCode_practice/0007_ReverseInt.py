#_*_coding:utf-8_*_
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

'''
class Solution:
    def reverse(self, x: int) -> int:
        '''
        先将输入的整数各个位置的数字分别提取（摸运算和除运算结合）存储到list数组中
        注意此时数字顺序相反，再利用数组的 reserved将其翻转，再乘以10的n次方相乘再 相加

        或者对当前数取对10的余数，再一项项填入res尾部，即可完成int翻转
        int取值范围为[−2**31,  2**31 − 1] 如果翻转数字溢出，则立即返回0
        ## 注意存储数字理论上式无限长度，因此每次计算完成后判断res与of的代销关系
         由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。
        <<：左移操作，2的幂相关    >>：右移操作，2的幂相关
        :param x:
        :return:
        '''
        y, res = abs(x), 0
        of = (1 << 31)-1 if x >0 else 1 << 31
        while y!=0:
            res = res *10 + y%10
            if res > of:return 0
            y //= 10
        return res if x > 0 else -res

    def reverse1(self, x: int) -> int:
        '''
        x//max(1, abs(x)) 意味着0:x 为正，-1：x为负
        [::-1] 代表序列反转
        2^31 和 -2^31 的比特数为32，其中正负号占用了一位
        32位整数范围 [−2^31, 2^31 − 1] 中正数范围小一个是因为0的存在
        :param x:
        :return:
        '''
        r = x // max(1, abs(x)) * int(str(abs(x))[::-1])
        return r if r.bit_length() < 32 or r == -2**31 else 0


def reverse1(x):
    symbol = x // max(1, abs(x))
    str_x = str(abs(x))
    res = int(str_x[::-1]) * symbol
    # return res
    return res if res.bit_length() < 32 or res == -2 * 31 else 0


def reverse2(x):
    symbol = 1 if x > 0 else -1
    str_x = str(abs(x))
    res = int(str_x[::-1]) * symbol
    return res
    # return res if res.bit_length() < 32 or res == -2 * 31 else 0


print(reverse2(x=-123))  # -321
print(reverse2(x=-1230))  # -321
print(reverse1(x=0))  # -321
print(reverse2(x=0))  # -321
