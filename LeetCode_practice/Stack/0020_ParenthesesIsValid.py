# _*_coding:utf-8_*_
'''

题目： 20  有效的括号

    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。

    有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

示例 1:
    输入: "()"
    输出: true

示例 2:
    输入: "()[]{}"
    输出: true

示例 3:
    输入: "(]"
    输出: false

示例 4:
    输入: "([)]"
    输出: false

示例 5:
    输入: "{[]}"
    输出: true


思路：
    我们对给定的字符串 s 进行遍历，当我们遇到一个左括号时，我们会期望在后续的遍历
    中，有一个相同类型的右括号将其闭合。由于后遇到的左括号要先闭合，因此我们可以将
    这个左括号放入栈顶。
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        本体的思想与栈陷入后出的特点一致，即遇到左括号入栈，遇到右括号则将对应的左括号出栈。
        然后遍历完所有括号，栈让然为空
        :param s:
        :return:
        '''
        stack = Stack()
        dict_s = {'}': '{', ']': '[', ')': '('}
        for ch in s:
            if ch in {'(', '[', '{'}:
                stack.push(ch)
            else:
                if stack.is_empty():
                    return False
                elif stack.get_top() == dict_s[ch]:
                    stack.pop()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False

    def isValid1(self, s: str) -> bool:
        '''
            复杂度分析：
                时间复杂度为：O(n)  其中 n为字符串s的长度
                空间复杂度为：O(n+sigma)  哈希映射使用的空间为O(sigma)，相加即可得到总的空间复杂度
        '''
        stack = []
        mapping = {'}': '{', ']': '[', ')': '('}
        for char in s:
            if char in {'{', '[', '('}:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        if len(stack) is 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        pairs = {'}':'{', ']': '[', ')': '('}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack




