# _*_coding:utf-8_*_
'''
题目：
    8：字符串转换整数（atoi）

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

    首先，该函数会根据需要丢弃无用的开头空格字符直到寻找到第一个非空格的字符为止。接下来的转换规则如下：
        当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
        假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
        该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意： 假如该字符串中的第一个非空格字符不是一个有效整数字符、
      字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
      在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
    假设我们的环境只能存储 32 位大小的有符号整数，
    那么其数值范围为 [−2**31,  2**31 − 1]。如果数值超过这个范围，
    请返回  INT_MAX (2**31 − 1) 或 INT_MIN (−2**31) 。

示例 1:
    输入: "42"
    输出: 42

示例 2:
    输入: "   -42"
    输出: -42
    解释: 第一个非空白字符为 '-', 它是一个负号。
         我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例 3:
    输入: "4193 with words"
    输出: 4193
    解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:
    输入: "words and 987"
    输出: 0
    解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
         因此无法执行有效的转换。

示例 5:
    输入: "-91283472332"
    输出: -2147483648
    解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
         因此返回 INT_MIN (−2**31) 。
'''
import re
'''
为什么可以使用正则表达式，如果整数过大溢出怎么办？
    题目描述：假设我们的环境只能存储 32 位大小的有符号整数
    首先，这个假设对于Python不成立，Python不存在 32 位的 int 类型。
    其次，即使搜索到的字符串转32位整数可能导致溢出，我们也可以直接通过
    字符串判断是否存在溢出的情况（比如try函数或者判断字符串长度+字符串比较）
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        ^ 匹配字符串开头
        [\+\-]：代表一个+字符或者一个-字符
        ？：前面一个字符可有可无
        \d 一个数字
        + 前面的一个字符的一个或多个
        \D 一个非数字字符
        * 前面一个字符的0个或多个
        max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界
        '''
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 32 - 1), -2 ** 32)


    def myAtoi1(self, s):
        INT_MAX, INT_MIN = 2**31-1, -2**31
        # 清除左边多余的空格
        s = s.lstrip()
        # 设置正则规则
        num_re = re.compile(r'^[\+\-]?\d+')
        # 查找匹配的内容
        num = num_re.findall(str)
        # 由于返回的是一个列表，解包并且转换成整数
        num = int(*num)
        return max(min(num, INT_MAX), INT_MIN)



    def myAtoi2(self, s: str) -> int:
        # 去掉左边字符
        s = s.lstrip()  # 截掉左边的空格
        # 如果字符串为空，则返回
        if len(s) == 0:
            return 0
        # 设置默认输出为0
        res = 0
        # 如果有符号设置起始位置2，其余的为1
        i = 2 if s[0] == '-' or s[0] == '+' else 1
        # i = 1 if s[0] == '-' or s[0] == '+' else 0
        # 循环，知道无法强制转成Int，跳出循环
        while i <= len(s):
            try:
                res = int(str[:i])
                # res = int(str[:i+1])
                i += 1
            except:
                break

        # 如果数字超过范围，返回范围最大值
        if res < -2 ** 31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res


INT_MAX, INT_MIN = 2**31-1, -2**31
class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c=='+' or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solutions:

    def myAtoi(self, s: str) -> int:
        '''
            官方解答：自动机
                我们的程序在每个时刻都有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c
                转移到下一个状态 s'。这样我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s'
                的表格即可解决问题。

                        ''        +/-       number      other

            start       start   signed     in_number     end
            signed      end       end      in_number     end
            in_number   end       end      in_number     end
            end         end       end       end          end
        '''
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans
        
