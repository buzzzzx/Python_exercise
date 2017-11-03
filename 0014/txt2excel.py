# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/2 下午7:53'

"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
"
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
"
"""

import xlwt

file_stu = "student.txt"


def readText():
    with open(file_stu, 'r', encoding='utf8') as p:
        content = p.read()
        d = eval(content)
        return d


def txt2excel(text):
    # create workbook sheet
    workbook = xlwt.Workbook()
    sheet_stu = workbook.add_sheet("student")

    row = 0
    for k, v in text.items():
        col = 0
        sheet_stu.write(row, col, k)
        for val in v:
            col += 1
            sheet_stu.write(row, col, val)
        row += 1
    workbook.save("student.xls")
    print("写入EXCEL完毕!")


if __name__ == '__main__':
    text = readText()
    txt2excel(text)
