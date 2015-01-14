#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @author: huangwangping@youmi.net
# Created Time: 2015-01-13
"""
"""
import os
from os import path
os.chdir(path.dirname(path.abspath(__file__)))

import time
from msgpack import packb, unpackb

from modules import db
from modules.util import dt_to_tstamp
disc_prefix = 'discount_'
price_prefix = 'price_'
good_prefix = 'good_'


def query_discount(mid, major, minor, brand, sex):
    return db.mysql.get((r'SELECT `type`, `discount`, `price`, '
                         r'`start_time`, `end_time` '
                         r'FROM `momo`.`discount` '
                         r'WHERE `mall_id` = %s AND `major_type` = %s '
                         r'AND `minor_type` = %s AND `brand_id` = %s '
                         r'AND `sex` = %s LIMIT 1'),
                        mid, major, minor, brand, sex)


def query_good(gid):
    return db.mysql.get((r'SELECT * FROM `momo`.`goods` '
                        r'WHERE `gid` = %s LIMIT 1'), gid)


def get_discount(mid, major, minor, brand, sex):
    '''
    获取折扣信息
    return: tuple(isdisc, type, discount, price)
    type: int, Discount type: 1:discount, 2,price, other: no discount
    discount: int, discount, only if type=1
    price: int, price, only if type=2
    '''
    key = '%s_%d_%d_%d_%d_%d' % (disc_prefix, mid, major, minor, brand, sex)
    res = db.redis.get(key)
    if not res:
        res = query_discount(mid, major, minor, brand, sex)
        if res:
            # can't serialize decimal, datetime
            res['price'] = float(res['price'])
            res['start_time'] = dt_to_tstamp(res['start_time'])
            res['end_time'] = dt_to_tstamp(res['end_time'])

            db.redis.set(key, packb(res))
            db.redis.expire(key, 60 * 60)
        else:
            return (None, None, None)
    else:
        res = unpackb(res)

    now = time.time()
    if res['start_time'] >= now or now >= res['end_time']:
        return (None, None, None)

    return (res['type'], res['discount'], res['price'])


def get_discount_by_gid(gid):
    '''
    获取折扣信息
    gid: int good_id
    return: (type, discount, discprice)
    '''
    key = '%s_%d' % (good_prefix, gid)
    res = db.redis.get(key)
    if not res:
        res = query_good(gid)
        if res:
            res['price'] = float(res['price'])  # can't serialize decimal
            db.redis.set(key, packb(res))
            db.redis.expire(key, 60 * 60)
        else:
            return (None, None, None)
    else:
        res = unpackb(res)
    return get_discount(res['mall_id'], res['major_type'], res['minor_type'],
                        res['brand_id'], res['sex'])


def get_price(gid):
    '''获取商品价格
    gid: int, good id
    return: int, price
    '''
    key = '%s_%d' % (price_prefix, gid)
    price = db.redis.get(key)
    if not price:
        tp, disc, discprice = get_discount_by_gid(gid)
        gdinfo = unpackb(db.redis.get('%s_%d' % (good_prefix, gid)))
        if tp == 1:
            price = gdinfo['price'] * disc / 100
        elif tp == 2:
            price = discprice
        else:
            price = gdinfo['price']

        db.redis.set(key, price)
        db.redis.expire(key, 60 * 60)
    return price


def delete_price(gid):
    '''更新goods表时的关联函数,后台使用
    使价格缓存无效
    '''
    key = '%s_%d' % (price_prefix, gid)
    db.redis.delete(key)


def delete_discount(mid, major, minor, brand, sex):
    ''' 更新discount表时关联函数,后台使用
        使折扣缓存无效
        mid: mall_id
        major: major_type
        minor: minor_type
        brand: brand_id
        sex : sex
    '''
    key = '%s_%d_%d_%d_%d_%d' % (disc_prefix, mid, major, minor, brand, sex)
    db.redis.delete(key)
