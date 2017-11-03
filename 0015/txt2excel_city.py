# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/3 上午10:34'

"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
"
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
"
"""

import xlwt

file_city = "city.txt"

xls = 'city.xls'


def readText():
    with open(file_city, 'r', encoding='utf8') as p:
        text = p.read()
        d = eval(text)
        return d


def txt2excel(d):
    # create workbook sheet
    workbook = xlwt.Workbook()
    sheet_city = workbook.add_sheet('city')
    row = 0
    for k, v in d.items():
        col = 0
        sheet_city.write(row, col, k)
        sheet_city.write(row, col + 1, v)
        row += 1

    workbook.save(xls)
    print("写入EXCEL完毕!")


if __name__ == '__main__':
    d = readText()
    txt2excel(d)
