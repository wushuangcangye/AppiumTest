#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:27 PM
# software: PyCharm
# import sys
# raise Exception ('%s-------****%s****,****%s****'%(sys.path,sys.version,sys.platform))
from appium.webdriver.webdriver import WebDriver


from PageObjectDemo.Page.basePage import basePage
from PageObjectDemo.Page.homePage import homePage

class App(basePage):
    driver:WebDriver
    #调用Android
    @classmethod
    def initApp(cls):
        cls.driver=cls.getClient().restart_App()
        return homePage()


