#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @author: huangwangping@youmi.net
# Created Time: 2015-01-13
"""
"""
import yaml
import redis
import torndb
import logging
import sys

from modules import db
import discount


if __name__ == '__main__':
    logging.basicConfig(filename='momo_discount.log',
                        level=logging.DEBUG)
    try:
        with open('etc/settings.yaml', 'r') as fp:
            config = yaml.load(fp)
    except yaml.YAMLError as e:
        logging.debug('error in configuration file: %s', e)
        sys.exit(0)
    pool = redis.ConnectionPool(host=config['redis']['host'],
                                port=config['redis']['port'],
                                db=config['redis']['db'])
    db.redis = redis.Redis(connection_pool=pool)

    db.mysql = torndb.Connection(**config['mysql'])

    res = discount.get_discount(1, 1, 1, 1, 1)
    print(res)

    res = discount.get_discount(2, 2, 2, 2, 2)
    print(res)

    res = discount.get_discount_by_gid(1)
    print(res)

    price = discount.get_price(1)
    print(price)

    price = discount.get_price(3)
    print(price)
