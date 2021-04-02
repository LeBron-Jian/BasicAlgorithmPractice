#_*_coding:utf-8_*_
'''
    面试题01.06  字符串压缩
    题目：字符串压缩，利用字符串重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
        比如，字符串 aabcccccaaa 会变成 a2b1c5a3。若“压缩”后的字符串没有变短，则返回
        原先的字符串。你可以假设字符串只包含大小写英文字母（a至z)。
示例1:
     输入："aabcccccaaa"
     输出："a2b1c5a3"
示例2:
     输入："abbccd"
     输出："abbccd"
     解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：
    字符串长度在[0, 50000]范围内。
'''
class Solution:
    def compressString(self, S: str) -> str:
        '''
            模拟：字符串压缩的方式就是将连续出现的相同字符按照 字符 + 出现次数 压缩。
            如果压缩后的字符串长度变短，则返回压缩后的字符串，否则保留原来的字符串。
            所以我们模拟这个过程构建字符串即可。
            从左往右遍历字符串，用 列表记录当前要压缩的字符，用count 记录 其出现的次数
            如果当前枚举到的字符 s[i] == s[i+1] 则 count +=1，否则我们就更新到列表中
            完成对 字符串的压缩
            在遍历结束后，我们就得到了压缩后的字符串，并将其与原字符串比较，如果长度没有
            变短，则返回原串，否则返回压缩后的字符串。
            复杂度分析：
                时间复杂度：O(n)  n为字符串的长度
                空间复杂度：O(1)  只需要常数空间存储变量
        '''
        res = ''
        count = 1
        frequency = []
        S += " "
        for i in range(len(S)-1):
            
            if S[i] == S[i+1]:
                count += 1
            else:
                frequency.append([S[i], count])
                count = 1
        S = S[:len(S)-1]
        for j in frequency:
            res += j[0] + str(j[1])

        if len(S) <= len(res):
            return S
        else:
            return res


    def compressString1(self, S: str) -> str:
        ch, res, count  = S[0], '', 0

        for i in S:
            if i == ch:
                count += 1
            else:
                res += i + str(count)
                ch = i
                count = 1

        res += ch + str(count)

        return res if len(res) < len(S) else S
