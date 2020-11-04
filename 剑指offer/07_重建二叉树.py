    #_*_coding:utf-8_*_
'''
题目：
    剑指offer 7  重建二叉树

    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历
    的结果中都不包含重复的数字



例如给出：
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]

返回如下二叉树：

        3
       / \
      9  20
        /  \
       15   7

限制：
    0 <= 节点个数 <= 5000

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
            前序遍历：遍历顺序：父节点  左子节点  右子节点
            中序遍历：遍历顺序：左子节点  父节点  右子节点

            注意：前序遍历中的第一个元素一定是树的根，这个根又将中序序列分为左右两颗树
            现在我们只需要将前序遍历的数组中删除根元素，然后重复上面过程处理左右两颗子树

                所以这个题的本质问题就是：
                1，找到各个子树的根节点 root
                2，构建该根节点的左子树
                3，构建该根节点的右子树

            递归方法的基准情形有两个：判断前序遍历的下标范围的开始和结束，
                若开始大于结束，则当前的二叉树 中没有结点，返回空值null，若开始等于结束，
                则当前的二叉树恰好有一个节点，根据节点值创建该节点作为根节点并返回

                若开始小于结束，则当前的二叉树中有多个结点，在中序遍历中找到根节点的位置，从而
                得到左子树和右子树各自的下标范围和节点数量，知道节点数量后，在前序遍历中可得到
                左子树和右子树各自的下标范围，然后递归重建左子树和右子树，并将左右子树的根节点分别
                作为当前节点的左右子节点
        '''
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        rootNode = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置 
        mid = inorder.index(preorder[0])
        rootNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        rootNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return rootNode


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBilidTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            # 前序遍历中第一个节点就是跟节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构建左子树，并连接到根节点
            # 先序遍历中 从左边界 +1 开始的 size_left_subtree 个元素就对应了中序遍历中 从左边界开始到根节点定位 -1 的元素
            root.left = myBilidTree(preorder_left+1, preorder_left+size_left_subtree, inorder_left, inorder_root-1)
            # 递归的构造右子树，并连接到根节点
            # 先序遍历中，从左边界+1+左子树节点数目开始到右边界的额元素就对应了中序遍历中 从根节点定位+1到 右边界的元素
            root.right = myBilidTree(preorder_left+size_left_subtree+1, preorder_right, inorder_left+1, inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element:i for i, element in enumerate(inorder)}
        return myBuildTree(0, n-1, n-1)

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
            迭代：
            对于前序遍历中的任意两个连续节点u和v，根据前序遍历的流程，我们可以知道U和v只有两种
            可能的关系：
                v是u的左儿子，这里因为在遍历到U之后，下一个遍历的节点就是u的左儿子，即v

                u 没有左儿子的话，并且 v 是 u 的某个祖先节点（或者u本身）的右儿子，如果 u 没有左儿子
                那么下一个遍历的节点就是 u 的右儿子。如果 u 没有右儿子，我们就往上回溯，直到遇到第一个
                有右儿子（且 u 不在它的右儿子的子树中）的节点 u_a，那么 v 就是 u_a 的右儿子
        '''
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root
