# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/1 上午10:29'

"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

参考代码: http://tieba.baidu.com/p/2166231880

Notation: 只是为了完成练习任务
"""

import requests
from lxml import etree
import os


class DownloadImage:
    def __init__(self):
        self.url = "http://tieba.baidu.com/p/2166231880"
        self.img_urls = []
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/59.0.3071.109 Safari/537.36'
        }
        self.img_dir = "imgs"

    def download(self):
        self.get_img_urls()
        self.save()

    def get_img_urls(self):
        rq = requests.get(self.url, headers=self.headers)
        html_text = rq.text
        sel = etree.HTML(html_text)
        datas = sel.xpath('//img[@class="BDE_Image"]')[:10]
        for data in datas:
            self.img_urls.append(data.attrib['src'])

    def save(self):
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)
        for img_url in self.img_urls:
            img_name = os.path.basename(img_url)
            img_path = os.path.join(self.img_dir, img_name)
            resp = requests.get(img_url)
            with open(img_path, 'wb') as p:
                p.write(resp.content)


if __name__ == '__main__':
    dl = DownloadImage()
    dl.download()
