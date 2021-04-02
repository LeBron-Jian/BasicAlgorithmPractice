#_*_coding:utf-8_*_
'''

    面试题01.02  判断是否互为字符重排

    题目：给定两个字符串 s1 和 s2 ，请编写一个程序，确定其中一个字符串的字符
    重新排列后，能否变成另一个字符串。


示例 1：
    输入: s1 = "abc", s2 = "bca"
    输出: true 
    
示例 2：
    输入: s1 = "abc", s2 = "bad"
    输出: false

说明：
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100



'''
from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        list1, list2 = list(s1), list(s2)
        for i in range(len(list1)):
            if list1[i] in list2:
                list2.remove(list1[i])

        if len(list2) == 0:
            return True
        else:
            return False
       
    def CheckPermutation2(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
    
    def CheckPermutation3(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
    
