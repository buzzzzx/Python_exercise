# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/29 上午10:07'

"""
第 0008 题：一个HTML文件，找出里面的正文。
这里用的模块是网上别人做的提取正文的模块都封装好了，
可以提取本地的html文件的正文，也可以提取给出url的网页的正文，只是用到的方法不同而已，
这里我直接把html文件保存下来在本地提取
用到的模块GitHub地址：https://github.com/chrislinan/cx-extractor-python
"""

import os

from my_code.utils.CxExtractor import CxExtractor

# directory
htmls = "htmls"
contents = "contents"

html_files = os.listdir(htmls)


def extMainText():
    cx = CxExtractor()
    for html in html_files:
        html_path = os.path.join(htmls, html)
        myhtml = cx.readHtml(html_path, 'utf8')
        content = cx.filter_tags(myhtml)
        mainText = cx.getText(content)

        # get txt file name
        txt_name = os.path.splitext(html)[0] + '.txt'
        save(mainText, contents, txt_name)


def save(text, path, name):
    save_path = os.path.join(path, name)
    with open(save_path, 'w', encoding='utf8') as p:
        p.write(text)


if __name__ == '__main__':
    extMainText()
