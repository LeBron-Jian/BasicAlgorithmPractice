#_*_coding:utf-8_*_
'''

    面试题01.04  回文排列

    题目：给定一个字符串，编写一个函数判断其是否为某个回文串的排列之一。回文串是指正反两个方向都一样的
    单词或短语，排列是指字母的重新排列。回文串不一定是字典当中的单词。


示例1：
    输入："tactcoa"
    输出：true（排列有"tacocat"、"atcocta"，等等）

'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
            回文数字符串有两种：一种是奇数的，一种是偶数的。
            偶数的我们好判断，只需要找出每个字符串是偶数就可以了。但是奇数就不能使用这个方法了。
            当我们仔细观察就会发现，如果是奇数的话，那么字符串的所有字符只有一个字符是奇数的，
            其他都是偶数。
        '''
        tmp_dict = {}
        for i in s:
            if i not in tmp_dict:
                tmp_dict[i] = 1
            else:
                tmp_dict[i] += 1
        res = 0
        for k,i in tmp_dict.items():
            if i%2 == 1:
                res += 1
        return True if res <=1 else False

    def canPermutePalindrome2(self, s: str) -> bool:
        from collections import Counter
        count = Counter(s)
        res = 0
        for i in count.values():
            if i%2 ==1:
                res += 1
        return True if res <=1 else False
