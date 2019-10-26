#_*_coding:utf-8_*_
'''
1，给两个字符串s和t，判断 t是否为s的重新排列后组成的单词

　　s = 'anagram'   t='nagaram'  return true

　　s='rat', t='car',  return false
'''
# 下面这三种方法的时间复杂度非常高
def recombination(s,t):
    s = list(s)
    t = list(t)
    if len(s) == len(t):
        for i in s:
            if i in t:
                t.remove(i)
        if len(t) == 0:
            return True
        else:
            return False
    else:
        return False

def recombination1(s,t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    print(s)
    print(t)
    return s==t

def recombination2(s,t):
    return sorted(list(s)) == sorted(list(t))

def isAnagram(s, t):
    dict1 = []  #['a':1, 'b':2]
    dict2 = []
    for ch in s:
        if ch in dict1:
            dict1[ch] += 1
        else:
            dict1[ch] = 1

        # 一种更快的方法
        dict1[ch] = dict1.get(ch, 0) + 1

    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2
res = recombination1(s='rat', t='car')
print(res)