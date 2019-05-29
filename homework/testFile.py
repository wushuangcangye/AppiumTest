#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/22 3:50 PM
# software: PyCharm
import os
import chardet
import sys
import xlrd
#获取当前脚本执行的路径
# curRoutes=os.path.abspath(__file__)
# print(curRoutes)
# sr="你好啊"
print(sys.getdefaultencoding())
xlrd.open_workbook()
with open("testHomework2.py") as file:
    print(file.readlines())
