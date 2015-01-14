#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @author: huangwangping@youmi.net
# Created Time: 2015-01-13
"""
"""
import time


def dt_to_tstamp(dt):
    '''
    convert datetime to timestamp
    '''
    return time.mktime(dt.timetuple())
