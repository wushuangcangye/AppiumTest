#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/19 8:03 PM
# software: PyCharm
from appium import webdriver
import subprocess


class initAppDriver:
    # 初始化driver
    def __init__(self, REMOTE_DRIVER_URL, caps,IMPLICITLY_TIME=15) -> webdriver:
        self.driver = webdriver.Remote(REMOTE_DRIVER_URL, caps)
        # 设置等待时间,默认15秒
        self.driver.implicitly_wait(IMPLICITLY_TIME)

    # 重启应用
    def restart_App(self, REMOTE_DRIVER_URL, caps) -> webdriver:
        # # -W：等待启动完成    -S:关闭Activity所属的App进程后再启动Activity
        # __shell = "adb shell am start -W -S {package}/{activity}".format(package=config.CAPS['appPackage'],
        #                                                                  activity=config.CAPS['appActivity'])
        # subprocess.call(__shell, shell=True)
        self.driver: webdriver = webdriver.Remote(REMOTE_DRIVER_URL, caps, IMPLICITLY_TIME=15)
        self.driver.implicitly_wait(self.IMPLICITLY_TIME)
        return self.driver
