# _*_coding:utf-8_*_
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        滑动过程：滑动窗口两边界均是闭的，最开始滑动窗口里没有元素，即 left=0,right=-1
        res用来存储最常窗口的长度，初始为0，移动窗口，窗口向右判断下一个元素是否已存在于
        窗口内，如果不存在，则将该元素加入到窗口中，即 right+1，左边界不动，如果窗口内已经存在该元素
        则将该元素加入到窗口中，即right+1，同时将窗口左边界移到窗口中已存在的元素的位置，即 left+1
        知道窗口中重复的元素的位置为止，同时将窗口左边界移到窗口中已经存在的元素为止，
        即left+1直到窗口中重复元素的位置为止，重复上述步骤，在窗口滑动的过程中，每得到一个新的窗口
        都将与res中的值比较，res中始终存放的是之前所有窗口的最常长度。

        判断元素在窗口中是否已经存在
        通过计算频率的方法判断是否已经存在，Python中使用collection中的 defaultdict类来存放
        每个元素的频率。每向窗口中加入一个元素，则该元素的频率设为1，每去掉一个元素，则将移除元素
        的频率重置为0，所以窗口中每个元素的频率都是1，若下一个元素的频率为0时，说明窗口不存在该元素
        若下一个元素的频率为1时，说明该元素在窗口中已经存在。
        :param s:
        :return:
        '''
        from collections import defaultdict

        # sliding window
        freq = defaultdict(int)

        # [left...right] as a sliding window
        left = res = 0
        right = -1

        while left < len(s):
            if right + 1 < len(s) and freq[s[right + 1]] == 0:
                right += 1
                freq[s[right]] += 1
            else:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res

    def lengthOfLongestSubstring1(self, s: str) -> int:
        '''
        滑动窗口简单版本：
        取left和right作为窗口的边界，right取不断右移，扩大窗口长度，一旦 s[right]与
        窗口内的值重复，则舍弃重复点之左的所有子串， 也就是将left移动到重复点之右
        然后重新增长窗口，因为当出现重复之后，想要探究是否有更长的不重复子串，能利用的
        部分只有窗口内重复点之右的子串，
        :param s:
        :return:
        '''
        left = 0
        right = left + 1
        num = len(s)
        max_len = 1
        if not s:
            return 0
        if len(s) == 1:
            return 1
        while right < num:
            if s[right] not in s[left:right]:
                right += 1
                if right - left > max_len:
                    max_len = right - left
            else:
                # left边界移动一定要注意，一定要在left和right之间的窗口s[left:right]内
                # 找到重复的的点，注意不要直接s.index(s[rigt])
                left = s[left:right].index(s[right]) + left + 1
                right += 1
        return max_len
