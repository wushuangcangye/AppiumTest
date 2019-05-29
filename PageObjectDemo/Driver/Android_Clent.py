#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 12:04 PM
# software: PyCharm
from appium.webdriver.webdriver import WebDriver
from appium import webdriver

class AndroidDriver(object):
    driver:WebDriver
    # 初始化driver
    @classmethod
    def install_App(cls, REMOTE_DRIVER_URL, caps, IMPLICITLY_TIME=5) -> webdriver:
        cls.driver = webdriver.Remote(REMOTE_DRIVER_URL, caps)
        # 设置等待时间,默认5秒
        cls.driver.implicitly_wait(IMPLICITLY_TIME)
        return cls.driver

    # 重启应用
    @classmethod
    def restart_App(cls, REMOTE_DRIVER_URL, caps, IMPLICITLY_TIME=15) -> webdriver:
        cls.driver = webdriver.Remote(REMOTE_DRIVER_URL, caps)
        cls.driver.implicitly_wait(IMPLICITLY_TIME)
        return cls.driver

    # 用adb命令重启应用
    # # -W：等待启动完成    -S:关闭Activity所属的App进程后再启动Activity
    # __shell = "adb shell am start -W -S {package}/{activity}".format(package=config.CAPS['appPackage'],
    #                                                                  activity=config.CAPS['appActivity'])
    # subprocess.call(__shell, shell=True)
