# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/25 下午4:57'

"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re

file = "English_passage.txt"


def calculate_word_amount(file):
    with open(file, 'r') as p:
        text = p.read()

    words = re.split(r'[,.!\s\n]', text)
    words_correct = []

    for word in words:
        if word != '':
            words_correct.append(word)

    print("该文本中的单词数量：" + str(len(words_correct)) + "个")


if __name__ == '__main__':
    calculate_word_amount(file)
