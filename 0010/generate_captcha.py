# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/31 上午10:52'

"""
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
"""

import string
import random
from PIL import ImageDraw, ImageFont, Image, ImageFilter

# font
font_path = 'font/arial.ttf'


def generate_captcha():
    codes = rand_string()
    generate_img(codes)


def rand_string():
    letters = string.ascii_letters
    digits = string.digits
    codes = ''
    for i in range(4):
        codes += random.choice(letters + str(digits))
    return codes


def generate_img(codes):
    x = 160
    y = 40
    img = Image.new('RGB', (x, y), (255, 255, 255))
    font = ImageFont.truetype(font_path, 32)
    draw = ImageDraw.Draw(img)

    # 随机颜色填充每个像素
    for i in range(x):
        for j in range(y):
            draw.point((i, j), fill=random_color(64, 255))

    # 随机颜色填充到每个验证码
    for m in range(4):
        draw.text((40 * m + 7, 5), codes[m], font=font, fill=random_color(32, 127))

    # 模糊滤镜
    image = img.filter(ImageFilter.BLUR)
    image.show()


def random_color(s=1, e=255):
    return (random.randint(s, e), random.randint(s, e), random.randint(s, e))


if __name__ == '__main__':
    generate_captcha()
