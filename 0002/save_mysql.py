# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/25 上午10:08'

"""
**第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。
"""

import pymysql

# connect to mysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='batman123',
    db='discount_code',
)

file = "result.txt"

cur = conn.cursor()


def save_mysql(file):
    with open(file, 'r') as p:
        codes = p.readlines()
        for discount_code in codes:
            cur.execute("insert into code(code) values ('%s')" % (discount_code))

        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    save_mysql(file)
