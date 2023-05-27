#_*_coding:utf-8_*_
'''
题目：
    剑指offer  68_1  二叉搜索树的最近公共祖先
    
    给定一个二叉搜索树，找到该树中两个指定节点的最近公共祖先
    最近公共祖先的定义为：对于有根树T的两个节点p，q，最近公共祖先
    表示为一个结点x，满足x是p,q的祖先且x的深度尽可能大（一个节点也
    可以是它自己的祖先）
    例如：给定如下二叉搜索树：root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
            6
          /   \
        2      8
      /  \\   /  \\
     0    4   7    9
        /  \\
       3    5
示例 1:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6 
    解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出: 2
    解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            注意题目给出的是一颗二叉搜索树，因此我们可以快速的找出树中某个节点以及从根节点到该节点的路径
            ，例如我们需要找到节点p：
                我们从根节点开始遍历
                如果当前节点就是p，那么成功的找到了节点
                如果当前节点的值大于p的值，说明p应该在当前节点的左子树，因此将当前节点移动到它的左子节点
                如果当前节点的值小于p的值，说明p应该在当前节点的右子树，因此将当前节点移动到它的右子节点
            同理可得，p节点
            当我们分别得到了从根节点到p和q的路径之后，我们就可以很方便的找到他们的最近公共祖先了，显然p和q
            的最近公共祖先就是从根节点到他们路径上的分叉点，也就是最后一个相同的节点。因此，如果我们设从根节点
            到p的路径为数组path_P，从根节点到q路径为数组path_q，那么只需要找到最大的编号i 
            满足path_q[i] = path_p[i]
            那么对应的节点就是分叉点，即p和q的最近公共祖先就是path_p[i]  或者path_q[i]
            复杂度分析：
                时间复杂度：O(n) 其中n是给定的二叉搜索树中的节点个数，在最坏的情况下，树呈链状，p和q一个
                    是树的唯一叶子节点，一个是孩子的父亲节点，此时时间复杂度为O(n)
                空间复杂度：O(n) 我们需要存储根节点到p和q的路径
    
        '''
        def getPath(root, target):
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path_p = getPath(root, p)
        path_q = getPath(root, q)
        ancestor = None
        for i, j in zip(path_p, path_q):
            if i == j:
                ancestor = i
            else:
                break
        return ancestor



class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            一次遍历
            对于上面方法，我们从根节点开始，通过遍历找出到达节点p和q的路径，一共需要遍历两次，我们也可以
            考虑将这两个节点放在一起遍历
            整体的遍历方法如下：
                我们从根节点开始遍历
                如果当前节点的值大于p和q的值，说明p和q应当在当前节点的左子树，因此将当前节点移动到它的左子节点
                如果当前节点的值小于p和q的值，说明p和q应该在当前节点的右子树，因此将当前节点移动到它的右子节点
                如果当前节点的值不满足上述条例，说明当前节点就是分叉点，此时p和q 要么在当前节点的不同子树，要
                要么就是其中一个就是当前节点
            可以发现，如果我们将这两个节点放在一起遍历，我们就是省去了存储路径需要的空间
        '''
        ancestor = root
        while True:
            if ancestor.val > q.val and ancestor.val > p.val:
                ancestor = ancestor.left
            elif ancestor.val < q.val and ancestor.val < p.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
  
  class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
          这个代码是实现二叉树的最近公共祖先，也可以满足二叉搜索树的最近公共祖先
        '''
        if not root  or root == p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
