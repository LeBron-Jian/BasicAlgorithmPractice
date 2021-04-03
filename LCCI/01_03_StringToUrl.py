#_*_coding:utf-8_*_
'''

    面试题01.03  URL 化

    题目：URL 化。 编写一种方法，将字符串中的空格全部替换为 %20。假定该字符串尾部有足够的空间存放新增字符。
    并且知道字符串的“真实”长度。


示例 1：
    输入："Mr John Smith    ", 13
    输出："Mr%20John%20Smith"


示例 2：
    输入："               ", 5
    输出："%20%20%20%20%20"
 

提示：
    字符串长度在 [0, 500000] 范围内。


'''

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        '''
            依据题意，输出的字符串长度为length；里面的空格全部转换为 "%20"
        '''
        res = ''
        count = 0
        for i in S:
            if i.isspace():
                res += '%20'
            else:
                res += i
            count += 1
            if count == length:
                return res

    def replaceSpaces1(self, S: str, length: int) -> str:
        '''
            面试官肯定不会考这个了。。。。
        '''
        return S[:length].replace(' ', '%20')

    def replaceSpaces3(self, S: str, length: int) -> str:
        res = ''
        for i in range(length):
            if S[i].isspace():
                res += '%20'
            else:
                res += S[i]
        return res
