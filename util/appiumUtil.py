#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/13 9:41 AM
# software: PyCharm
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pytest

class appiumUtilClass():

    # 左右滑动方法封装
    @classmethod
    def moveLR_action(self, driver:webdriver, n=1, direction="left"):
        # 获取屏幕大小
        __size = driver.get_window_size()
        __height = __size.get("height")
        __width = __size.get("width")
        __actions = TouchAction(driver)
        if direction == "left":
            for i in range(n):
                __actions.press(x=int(__width * 0.9), y=int(__height * 0.5)). \
                    move_to(x=int(__width * 0.1), y=int(__height * 0.5)). \
                    release().perform()
                time.sleep(2)
        elif direction == "right":
            for i in range(n):
                __actions.press(y=int(__height * 0.5), x=int(__width * 0.1)). \
                    move_to(y=int(__height * 0.5), x=int(__width * 0.9)). \
                    release().perform()
                time.sleep(2)
        else:
            return "error!! direction only (left) or (right)"

    # 封装上滑方法,n表示滑动的次数
    @classmethod
    def moveUp_action(self, driver: webdriver, n):
        # 从屏幕中间下方20%处上滑直80%处
        __size = driver.get_window_size()
        __height = __size.get("height")
        __width = __size.get("width")
        __actions = TouchAction(driver)
        for i in range(n):
            __actions.press(y=int(__height * 0.8), x=int(__width * 0.3)).move_to(y=int(
                __height * 0.2), x=int(__width * 0.3)).release().perform()
            # driver.swipe(int(__width * 0.3), int(__height * 0.8), int(__width * 0.3),
            #              int(__height * 0.2), 1)
            time.sleep(2)
