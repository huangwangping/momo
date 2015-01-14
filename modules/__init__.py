#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @author: huangwangping@youmi.net
# Created Time: 2015-01-13
""" Instance """


class Instance(object):

    _instances = {}

    def __setattr__(self, key, value):
        self._instances[key] = value

    def __getattr__(self, key):
        return self._instances[key] if key in self._instances else None


# 用户存储后端
# backends = Instance()

# 数据库或者缓存
db = Instance()
