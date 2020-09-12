# _*_coding:utf-8_*_
'''
1233 删除子文件夹
题目：你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有子文件
并以任意顺序返回剩下的文件夹。
    我们这样定义子文件夹：
        如果文件夹 folder[i] 位于另一个文件夹 folder[j]下，那么folder[i] 就是 folder[j]的子文件夹
    文件夹的路径是由一个或多个按照以下格式串形成的字符串
        / 后跟一个或者多个小写英文字母
    例如 /leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。

示例 1：
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

示例 2：
输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。

示例 3：
输入：folder = ["/a/b/c","/a/b/d","/a/b/ca"]
输出：["/a/b/c","/a/b/ca","/a/b/d"]

提示：
1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] 只包含小写字母和 /
folder[i] 总是以字符 / 起始
每个文件夹名都是唯一的

'''

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        对 folder按照字典排序，如果目录 x 在folder中存在根目录，那么这个根目录必定
        在x之前
        1，将第一个目录作为根目录
        2，从第二个目录开始遍历，判断 folder[i] 是否以当前根目录为前缀
            是：folder[i] 是子目录，跳过该目录，不记录到结果中
            否：将当前根目录更新为 folder[i]
        :param folder:
        :return:
        '''
        pass


def removeSubfolders(folder):
    print(folder)
    folder.sort()  # 排序
    print(folder)
    res = [folder[0]]
    root = folder[0] + '/'  # 根目录 （将第一个目录设置为当前根目录
    for i in range(1, len(folder)):
        # 是否以 root为前缀
        if not folder[i].startswith(root):
            # 不是子目录
            root = folder[i] + '/'  # 更新根目录
            res.append(folder[i])
    return res


# folder = ["/a", "/a/b/c", "/a/b/d"]
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
res = removeSubfolders(folder)
print(res)
