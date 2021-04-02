#_*_coding:utf-8_*_
'''

    面试题01.01  判定字符是否唯一

    题目：实现一个算法，确定一个字符串 s 的所有字符是否全都不同。


示例 1：
    输入: s = "leetcode"
    输出: false 

示例 2：
    输入: s = "abc"
    输出: true

限制：
    0 <= len(s) <= 100
    如果你不使用额外的数据结构，会很加分。

'''

class Solution:
    def isUnique(self, astr: str) -> bool:
        res = []
        for i in astr:
            if i in res:
                return False
            else:
                res.append(i)
        return True

    def isUnique2(self, astr: str) -> bool:
        return len(astr) == len(set(astr))
