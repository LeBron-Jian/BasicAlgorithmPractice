#_*_coding:utf-8_*_
'''
题目： 77 组合
  给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
  输入: n = 4, k = 2
  输出:
  [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
  ]
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        C(m,n)=C(m-1,n)+C(m-1,n-1)
        :param n:
        :param k:
        :return:
        '''
        if k>n or k ==0:
            return []
        if k==1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[i for i in range(1, n+1)]]
        answer = self.combine(n-1, k)
        for item in self.combine(n-1, k-1):
            item.append(n)
            answer.append(item)

        return answer


    def combine2(self, n: int, k: int) -> List[List[int]]:
      '''
        注意这里用了轮子，都是迭代器工具库里面itertools的东西
        其中 combinations(iterable, r) 返回的是可迭代对象所有的长度为 r 的子序列
        注意 combinations 与 permutations 不同，permutations 返回的是排列，
        而 combinations() 返回的是组合

        排列：就是排序，可重复
        组合：就是分配，不可重复
      '''
      from itertools import combinations
      return list(combinations(range(1, n+1), k))


    def combine3(self, n: int, k: int) -> List[List[int]]:
      '''
        这是一道比较经典的回溯题，首先建立 backtrace 函数，有两个参数，一个是从1开始一直
        加到n的整数，一个是暂存的列表。

        先用一个 if 语句判断回溯结果条件，就是列表的长度是否等于k，如果是的话就添加进 res 中，
        然后结束递归函数。

        如果列表长度小于 k 的话，就进入循环，将 j 增大 1，且暂存列表加入数字 j

        全部结束完输出结果 res 即可。

      '''
      res = []
      def backtrace(i, tmp):
        if len(tmp) == k:
          res.append(tmp)
          return

        for j in range(i, n+1):
          backtrace(j+1, tmp+[j])
        backtrace(1, [])
        return res
