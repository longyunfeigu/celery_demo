#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from celery import task
import time

@task
def add(x, y):
    time.sleep(30)    #模拟长时间执行
    return x + y