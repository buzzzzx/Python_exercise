# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/31 下午8:55'

"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

sensitive_words = 'filtered_words.txt'
text = input("> ")
len_t = len(text)


def replace_words():
    text_modify = text
    with open(sensitive_words, 'r', encoding='utf8') as p:
        sw = p.readlines()
    for word in sw:
        word = word.strip()
        len_w = len(word)
        if word in text:
            text_modify = text_modify.replace(word, "*"*len_w)

    print(text_modify)


if __name__ == '__main__':
    replace_words()
