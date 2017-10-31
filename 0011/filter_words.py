# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/31 下午7:59'

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

sensitive_words_file = "filtered_words.txt"

print("请输入你想输入的话：")
user_words = input("> ")


def filter_words():
    out = "Human Rights"
    with open(sensitive_words_file, 'r', encoding="utf8") as p:
        sensitive_words = p.readlines()
    for sensitive_word in sensitive_words:
        if sensitive_word.strip("\n") in user_words:
            out = "Freedom"

    print(out)


if __name__ == '__main__':
    filter_words()
