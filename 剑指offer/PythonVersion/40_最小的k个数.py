#_*_coding:utf-8_*_
'''
题目：
    剑指offer 40 最小的k个数

    输入整数数组 arr，找出其中最小的 k 个数，例如，输入4,5,1,6,2,7,3,8 这八个数字
    则最小的4个数字是1,2,3,4

示例 1：
    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]

示例 2：
    输入：arr = [0,1,2,1], k = 1
    输出：[0]


堆的学习
    堆简单来说：一种特殊的完全二叉树结构
        大根堆：一种完全二叉树，满足任一节点都比其孩子节点大
        小根堆：一种完全二叉树，满足任一节点都比其孩子节点小

    堆排序——堆的向下调整性质
        假设根节点的左右子树都是堆，但根节点不满足堆的性质，可以通过一次向下
        的调整来将其变为一个堆。
    堆排序过程
        1，建立堆
        2，得到堆顶元素，为最大元素
        3，去掉堆顶，将堆最后一个元素放到堆顶，此时可以通过一次调整重新使堆有序
        4，堆顶元素为第二大元素
        5，重复步骤3，直到堆变为空

'''

class Solution:
    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        '''
            排序：对原数组从小到大排序取出前k个数即可。

            复杂度分析：
                时间复杂度：O(n logn) 其中是数组 arr的长度，算法的时间复杂度即排序的时间复杂度
                空间复杂度：O(log n) 排序所需要的额外空间复杂度为O(log n)
        '''
        res = sorted(arr, reverse=False)
        return res[:k]

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        '''
            堆
            我们用一个大根堆实时维护数组的前k小值，首先将前 k 个数插入大根堆中，随后
            从第 k+1 个数开始遍历，如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶
            的数弹出，再插入当前遍历到的数。最后将大根堆里的数存入数组返回即可。

            在Python中的对为小根堆，因此我们要对数组中所有数取反，才能使用小根堆维度前
            k小的值。

            复杂度分析：
            时间复杂度：O(n logk) 其中 n 是数组 arr 的长度，由于大根堆实时维度前 k 小值，
                    所以插入删除都是 O(logk)的时间复杂度，最坏情况下数组里 n 个数都会插入
                    所以一共需要 O(nlogk)的时间复杂度
            空间复杂度：O(k)，因为大根堆里最多 k 个数
        '''
        if k == 0:
            return []
        heapq.heapify(arr)
        res = [heapq.heappop(arr) for _ in range(len(arr))]
        return res[:k]

    def getLeastNumbers22(self, arr: List[int], k: int) -> List[int]:
        '''
            有两种生成堆的方式，这里展示第二种
        '''
        if k == 0:
            return list()
        hp = []
        for i in range(0, len(arr)):
            heapq.heappush(hp, arr[i])
        print('hp', hp)
        res = [heapq.heappop(hp) for _ in range(len(hp))]
        print('res', res)
        return res[:k]

    def getLeastNumbers23(self, arr: List[int], k: int) -> List[int]:
        '''
            官方代码
        '''
        if k == 0:
            return list()

        # 因为Python语言中的堆为小根堆，所以官方对其取相反数，才能使用小根堆维护前k小值
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heappop.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
