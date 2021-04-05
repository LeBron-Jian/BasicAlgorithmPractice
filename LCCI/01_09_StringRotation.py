#_*_coding:utf-8_*_
'''
    01.09  字符串轮转

    题目： 字符串轮转。给定两个字符串s1, s2。请编写代码检查 s2 是否为 s1 旋转而成。
            （比如： waterbottle 是 erbottlewat 旋转后的字符串）


示例1:
        输入：s1 = "waterbottle", s2 = "erbottlewat"
        输出：True

示例2:
        输入：s1 = "aa", s2 = "aba"
        输出：False


提示：
        字符串长度在[0, 100000]范围内。

说明:
        你能只调用一次检查子串的方法吗？


'''

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        '''
            首先判断长度是否一致，不相同返回False，
            其次拼接两个 s2，如果是由 s1旋转而成，则拼接后的s 一定包含 s1。

            复杂度分析：
                时间复杂度：O(N)
                空间复杂度：O(N)
        '''
        if len(s1) != len(s2):
            return False
        compare =  s2 + s2
        return s1 in compare

    def isFlipedString2(self, s1: str, s2: str) -> bool:
        '''
            逐个比较，笨方法
            注意： s1, s2 = '', ''
        '''
        if s1 == s2:
            return True
        for i in s1:
            if s1[i:] + s1[:i] == s2:
                return True

        return False


s1 = "ac"
s2 = "ac"

print(Solution().isFlipedString(s1, s2))
