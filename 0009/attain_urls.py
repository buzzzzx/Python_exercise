# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/30 下午10:46'

"""
第 0009 题：一个HTML文件，找出里面的链接。
"""

import requests
from lxml import etree

url = "http://blog.jobbole.com/112778/"
urls = {}


def attain_urls():
    r = requests.get(url)
    html_text = r.text

    sel = etree.HTML(html_text)
    infos = sel.xpath('//a[@href]')
    for info in infos:
        urls[info.text] = info.attrib['href']
    savetofile(urls, "urls.txt")


def savetofile(text, filename):
    with open(filename, 'w', encoding='utf8') as p:
        for key, value in text.items():
            p.write(str(key) + ": " + str(value) + "\n")


if __name__ == '__main__':
    attain_urls()
