# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/3 上午10:59'

"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

请将上述内容写到 numbers.xls 文件中，如下图所示：
"""

import xlwt

file_num = "numbers.txt"
xls = "numbers.xls"


def readText():
    with open(file_num, 'r', encoding='utf8') as p:
        text = p.read()
        l = eval(text)
        return l


def txt2excel(data):
    # create workbook sheet
    workbook = xlwt.Workbook()
    sheet_num = workbook.add_sheet("numbers")

    row = 0
    for d_row in data:
        col = 0
        for d in d_row:
            sheet_num.write(row, col, d)
            col += 1
        row += 1

    workbook.save(xls)


if __name__ == '__main__':
    l = readText()
    txt2excel(l)
