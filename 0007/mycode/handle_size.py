# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/25 下午11:08'

"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

import os

from PIL import Image

iPhone_x, iPhone_y = (640, 1136)

# directory
old_images = 'old_images'
new_images = 'new_images'

file_list = os.listdir(old_images)


def handle_size():
    for img in file_list:
        img_path = os.path.join(old_images, img)
        old_img = Image.open(img_path)
        x, y = old_img.size
        if x > iPhone_x:
            x = 640
        if y > iPhone_y:
            y = 1136

        new_img = old_img.resize((x, y), Image.ANTIALIAS)

        if not os.path.exists(new_images):
            os.makedirs(new_images)

        save_img(img, new_img)

        calculate_size(img, old_img, new_img)


def calculate_size(imgname, old, new):

    print("The old " + imgname + "'s size is: " + str(old.size))
    print("The new " + imgname + "'s size is: " + str(new.size))


def save_img(imgname, new_img, dirname=new_images):
    new_img.save(os.path.join(dirname, imgname))


if __name__ == '__main__':
    handle_size()
