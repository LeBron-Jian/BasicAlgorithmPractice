#_*_coding:utf-8_*_
'''
题目：
    剑指offer 50  第一次只出现一次的字符

    在字符串s中找出第一个只出现一次的字符，如果没有，返回一个单空格，s只包含小写字母

示例：

    s = "abaccdeff"
    返回 "b"

    s = "" 
    返回 " "


限制：
    0 <= s的长度 <= 10000
'''
import collections

class Solution1:
    def firstUniqChar(self, s: str) -> str:
        '''
            哈希表解法

            最初想到的方法就是通过一个字典，我们将数字统计到字典里面，然后找统计值为1的字符串

            时间复杂度为O(n)
            空间复杂度为O(n)
            网上说，s只包含小写字母，因此最多有26个不同字符，hashMap存储需要占用O(26)个额外空间
            即空间复杂度为O(1)

            因为Python3.6之后，默认字典就是有序的因此无需使用 OrderedDict()
        '''
        if len(s) == 0:
            return ' '
        res = {}
        for i in s:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
        print(res)
        for key, value in res.items():
            print(key, value)
            if value == 1:
                return key
            else:
                continue
        return ' '

    def firstUniqChar1(self,s):
        # 利用counter计数器保留出场顺序的特性进行计数
        dic = collections.Counter(s)
        for i in s:
            if dic[i] == 1:
                return i
        return ' '

    def firstUniqChar2(self,s):
        '''
            暴力解法
        '''
        for i in range(len(s)):
            for j in  range(i, len(s)):
                if i != j:
                    return i
        return ''

class Solution:
    def firstUniqChar(self, s: str) -> str:
        '''
            但是这样写有个问题，就是当s里面有三个同一类的字符串，可能会为False
        '''
        dic = {}
        for c in s:
            # dic[c] = not c in dic
            if c in dic:
                dic[c] = False
            else:
                dic[c] = True
            print(dic)
        for c in s:
            if dic[c]:
                return c
        return ' '


s = "loveleetcode"
print(Solution().firstUniqChar(s))
# print(collections.Counter(s))
# 利用counter计数器保留出场顺序的特性进行计数
# Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})

'''
{'l': True, 'o': True, 'v': True}
{'l': True, 'o': True, 'v': True, 'e': True}
{'l': False, 'o': True, 'v': True, 'e': True}
{'l': False, 'o': True, 'v': True, 'e': False}
{'l': False, 'o': True, 'v': True, 'e': False}
{'l': False, 'o': True, 'v': True, 'e': False, 't': True}
{'l': False, 'o': True, 'v': True, 'e': False, 't': True, 'c': True}
{'l': False, 'o': False, 'v': True, 'e': False, 't': True, 'c': True}
{'l': False, 'o': False, 'v': True, 'e': False, 't': True, 'c': True, 'd': True}

{'l': False, 'o': False, 'v': True, 'e': False, 't': True, 'c': True, 'd': True}

'''
