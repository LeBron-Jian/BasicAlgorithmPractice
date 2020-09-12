#_*_coding:utf-8_*_
'''
557：翻转字符串中的单词 III
给定一个字符串，你需要翻转字符串中每个单词的字符顺序，同时仍保留
空格和单词的初始顺序。
示例1：
    输入: "Let's take LeetCode contest"
    输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会与任何额外的空格
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        时间复杂度 O(n) 其中n是字符串的长度
        空间复杂度 O(1)
        :param s:
        :return:
        '''
        ss = s.split()
        s_list = []
        for i in range(len(ss)):
            s_list.append(ss[i][::-1])
        return " ".join(s_list)

def reverseWords1(s):
    s = s.split()
    print(s)
    s_output = []
    for i in range(len(s)):
        s_output.append(s[i][::-1])
    s_output = " ".join(s_output)
    print(s_output)

def reverseWords(s):
    res = " ".join(word[::-1] for word in s.split())


s = "Let's take LeetCode contest"
s_output = "s'teL ekat edoCteeL tsetnoc"
reverseWords(s)

