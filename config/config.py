#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/21 2:59 PM
# software: PyCharm

import os

# 获取当前脚本执行的路径
curRoutes = os.path.abspath(__file__)
##以字典形式存储路径方便切割
__curRoutesList = curRoutes.split("/")
# 获取root路径
__rootList = __curRoutesList[:__curRoutesList.index('AppiumTest') + 1]
ROOT = "/".join(__rootList)
##获取报告存放路径
REPORT = os.path.join(ROOT, "report")

# caps配置参数
CAPS = {
    "deviceName": 'MyPhone',
    "platformName": 'android',
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    # 当前session下不重置应用,用于保留权限设置
    "noReset": True,
    # 使用Appium Unicode键盘输入内容
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutableDir": "/Users/hongwei/tmp/Driver"
}

# 初始化权限
# CAPS["autoGrantPermissions"] = True

REMOTE_DRIVER_URL = "http://127.0.0.1:4723/wd/hub"

IMPLICITLY_TIME = 15
