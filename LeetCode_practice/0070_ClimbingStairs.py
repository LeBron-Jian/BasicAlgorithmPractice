# _*_coding:utf-8_*_
'''
70 爬楼梯
题目：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        通过看网友的解法，我发现了一些规律
        那就是类似于斐波那契数列的了，
        因为从大佬列举的结果中发现规律：
        结果：    1,2,3,5,8,13,21
        下标：    1,2,3,4,5,6, 7
        所以：Xn+1 = Xn + Xn-1

        果然，高手在评论席
        :param n:
        :return:
        '''
        pass


def climbStairs1(n):
    '''
    斐波那契数列固然可以解决问题，但是我们下面这种是最常规的斐波那契数列
    也就是使用递归方法解决，但是递归会设计大量的重复计算
    所以需要改进。。。
    :param n:
    :return:
    '''
    f1, f2 = 1, 2
    while n > 1:
        f1, f2 = f2, f1 + f2
        n -= 1
    return f1


def climbStairs2(n):
    '''
    改进递归
    为了避免重复计算，因此每次跳台阶的方法数，要是我们记下来就可以了
    这样就不会重复计算了，用一个数组dp就可以解决
    dp[n] = dp[n-1] + dp[n-2]
    这样的时间复杂度为O(n)，空间复杂度为O(n)
    :param n:
    :return:
    '''
    if n <= 2:
        return n
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]


def climbStairs(n):
    '''
    实际上，我们还可以对上面方法进行改进
    就是不必将所有的记录都记起来，假设我们有三层楼梯
    也只需要知道跳2阶和1阶的方法数是多少就可以算出3阶了
    这样每次就只需要保留 n-1阶 和 n-2 阶的方法数
    :param n:
    :return:
    '''
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


res = climbStairs(5)
print(res)

'''
在这里不得不粘贴大佬的一个想法：在爬楼梯评论里就有：作者咖喱土豆
写的话是使用java写的：
当使用Java的话，因为返回值为int,他竟然找到了在 n=46的时候，结果溢出的问题。
所以，他直接一一列举了。。。。最后直接返回结果，并且算出来了，真实佩服

但确实是说得对，不要沉迷算法的精妙而忽视实际情况。。。
public int climbStairs(int n) {
    
    int result = 0;
    
    switch(n){
    case 1: result = 1; break;
    case 2: result = 2; break;
    case 3: result = 3; break;
    case 4: result = 5; break;
    case 5: result = 8; break;
    case 6: result = 13; break;
    case 7: result = 21; break;
    case 8: result = 34; break;
    case 9: result = 55; break;
    case 10: result = 89; break;
    case 11: result = 144; break;
    case 12: result = 233; break;
    case 13: result = 377; break;
    case 14: result = 610; break;
    case 15: result = 987; break;
    case 16: result = 1597; break;
    case 17: result = 2584; break;
    case 18: result = 4181; break;
    case 19: result = 6765; break;
    case 20: result = 10946; break;
    case 21: result = 17711; break;
    case 22: result = 28657; break;
    case 23: result = 46368; break;
    case 24: result = 75025; break;
    case 25: result = 121393; break;
    case 26: result = 196418; break;
    case 27: result = 317811; break;
    case 28: result = 514229; break;
    case 29: result = 832040; break;
    case 30: result = 1346269; break;
    case 31: result = 2178309; break;
    case 32: result = 3524578; break;
    case 33: result = 5702887; break;
    case 34: result = 9227465; break;
    case 35: result = 14930352; break;
    case 36: result = 24157817; break;
    case 37: result = 39088169; break;
    case 38: result = 63245986; break;
    case 39: result = 102334155; break;
    case 40: result = 165580141; break;
    case 41: result = 267914296; break;
    case 42: result = 433494437; break;
    case 43: result = 701408733; break;
    case 44: result = 1134903170; break;
    case 45: result = 1836311903; break;
    
    }
    return result;
}

'''
