#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/21 2:59 PM
# software: PyCharm

import os

# 获取当前脚本执行的路径
__CURROUTES = os.path.abspath(__file__)
##以字典形式存储路径方便切割
__CULROUTESLIST = __CURROUTES.split("/")
# 获取root路径
PROJECT_NAME = "AppiumTest"
__ROOTLIST = __CULROUTESLIST[:__CULROUTESLIST.index(PROJECT_NAME) + 1]
ROOT = "/".join(__ROOTLIST)
# 获取报告存放路径
REPORT = os.path.join(ROOT, "report")
# 获取yaml文件存在路径
YAML: str = str(os.path.join(ROOT, "data"))
# 日志存放路径
LOG_DIR = os.path.join(ROOT,"Log")

# webview所需driver路径
__CHROME_DRIVER_PATH = os.path.join(ROOT, "PageObjectDemo/Driver")

# # caps配置参数
# __DEVICE_NAME = 'MyPhone'
# __PLATFORM = 'android'
# __PACKAGE_NAME = "com.xueqiu.android"
# __ACTIVITY = ".view.WelcomeActivityAlias"

# 指定运行设备
# udid=""


# CAPS = {
#     "deviceName": __DEVICE_NAME,
#     "platformName": __PLATFORM,
#     "appPackage": __PACKAGE_NAME,
#     "appActivity": __ACTIVITY,
#     # 当前session下不重置应用,用于保留权限设置
#     "noReset": True,
#     # 使用Appium Unicode键盘输入内容
#     "unicodeKeyboard": True,
#     # 应用结束后
#     "resetKeyboard": True,
#     "automationName": "UiAutomator2"
#     # webviewdriver所在路径文件夹
#     # "chromedriverExecutableDir": __CHROME_DRIVER_PATH
# }

# 初始化权限
# CAPS["autoGrantPermissions"] = True

# REMOTE_DRIVER_URL = "http://127.0.0.1:4723/wd/hub"
#
# __IMPLICITLY_TIME = 15

# yaml文件对应关系
_yaml_searchPage = 'searchPage.yaml'
_yaml_choiceBySelfPage = 'choiceBySelfPage.yaml'
_yaml_dynamicsPage = 'dynamicsPage.yaml'
_yaml_homePage = 'homePage.yaml'
_yaml_pricePage = 'pricePage.yaml'
_yaml_tradePage = 'tradePage.yaml'
