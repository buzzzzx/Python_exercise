# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/24 下午10:12'

"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random

code_num = 200  # 激活码的数量
code_len = 10   # 激活码的长度


def generate_code(code_num, code_len):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars)
    with open('result.txt', 'w') as p:
        for i in range(code_num):
            code = ""
            for j in range(code_len):
                code += chars[random.randint(0, length - 1)]
            if i == code_num - 1:
                p.write(code)
            else:
                p.write(code + '\n')


if __name__ == '__main__':
    generate_code(code_num, code_len)
