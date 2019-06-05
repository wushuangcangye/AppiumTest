#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/27 10:05 AM
# software: PyCharm
from selenium.webdriver.common.by import By

from PageObjectDemo.Page.basePage import basePage
from PageObjectDemo.config import config

_yaml_pricePage=config._yaml_pricePage

class pricePage(basePage):
    #点击沪深
    def goToHS(self):
        # self.find_by_name('沪深').click()
        self.load_steps(_yaml_pricePage,'goToHS')
        return self

    #深证成指
    def get_HZCZ_price(self,attrkey='text') -> float:
        #TODO: 增加action get_attribute
        return float(self.find(
            (By.XPATH, "//*[contains(@text,'深证成指')]/../ *[contains(@resource-id, 'index_price')]")).get_attribute(
            attrkey))
