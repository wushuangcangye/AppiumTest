#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:48 PM
# software: PyCharm
from PageObjectDemo.Page.basePage import basePage
from selenium.webdriver.common.by import By


class choiceBySelfPage(basePage):

    # 点击股票tab
    def goto_stockPage(self):
        self.find_by_name('股票').click()
        return self

    #获取股票价格
    def get_price_by_name(self,name):
        price_locator="//*[contains(@text,'%s')]/../../..//*[contains(@resource-id,'portfolio_currentPrice')]"%name
        return self.find(By.XPATH,price_locator).text


    def goto_fundPage(self):
        self.find_by_name('基金').click()
        return self

    def goto_cubePage(self):
        self.find_by_name('组合').click()
        return self
