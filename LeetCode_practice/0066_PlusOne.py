#_*_coding:utf-8_*_
'''
66 ：加一
题目：
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

'''
class Solution:
    def plusOne(self, digits):
        '''
        单个数字的非空数组，元素合成一个整数后，加1，输出新数组。
        如果将其单纯的理解为末尾加1，会有位数运算的烦恼，
        但是将数组整合后的整数看做一个整体，将其视为一个数字类型就好办了
        那我们手动实现进位就OK。
        遍历列表，将列表的第0,1,2，。。元素以。。。百，十，个位进行分别相加
        :param digits: : List[int]
        :return:  -> List[int]
        '''

        sums = 0
        for i in range(len(digits)):
            sums += 10**(len(digits)-1-i)*digits[i]
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

res = Solution()
print(res.plusone([5, 4, 3, 2]))

li = [1,2,3]
# print(len(li))  # 3
def test(li):
    sums = 0
    for i in range(len(li)):
        # print(i)
        sums += 10**(len(li)-i-1)*li[i]
        print(sums)
    sums_str = str(sums+1)
    print(sums_str)
    return [int(j) for j in sums_str]
s = test(li)
print(s)
