#_*_coding:utf-8_*_
'''
题目：
    剑指offer 58_1  翻转单词的顺序

    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
    例如输入字符串"I am a student. "，则输出"student. a am I"。

示例1：
    输入: "the sky is blue"
    输出: "blue is sky the"

示例 2：
    输入: "  hello world!  "
    输出: "world! hello"
    解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
    输入: "a good   example"
    输出: "example good a"
    解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

说明：
    无空格字符构成一个单词。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
            双指针
            算法解析：
                1，倒序遍历字符串s，记录单词左右索引边界i,j
                2，每确定一个单词的边界，则将其添加到单词列表res
                3，最终，将单词列表拼接为字符串，并返回即可
            复杂度分析：
                时间复杂度O(n)：其中n为字符串s的长度，线性遍历字符串
                空间复杂度O(n)：新建的list的字符串总长度为N,占用O(n)大小的额外空间
        '''
        s = s.strip()
        i = j = len(s)-1
        res = []
        while i>=0:
            while i>=0 and s[i] != ' ':
                i -= 1   # 搜索首个空格
            res.append(s[i+1:j+1])  # 添加单词
            while s[i] == ' ':
                i -= 1    # 跳过单词间空格
            j = i     # j 指向下一各单词的尾字符
        return ' '.join(res)

    def reverseWords1(self, s: str) -> str:
        '''
            分割加倒序
            利用字符串分割，列表倒序的内置函数，可简便的实现本题的字符串翻转要求
            （面试时不建议使用）
            算法分析：
                由于split() 方法将单词间的“多一个空格看做一个空格，因此不会出现多余的
                空单词，因此直接利用reverse()方法翻转单词列表str，拼接为字符串并返回即可

            算法解析：
                1，删除首位空格
                2，分割字符串
                3，翻转单词列表
                4，拼接并返回
        
            复杂度分析：
                时间复杂度O(n)：总体为线性时间复杂度
                    split() 方法为 O(n)
                    join()方法，最差情况下，当字符串全为空格时，为O(n)
                    reverse() 为O(n)

                空间复杂度：O(n)
                    单词列表str 占用线性大小的额外空间


        '''
        s = s.strip().split()  # 删除首尾空格， 分割字符串
        s.reverse()   # 翻转单词列表
        return ' '.join(s)   # 拼接为字符串并返回



s = " a good   example"
s = s.strip().split(' ')
print(s)
s.reverse()
print(s)
