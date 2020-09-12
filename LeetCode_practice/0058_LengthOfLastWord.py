# _*_coding:utf-8_*_
'''
58：最后一个单词的长度
题目：给定一个仅包含大小写字母和空格' ' 的字符串 s，返回其最后一个单词的长度
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回0。
说明：一个单词是指仅由字母组成，不包含任何空格的 最大子字符串。

示例：
    输入: "Hello World"
    输出: 5
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Python 对字符串进行split切分操作
        s = s.split()
        return len(s[-1]) if s else 0
