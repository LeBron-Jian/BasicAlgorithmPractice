#_*_coding:utf-8_*_
'''

    190  颠倒二进制位

    题目：颠倒给定的32位无符号整数的二进制位


提示：
    请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被
    指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其
    内部的二进制表示形式都是相同的。
    在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，
    输入表示有符号整数 -3，输出表示有符号整数 -1073741825。
   
进阶:
    如果多次调用这个函数，你将如何优化你的算法？  

示例1：
    输入: 00000010100101000001111010011100
    输出: 00111001011110000010100101000000
    解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
         因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。

示例2：
    输入：11111111111111111111111111111101
    输出：10111111111111111111111111111111
    解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
         因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。

提示：
    输入是一个长度为32的二进制字符串


注意：问题的难点在于，在10进制中，不会出现前缀零的问题，如果对于32位二进制来说，如果我们
还是按照十进制的处理而不加更多的改动，肯定有可能会出现漏掉之前的零。

'''
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
            这个题是给定一个 32 位的无符号整型，让我们按位翻转，第一位变最后一位。
            第二位变倒数第二位。。。。

            思路：
                1，n从高位开始逐步左移，res从低位开始逐步右移
                2，逐步判断，如果该位是1，则res+1，如果该位是0，则res+0
                3，32位全部遍历完，则遍历结束

            性能提升：
                可以用任何数字和1进行位运算的结果都取决于该数字最后一位的特性简化和提高性能
                比如：
                    n&1==1 说明n的最后一位是1
                    n&1==0 说明n的最后一位是0

            每次都使用 n 的最低一位，使用 n 的最低一位去更新答案的最低一位，使用完将 n 进行
            右移一位，将答案左移一位。

            复杂度分析：
                时间复杂度：O(1)
                空间复杂度：O(1)

            简单来说，每次把res左移，把n的二进制末尾数字，拼接到结果 res的末尾，然后把n右移
        '''
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res

print(Solution().reverseBits(n=11110100))