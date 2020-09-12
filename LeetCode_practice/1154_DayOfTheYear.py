# _*_coding:utf-8_*_
'''
1154 一年中的第几天
题目：
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。
每个月的天数与现行公元纪年法（格里高利历）一致。


示例 1：
输入：date = "2019-01-09"
输出：9

示例 2：
输入：date = "2019-02-10"
输出：41

示例 3：
输入：date = "2003-03-01"
输出：60

示例 4：
输入：date = "2004-03-01"
输出：61
 

提示：
date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。

'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        pass


import datetime, time


def dayOfYear1(date):
    '''
    题目都说当年了，所以只需要考虑月份和日期即可。
    特别注意2019年二月份是几天。，。
    平年2月28天,闰年2月29天.

    闰年的判断条件为：通常年份能被4整除且不能被100整除的为闰年
    普通的情况求闰年只需要除以4即可除尽  即年份除以4余数为0
    如果是100的倍数但不是400的倍数，那就不是闰年，即末两位都是零的整除400才行
    像 1700  1800 1900 2100都不是闰年
    但是2000 2400 是闰年

    总结一下：
        1， 能别4整数而不能被100整除
        2， 能被400整除
        （四年一闰，百年不闰，四百年一闰）
    :param date:
    :return:
    '''
    year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
    print(year, month, day)
    common_month_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = day
    print(res)
    for i in range(1, month):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # 表示闰年
            # 这里特别注意一下我们月份从 1 开始，但是列表从 0 开始
            res += leap_month_num[i-1]
        else:  # 表示平年
            res += common_month_num[i-1]
    return res

def dayOfYear(date):
    '''
    其实第一想法就是调用库。。。。没办法Python库真的太强大
    我就懒成直接想用datetime库。没救了
    :param date:
    :return:
    '''
    res = map(int, date.split('-'))  #打印为 [2003, 3, 1]
    # %j 	显示当年第几天
    res = datetime.date(*res).strftime('%j').lstrip('0')
    return res


res1 = dayOfYear('2019-01-09')  # 9
res2 = dayOfYear('2019-02-09')  # 40
res3 = dayOfYear('2004-03-01')  # 61
res4 = dayOfYear('2003-03-01')  # 60
print(res1, res2, res3, res4)
