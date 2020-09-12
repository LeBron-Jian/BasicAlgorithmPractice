# _*_coding:utf-8_*_
'''
5 最长回文子串
题目：
给定一个字符串 s，找到s中最长的回文子串，你可以假设 s的最大长度为 1000

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        思路：动态规划（官方解法）
        对于一个子串而言，如果他是回文串，并且长度大于22，那么将它首尾的两个字母去掉之后，
        它仍然是个回文串。根据这一的思路，我们就可以使用动态规划来解决这个问题
        我们用P(i,  j)表示字符串ss的第ii到jj个字母组成的串，（
        下文表示成 s[i, j]是否为回文串
        这里的其他情况包含两组可能性：
            1，s[i, j]本身不是一个回文串
            2，i > j此时 s[i, j] 本身不合法

        :param s:
        :return:
        '''
        pass

def longestPalindrome1(s):
    '''
    我比较菜，想到的就是时间复杂度高的，拿到字符串，将字串符与原字符串取反进行比较
    如果不相等，则缩短长度，分别比较，以此类推，这个解法的好处就是一次判断成功可以直接返回结果
    坏处就是复杂度高的一P
    :param s:
    :return:
    '''
    # for right in range(len(s), -1, -1):
    #     for left in range(len(s)-right+1):
    #         sub_string = s[left:left+right]
    #         if sub_string == sub_string[::-1]:
    #             return sub_string

    # 这个代码有问题，比如bccd，结果是b
    for left in range(len(s)):
        for right in range(len(s)-left+1, -1, -1):
            sub_string = s[left:left+right]
            if sub_string == sub_string[::-1]:
                return sub_string

def longestPalindrome(s):
    '''
    参考：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/pythonshuang-bai-50msyi-lun-bian-li-fa-5-zui-chang/
    其解题思路：因为题目要的是最长回文，所以不用验证更短的子串
    或者说，就是以尾坐标为标志进行验证，也不用担心错过更长的结果
    效果是只需要遍历一次，时间空间都是双百
    :param s:
    :return:
    '''
    length = len(s)
    if length == 0:
        return ''
    if length == 1:
        return s
    if length == 2 and s == s[::-1]:
        return s
    max_length, start = 1, 0
    for i in range(1, length):
        even_number = s[i-max_length:i+1]
        odd_number = s[i-max_length-1:i+1]
        if i-max_length-1 >= 0 and odd_number == odd_number[::-1]:
            start = i-max_length-1
            max_length += 2
            continue
        if i-max_length-1 >= 0 and even_number == even_number[::-1]:
            start = i-max_length
            max_length += 1
            continue
    return s[start:start + max_length]



res = longestPalindrome(s='bcacd')
print(res)
