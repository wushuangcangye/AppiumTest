#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:16 PM
# software: PyCharm
from appium.webdriver.common.mobileby import MobileBy

from PageObjectDemo.Page.basePage import basePage
from PageObjectDemo.Page.choiceBySelfPage import choiceBySelfPage
from PageObjectDemo.Page.dynamicsPage import dynamicsPage
from PageObjectDemo.Page.pricePage import pricePage
from PageObjectDemo.Page.searchPage import searchPage
from PageObjectDemo.Page.tradePage import tradePage
from PageObjectDemo.config import config
_yaml_homePage=config._yaml_homePage

class homePage(basePage):
    #进入自选页
    def go_to_choiceBySelf(self):
        # self.find_by_name('自选')
        # self.find_by_name('自选').click()
        self.load_steps(_yaml_homePage,'go_to_choiceBySelf')
        return choiceBySelfPage()

    #进入动态页
    def go_to_dynamics(self):
        # self.find_by_name('动态')
        # self.find_by_name('动态').click()
        self.load_steps(_yaml_homePage, 'go_to_dynamics')
        return dynamicsPage()

    #进入行情页
    def go_to_price(self):
        # self.find_by_name('行情')
        # self.find_by_name('行情').click()
        self.load_steps(_yaml_homePage, 'go_to_price')
        return pricePage()


    #进入交易页
    def go_to_trade(self):
        # self.find_by_name('交易')
        # self.find_by_name('交易').click()
        self.load_steps(_yaml_homePage, 'go_to_trade')
        return tradePage()

    #进入搜索页
    def go_to_search(self):
        # self.find((MobileBy.ID,'home_search')).click()
        self.load_steps(_yaml_homePage, 'go_to_search')
        return searchPage()