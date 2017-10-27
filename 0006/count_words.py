# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/27 上午10:04'

"""
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
规定：出现次数最多的单词为最重要的词
"""

import os
import re
from collections import Counter

logs = 'mylog'

log_files = os.listdir(logs)


def count_word():
    for log in log_files:
        log_path = os.path.join(logs, log)
        with open(log_path, 'r') as p:
            text = p.read()

        words = re.split(r'[-,.;:\s\n]', text)
        words_correct = []

        for word in words:

            if re.match(r'[a-zA-Z]+', word):
                words_correct.append(word)
        find_word(log, words_correct)


def find_word(logname, words):
    c = Counter(words)

    words_sort = sorted(c.items(), key=lambda item: item[1], reverse=True)
    most_imp_word = words_sort[0][0]

    print("The most important word in '{}' is '{}'".format(logname, most_imp_word))


if __name__ == '__main__':
    count_word()
