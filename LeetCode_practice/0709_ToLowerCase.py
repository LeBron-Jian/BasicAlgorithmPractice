# _*_coding:utf-8_*_
'''
709：转换成小写字母
实现函数 ToLowerCase()，该函数接受一个字符串参数 str，并将
该字符串中的大写字母转换为小写字母，之后返回新的字符串
示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"

'''


class Solution:
    def toLowerCase(self, str: str) -> str:
        pass


def toLowerCase1(s):
    new_s = []
    for i in range(len(s)):
        if s[i].islower() is True:
            new_s.append(s[i])
        else:
            new_s.append(s[i].swapcase())
    return "".join(new_s)


def toLowerCase2(s):
    # 内置函数应该不符合解题要求把。。。
    res = s.lower()
    return res


def toLowerCase3(s):
    # 记住这种方法不可取哈，，，，代码太复杂。。
    str = s.replace("A", "a").replace("B", "b").replace("C", "c").replace("D", "d").replace("E", "e").replace("F","f").replace(
        "G", "g").replace("H", "h").replace("I", "i").replace("J", "j").replace("K", "k").replace("L", "l").replace("M","m").replace(
        "N", "n").replace("O", "o").replace("P", "p").replace("Q", "q").replace("R", "r").replace("S", "s").replace("T","t").replace(
        "U", "u").replace("V", "v").replace("W", "w").replace("X", "x").replace("Y", "y").replace("Z", "z")
    return str


def toLowerCase(s):
    '''
    使用AICii码，其中A-Z对应Ascii是 65-90  a-z对应的Ascii是97-122
    chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）
        的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，
        或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，
        则会引发一个 TypeError 的异常。
    大小写字母相差32，只需要记住 ord()  chr()函数即可
    :param s:
    :return:
    '''
    s_list = []
    for i in s:
        if 65 <= ord(i) <= 90:
            s_list.append(chr(ord(i) + 32))
        else:
            s_list.append(i)
    return "".join(s_list)

res = toLowerCase('LOEOEOEOEO')
print(res)
print(chr('a'))
