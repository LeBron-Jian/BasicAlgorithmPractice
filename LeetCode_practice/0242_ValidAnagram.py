#_*_coding:utf-8_*_
'''
题目： 241  有效的字母异位词

    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true

示例 2:
    输入: s = "rat", t = "car"
    输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        我的思路是将其转化为一个列表，首先判断列表长度是否一致，如果一致的话，
        那么进而可以判断列表里面的元素是否相等，如果不一致的话直接返回FALSE
        一致的话，我们可以从列表s中找t里的元素。


        :param s:
        :param t:
        :return:
        '''
        s = list(s)
        t = list(t)
        if len(s) == len(t):
            for i in s:
                if i in t:
                    t.remove(i)
            if len(t) == 0:
                return True
            else:
                return False
        else:
            return False

    def isAnagram0(self, s, t):
        '''
            排序后，我们可以看两个字符串排序后是否相等，此外，如果s和t的
            长度不同，t和s 不然不是异位词
            复杂度分析：
                时间复杂度：O(nlogn)  其中 n为s的长度，排序的时间复杂度为O(nlogn)
                        比较两个字符串是否相等，则时间复杂度为O(n)
                空间复杂度：O(logn) 排序需要O(logn)的空间复杂度
        '''
        return sorted(list(s)) == sorted(list(t))

    def isAnagram1(self, s, t):
        dict1 = []  # ['a':1, 'b':2]
        dict2 = []
        for ch in s:
            # if ch in dict1:
            #     dict1[ch] += 1
            # else:
            #     dict1[ch] = 1

            # 一种更快的方法
            dict1[ch] = dict1.get(ch, 0) + 1

        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict1 == dict2

    def isAnagram2(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)