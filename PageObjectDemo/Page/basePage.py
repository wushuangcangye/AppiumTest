#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:37 PM
# software: PyCharm
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjectDemo.Driver.Android_Clent import AndroidDriver


class basePage(object):
    # 初始化driver
    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls) -> WebDriver:
        from PageObjectDemo.Driver.Driver import App
        cls.driver = App.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidDriver

    # 封装一个find方法
    def find(self, *locator) -> WebElement:
        return self.driver.find_element(*locator)

    # 封装一个findText方法
    def find_by_name(self, name) -> WebElement:
        return self.find(By.XPATH, "//*[@text='%s']" % name)

    # 封装一个partialText方法
    def find_by_partialText(self, partialName) -> WebElement:
        return self.find(By.XPATH, "//*contains[@text='%s']" % partialName)

    # 封装获取屏幕大小方法
    def getWindoSize(self):
        return self.driver.get_window_size()

    # 封装左滑动作
    def move_action(self, turned: str):
        # 获取屏幕大小
        __size = self.getWindoSize()
        __height = __size["height"]
        __width = __size["width"]
        __actions = TouchAction(self.driver)
        if turned == 'left':
            __actions.press(x=int(__width * 0.9), y=int(__height * 0.5)).move_to(x=int(__width * 0.1), y=int(
                __height * 0.5)).release().perform()
        elif turned == 'right':
            __actions.press(x=int(__width * 0.1), y=int(__height * 0.5)).move_to(x=int(__width * 0.9), y=int(
                __height * 0.5)).release().perform()
        elif turned == 'up':
            __actions.press(y=int(__height * 0.8), x=int(__width * 0.3)).move_to(y=int(__height * 0.2), x=int(
                __width * 0.3)).release().perform()
        elif turned == 'down':
            __actions.press(y=int(__height * 0.2), x=int(__width * 0.3)).move_to(y=int(__height * 0.8), x=int(
                __width * 0.3)).release().perform()
        else:
            raise Exception('Please check your turned, turned only in（left,right,up,down）!')
        return self

    # 封装显示等待
    def wait_until(self, locator, limit=10):
        __wait = WebDriverWait(self.driver, limit)
        __wait.until(EC.presence_of_element_located(*locator))

    def closeDriver(self):
        self.driver.quit()
