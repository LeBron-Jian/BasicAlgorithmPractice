# _*_coding:utf-8_*_
'''
461  汉明距离
题目：
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
给出两个整数 x 和 y ，计算他们之间的汉明距离
注意 ：0 <= x, y < 2**31

示例：
输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        汉明距离：汉明距离是使用在数据传输差错控制编码里面的
        汉明距离是一个概念，它表示两个（相同长度）字对应位不同的数量
        我们以d(x, y)表示两个字 x, y之间的汉明距离。对两个字符串进行异或运算
        并统计结果为1的个数，那么这个数字就是汉明距离
        在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数
        换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数
        例如：
            1011101 与 1001001 之间的汉明距离就是 2
            2143896 与 2233796 之间的汉明距离就是 3
            'toned' 与 ' roses' 之间的汉明距离是 3
        :param x:
        :param y:
        :return:
        '''
        pass


'''
python 如何将整数转换为二进制字符串
sol1 = bin(123).replace('0b', '')
print(sol1)
# 采用字符串的 format 方法来获取二进制
sol2 = '{0:b}'.format(123)
print(sol2)

'''


def HanmingDistance1(x, y):
    '''
    读过题目后，想法是来将两个整数先转换为二进制
    然后计算两个整数的二进制位不同位置的数目。

    :param x:
    :param y:
    :return:
    '''
    bin_x = bin(x).replace('0b', '')
    bin_y = bin(y).replace('0b', '')
    # 不能这样转换二进制
    res = int(bin_x) ^ int(bin_y)
    # count() 方法用于统计字符串里某个字符出现的次数，可选参数为在字符串搜索的开始与结束位置。
    # str.count(sub, start= 0,end=len(string))
    # bin() 返回一个整数int 或者 长整数 log int 的二进制表示
    return bin(x ^ y).count('1')


def HanmingDistance(x, y):
    '''
    这是LeetCode上的网友写的
    :param x:
    :param y:
    :return:
    '''
    num = 0
    res = []
    while x != 0 or y != 0:
        res.append((x % 2, y % 2))
        x //= 2
        y //= 2
    print(res)  # [(1, 0), (0, 0), (0, 1)]
    for xii, yii in res:
        if xii != yii:
            num += 1
    return num


res = HanmingDistance(x=1, y=4)
print(res)
