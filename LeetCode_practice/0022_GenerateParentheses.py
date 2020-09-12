# _*_coding:utf-8_*_
'''
22 括号生成
题目：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

输入：n = 2
输出：[
    ' (())',
    ' ()()'
    ]
'''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        有点难。。。。可能是自己太菜了。
        参考地址：https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
        官方解答：这一类问题是在一颗隐式的树上求解，可以用深度优先遍历，
        也可以用广度优先遍历。
        一般写深度优先遍历：代码好写，使用递归的方法，直接借助系统栈完成状态的转移
        广度优先遍历需要自己编写结点类和借助队列

        上面的状态是指程序执行到“隐式树”的某个节点的语言描述
        在程序中用不同的“变量”加以区分。

        深度优先遍历：这个方法称为“回溯” 也是可以的，
                    由于字符串的特殊性，产生一次拼接都生成新的对象，因此无需“回溯”
        广度优先遍历：创建结点对象，使用队列完成广度优先遍历
        动态规划：从一个最基本的问题触发，逐步记录每个阶段的解
        :param n:
        :return:
        '''
        pass


def generateParenthesis1(n):
    '''
    深度优先遍历
    思想：回溯+剪枝 ：可以生出左枝叶的条件是：左括号剩余数量（严格）小于0
    可以生出右枝叶的条件是：左括号剩余数量（严格）小于右括号剩余数量
    图例：蓝色结点为非叶子节点，表示在这里尝试节外生枝
          红结点为叶子节点，表示在这里剪枝
          绿色结点为叶子节点，表示此时结算，也表示递归终止

    画图以后，可以分析出结论：
    1，当前左右括号都有大于00个可以使用的时候，才产生分支
    2，产生左分支的时候，只看当前是否还有左括号可以使用
    3，产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在
        严格大于左边剩余的数量的时候，才可以产生分支
    4，在左边和右边剩余的括号树都等于 00 的时候解算。
    :param n:
    :return:
    '''
    res = []
    cur_str = ' '

    def dfs(cur_str, left, right):
        '''
        :param cur_str: 从根节点到叶子结点的路径字符串
        :param left: 左括号还可以使用的个数
        :param right: 右括号还可以使用的个数
        :return:
        '''
        if left == 0 and right == 0:
            res.append(cur_str)
            return
        if right < left:
            return
        if left > 0:
            dfs(cur_str + '(', left - 1, right)
        if right > 0:
            dfs(cur_str + ')', left, right - 1)

    dfs(cur_str, n, n)
    return res


def generateParenthesis11(n):
    '''
    使用加法的方式得到原始问题的一个解
    :param n:
    :return:
    '''
    res = []
    cur_str = ''

    def dfs(cur_str, left, right, n):
        '''

        :param cur_str: 从根节点到叶子节点的路径字符串
        :param left: 左括号已经使用的个数
        :param right: 右括号已经使用的个数
        :param n: 总有有几个括号
        :return:
        '''
        if left == n and right == n:
            res.append(cur_str)
            return
        if left < right:
            return
        if left < n:
            dfs(cur_str + '(', left + 1, right, n)
        if right < n:
            dfs(cur_str + ')', left, right + 1, n)
    dfs(cur_str, 0, 0, n)
    return res

def generateParenthesis2(n):
    '''
    广度优先遍历
    通过编写广度优先遍历的代码，可以体会一下，为什么搜索几乎都是用深度优先遍历（回溯算法）
    广度优先遍历，需要程序员自己写结点类，显示使用队列这个数据结构。深度优先遍历的时候，就可以
    直接使用系统栈，在递归方法执行完毕的时候，系统栈顶就把我们所需要的状态直接弹出，而无需
    编写结点类和显示使用栈。
    :param n:
    :return:
    '''
    # 我不会写。。。
    pass

def generateParenthesis3(n):
    '''
    动态规划
    第一步：定义状态 dp[i]：使用 i 对括号能够生成的组合
        注意：每一个状态都是列表的形式
    第二步：状态转移方差
        i 对括号的一个组合，在 i-1 对括号的基础上得到，这是思考“状态转移方程” 的基础
        i 对括号的一个组合，一定是以左括号开始，不一定是以右括号结尾，为此，我们可以枚举
            新的右括号可能所处的位置，得到所有的组合
        枚举的方式就是枚举左括号和右括号中间可能合法的括号对数，而剩下的合法的括号对数
            在于第一个左括号配对的右括号的后面，这就用到了以前的状态
    状态转移方程是：
        dp[i] = "(" + dp[可能的括号对数] + ")" +dp[剩下的括号对数]
        可能的对号对数与剩下的括号对数之和得为 i-1，故可能的括号对数 j 可以从 0开始，
            最多不能超过 i，即 i-1
        剩下的括号对数 +j=i+1，故剩下的括号对数=i-j-i
    整理得：
        dp[i] = "(" + dp[j] + ")" + dp[i- j - 1] , j = 0, 1, ..., i - 1
    第三步：思考初始状态和输出：
        初始状态：因为我们需要 0 对括号这种状态，因此状态数组 dp 从 0 开始，0个括号当然就是 ['']
        输出 dp[n]
    这个方法暂且就叫它动态规划，这么用也是很神奇的，它有以下两个特点：
        1，自底向上：从小规模为开始，逐渐得到大规模问题的解集
        2，无后效性：后面的结果的得到，不会影响到前面的结果
    :param n:
    :return:
    '''
    if n == 0:
        return []
    dp = [None for _ in range(n+1)]
    dp[0] = ['']
    for i in range(1, n+1):
        cur = []
        for j in range(i):
            left = dp[j]
            right = dp[i-j-1]
            for s1 in left:
                for s2 in right:
                    cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
    return dp[n]


res = generateParenthesis3(3)
print(res)
