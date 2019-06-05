#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:48 PM
# software: PyCharm
from PageObjectDemo.Page.basePage import basePage
from selenium.webdriver.common.by import By
from PageObjectDemo.config import config

_yaml_choiceBySelfPage=config._yaml_choiceBySelfPage

class choiceBySelfPage(basePage):

    # 点击股票tab
    def goto_stockPage(self):
        self.load_steps(_yaml_choiceBySelfPage, 'goto_stockPage')
        return self

    # 获取股票价格
    def get_price_by_name(self, name):
        return self.load_steps(_yaml_choiceBySelfPage, 'get_price_by_name', xpath_args=name)
        # price_locator="//*[contains(@text,'%s')]/../../..//*[contains(@resource-id,'portfolio_currentPrice')]"%name
        # return self.find(By.XPATH,price_locator).text


    def goto_fundPage(self):
        self.load_steps(_yaml_choiceBySelfPage, 'goto_fundPage')
        return self

    def goto_cubePage(self):
        self.load_steps(_yaml_choiceBySelfPage, 'goto_cubePage')
        return self
