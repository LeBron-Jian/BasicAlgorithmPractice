#_*_coding:utf-8_*_
'''

    面试题01.05  一次编辑

    题目：字符串有三种编辑操作：插入一个字符，删除一个字符或者替换一个字符
    给定两个字符串，编写一个函数判定他们是否只需要一次（或者零次）编辑

示例 1:
    输入: 
        first = "pale"
        second = "ple"
    输出: True
 

示例 2:

    输入: 
        first = "pales"
        second = "pal"
    输出: False


'''

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        '''
            若长度差大于2，则至少需要两次改动才可以一致

            将顺序换位 first 短，second 长

            当发现不一致时，只有两种情况满足修改一次
                1，second 多一个，所以判断两种情况满足修改一次
                2，second 当下元素不一致，后面都相同，所以判断是否first[i+1:]==second[i+1:]
        '''
        if abs(len(first) - len(second)) > 1:
            return False

        if len(first) > len(second):
            first, second = second, first

        for i in range(len(first)):
            if first[i] == second[i]:
                continue
            return first[i:] == second[i+1:] or first[i+1:]==second[i+1:]
        return True
