#_*_coding:utf-8_*_
'''
题目：
    剑指offer 5  替换空格

    请实现一个函数，把字符串 s 中的每个空格替换为 %20


示例 1：
    输入：s = "We are happy."
    输出："We%20are%20happy."
 

限制：
    0 <= s 的长度 <= 10000

'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        '''
            遍历添加
            在Python中字符串被设计成不可变的类型，即无法直接修改字符串的某一个字符
            需要新建一个字符串实现

            算法流程：
                1，初始化一个list，记为res
                2，遍历列表s中每个字符c
                    当c为空格时，向res 添加字符串 “%20”
                    当c不为空格时，向res后添加字符串c
                将列表转换为字符串即可

                当然也可以直接初始化一个空字符串即可

            复杂度分析：
                时间复杂度O(n)：遍历使用O(n)，每轮添加字符操作使用O(1)
                空间复杂度O(n)：Python新建的list使用了线性大小的额外空间
        '''
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else:
                res.append(i)
        return ''.join(res)

    def replaceSpace(self, s: str) -> str:
        '''
            这里初始化一个空字符串
        '''
        res = ''
        for i in s:
            if i.isspace():
                res += '%20'
            else:
                res += i
        return res

    def replaceSpace1(self, s: str) -> str:
        '''
            直接调用api，但是面试使用这个。。。怕是不可以

            Python内置的replace函数用来替换字符串中指定的字符

            因为replace不会在原字符串上修改，所以需要额外的空间

            复杂度分析：
                时间复杂度：O(n)
                空间复杂度：O(n)
        '''
        return s.replace(' ', '%20')

    def replaceSpace2(self, s: str) -> str:
        '''
            方法2：原地修改
            在C++中，string被设计成可变的类型，因此可以在不新建字符串的情况下实现原地修改
            由于需要将空格替换为 "%20" ，字符串的总字符数增加，因此需要扩展原字符串 s 的长度，
            计算公式为：新字符串长度 = 原字符串长度 + 2 * 空格个数 

            思路：
                1，首先遍历一次字符串s来统计有多少个空格
                2，假设有m个空格，我们需要填充的%20占用三个字符位置，所以需要额外开辟2*m个空间
                3，将开辟的空间链接到原字符串的后面，新的字符串命名为s_new，设置两个指针p1和p2
                    初始时p1指向原字符串s的末尾，p2指向s_new 的末尾
                4，p1指针向前移动，当p1指向的字符不是空格时，将p1指向的字符复制到p2指向的位置，都
                    向前移动一位
                5，当p1指向的字符是空格时，p1向前移动一格，这时应该插入%20，所以p2向前移动三个，并在
                    这三格中插入%20

            复杂度分析
                时间复杂度：O(n)
                空间复杂度：O(n+2m)
        '''
        s_len = len(s)
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1
        s_len += 2*space_count
        new_array = [' '] * s_len
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_array[j] = '%'
                new_array[j+1] = '2'
                new_array[j+2] = '0'
                j += 3
            else:
                new_array[j] = s[i]
                j += 1
        return ''.join(new_array)
