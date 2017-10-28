# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/23 上午10:12'

"""
题目0：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
用到的库：Pillow：Python Imaging Library
方法：PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
"""

from PIL import Image, ImageDraw, ImageFont

avatar = "weChat_avatar.png"
the_font = "arial.ttf"
color = (255, 0, 0)


def draw_text(number, color, the_font):
    img = Image.open(avatar)
    x, y = img.size
    print("The image's size is:")
    print(img.format, img.size, img.mode)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(the_font, 35)
    draw.text((x-20, 0), number, fill=color, font=font)
    img.show()
    img.save("new_avatar.png")


if __name__ == '__main__':
    number = str(7)
    draw_text(number, color, the_font)
