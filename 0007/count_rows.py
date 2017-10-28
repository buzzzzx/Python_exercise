# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/27 下午5:21'

"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
"""

import os
import re

# directory and files
mycode = "mycode"
mycode_list = os.listdir(mycode)


def count_rows():
    code_rows = 0
    blank_rows = 0
    notation_rows = 0
    sum_code = 0
    sum_blank = 0
    sum_notation = 0
    for code in mycode_list:
        code_path = os.path.join(mycode, code)

        with open(code_path, 'r', encoding='utf8') as p:
            text = p.readlines()

        for line in text:
            if line.startswith("#"):
                notation_rows += 1
            elif line.startswith('"""'):
                notation_rows += 1
            elif re.match(r'^[\u4e00-\u9fa5]+', line):
                notation_rows += 1
            elif re.match(r'\n', line):
                blank_rows += 1
            else:
                code_rows += 1
        sum_code += code_rows
        sum_blank += blank_rows
        sum_notation += notation_rows
        show_result(code, notation_rows, blank_rows, code_rows)
        code_rows = 0
        blank_rows = 0
        notation_rows = 0
    show_result('all', sum_notation, sum_blank, sum_code)


def show_result(code, notation_rows, blank_rows, code_rows):
    print("{} file notation rows, blank rows, code rows: {}, {}, {}".format(code, notation_rows, blank_rows, code_rows))


if __name__ == '__main__':
    count_rows()
