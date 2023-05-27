#_*_coding:utf-8_*_
'''
题目：
    剑指offer 58_2  左旋转字符串

    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现
    字符串左旋转操作的功能。比如，输入字符串 'abcdefg' 和数字2，该函数将返回左旋转两位
    得到的结果 ‘cdefgab'

示例 1：
    输入: s = "abcdefg", k = 2
    输出: "cdefgab"

示例 2：
    输入: s = "lrloseumgh", k = 6
    输出: "umghlrlose"
 

限制：
    1 <= k < s.length <= 10000


'''

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        '''
            本题做法比较多，主要学习字符串切片，列表遍历拼接 字符串遍历拼接
            1，字符串切片
            时间复杂度：O(n)  其中n为字符串的长度，字符串切片函数为线性时间复杂度
            空间复杂度：O(n) 两个字符串切片的总长度为N
        '''
        return s[n:] + s[:n]

    def reverseLeftWords1(self, s: str, n: int) -> str:
        '''
            若面试规定不允许使用切片函数，则尝试此方法
            算法流程：
                1，新建一个list，记为res
                2，先像res添加“第 n+1”位至末尾的字符
                3，再向res添加“首位至n位的字符
                4，将res转换为字符串并返回
            时间复杂度为：O(n)  线性遍历s并添加，使用线性时间
            空间复杂度为O(n)：新建的辅助res使用O(N) 大小的额外空间
        '''
        res = []
        for i in range(n, len(s)):
            res.append(s[i])   # 添加第n+1位至末位的字符
        for i in range(n):
            res.append(s[i])   # 添加首位至第n位的字符
        return ''.join(res)    # 转换为字符串并返回

    def reverseLeftWords2(self, s: str, n: int) -> str:
        '''
            若规定Python不能使用join()函数
            则我们使用字符串取代列表，方法同上2

            时间复杂度O(n)：线性遍历s并添加，使用线性时间
            空间复杂度O(n)：假设循环过程中内存会被及时回收，内存中至少同时存在长度为n和n-1的
                            两个字符串，因此至少使用O(n)的额外空间
        '''
        res = ''
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res
