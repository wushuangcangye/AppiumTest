#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/21 9:05 PM
# software: PyCharm

import sys
sys.path.append("/Users/hongwei/PycharmProjects/AppiumTest")
from config import config
from util.appDriver import initAppDriver
from pageElement import homePage
from util.appiumUtil import appiumUtilClass



class TestHomework2(object):

    def setup_method(self):
        print("启动app")
        initApp=initAppDriver(config.REMOTE_DRIVER_URL, config.CAPS)
        self.driver=initApp.driver
        return self.driver

    def teardown_method(self):
        self.driver.quit()

    """
    作业2
    进入雪球首页，进入基金的新闻页（不是第一个基金按钮），对他以及它右侧的每个新闻栏目，执行上滑5次，进入下个栏目用从右边到左边滑动
    滑动使用相对坐标，而不是绝对坐标
    """
    def test_homework2(self):
        #点击基金
        fund_btn=self.driver.find_element_by_xpath(homePage._fund_xpath)
        fund_btn.click()

        #定位推荐栏
        navigation_tabs=self.driver.find_elements_by_xpath(homePage._navigation_tabs_xpath)

        # 判断基金右侧还有多少个元素
        over = None
        for index, value in enumerate(navigation_tabs):
            print(value.text)
            if value.text == "基金":
                over = len(navigation_tabs) - (index + 1)
                print("基金右侧还有%s个" % (over))
        #上滑5次
        appiumUtilClass.moveUp_action(self.driver,5)

        # 剩余元素右滑以及5次上滑
        for i in range(over):
            appiumUtilClass.moveLR_action(self.driver)
            appiumUtilClass.moveUp_action(self.driver, 5)