#_*_coding:utf-8_*_
'''
  题目 14   最长公共前缀

  编写一个函数来查询字符串数组中的最常公共前缀。

  如果不存在公共前缀，返回空字符串""

示例 1:
  输入: ["flower","flow","flight"]
  输出: "fl"

示例 2:
  输入: ["dog","racecar","car"]
  输出: ""
  解释: 输入不存在公共前缀。


说明:
  所有输入只包含小写字母 a-z 。
'''
from typing import List

class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
      '''
        我这里做纵向扫描，也就是从前向后遍历所有字符串的每一列，
        比较相同列行的字符是否相同，如果相同则继续对下一列的字符进行比较
        如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀

        复杂度分析：
          时间复杂度：O(nm)  其中m为字符串数组的长度，n为列表长度（即字符串的数量）
            最坏的情况下，字符串数组中每个字符串的每个字符都要被比较一次
          空间复杂度：O(1)
      '''
      if len(strs) == 0:
        return ''
    
      minstrlenghth = 10**9
      for s in strs:
        if len(s) < minstrlenghth:
          minstrlenghth = len(s)
      print(minstrlenghth)
      for i in range(minstrlenghth):
        temp = strs[0][i]
        for j in range(1, len(strs)):
          if strs[j][i] != temp:
            return strs[0][:i]
      return strs[0][:minstrlenghth]

    def longestCommonPrefix(self, strs: List[str]) -> str:
      '''
        利用Python特性，取每一个单词的同一位置的字母，看是否相同
      '''
      res = ''
      for temp in zip(*strs):
        temp_set = set(temp)
        if len(temp_set) == 1:
          res += temp[0]
        else:
          break
      return res



strs = ["dog","racecar","car"]
strs1 = ["flower","flow","flight", 'fl']
strs2 = ["","b"]
print(Solution().longestCommonPrefix(strs1))


