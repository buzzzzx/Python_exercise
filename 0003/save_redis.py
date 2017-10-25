# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/25 下午4:10'


"""
第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
用到了redis模块
将数据存为列表类型
"""

import redis

# connect to redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

file = "result.txt"

def save_redis(r, file):
    with open(file, 'r') as p :
        codes = p.readlines()
        for code in codes:
            r.rpush('discount_code', code)

    if len(r.lrange('discount_code', 0, -1)) == 200:
        print("保存成功！")


if __name__ == '__main__':
    save_redis(r, file)