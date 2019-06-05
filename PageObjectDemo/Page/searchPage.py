#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/29 9:41 AM
# software: PyCharm
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PageObjectDemo.Page.basePage import basePage
from PageObjectDemo.config import config

# 搜索页
_yaml_searchPage=config._yaml_searchPage

class searchPage(basePage):
    # 重构前
    # 输入搜索信息
    # def sendSearchKey(self, key):
    #     __input_text = self.find((By.XPATH, "//*[contains(@resource-id,'search_input_text')]"))
    #     __input_text.click()
    #     __input_text.send_keys(key)
    #     return self

    # 重构后
    # 输入搜索信息
    def sendSearchKey(self, text):
        self.load_steps(_yaml_searchPage, "sendSearchKey", text=text)
        return self

    # 点击综合
    def searchResult_goto_Comprehensive(self):
        # self.find_by_name('综合').click()
        self.load_steps(_yaml_searchPage, "searchResult_goto_Comprehensive")
        return self

    # 点击股票
    def searchResult_goto_stock(self):
        # self.find_by_name('股票').click()
        self.load_steps(_yaml_searchPage, "searchResult_goto_stock")
        return self

    # 点击组合
    def searchResult_goto_combination(self):
        # self.find_by_name('组合').click()
        self.load_steps(_yaml_searchPage, "searchResult_goto_combination")
        return self

    # 点击用户
    def searchResult_goto_user(self):
        # self.find_by_name('用户').click()
        self.load_steps(_yaml_searchPage, "searchResult_goto_user")
        return self

    # 股票添加关注
    def add_stockCode_to_fllowed(self, stockCode):
        # __flowBtn_locator = ((By.XPATH,
        #                      "//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]/../../..//*[contains(@resource-id,'follow_btn')]" % stockCode))
        # self.find(__flowBtn_locator).click()
        self.load_steps(_yaml_searchPage, "add_stockCode_to_fllowed",xpath_args=stockCode)
        return self

    # 股票移除关注
    def remove_stockCode_fllowed(self, code):
        # self.find((By.XPATH,
        #                        "//*[contains(@text,'%s') and contains(@resource-id,'stockCode')]/../../..//*[contains(@resource-id,'followed_btn')]" % code)).click()
        self.load_steps(_yaml_searchPage, "remove_stockCode_fllowed",xpath_args=code)
        return self

    # 判断是否已关注,默认检查股票页面，keytype=user时检查用户页面
    def stockCode_in_fllow(self, key, keytype='stock'):
        keytypeDict = {'stock': 'stockCode', 'user': 'user_name'}
        __flowBtn_locator = ((By.XPATH,
                             "//*[contains(@text,'%s') and contains(@resource-id,'%s')]/../../..//*[contains(@resource-id,'follow')]" % (
                             key, keytypeDict[keytype])))
        print(__flowBtn_locator, '*' * 20)
        __Id = self.find(__flowBtn_locator).get_attribute('resourceId')
        print(__Id)
        return "followed_btn" in __Id

    # 处理弹窗
    def click_popUps(self, key):
        # resource-id:md_buttonDefaultNegative
        try:
            self.find_by_name(key).click()
        except NoSuchElementException:
            print('未找到%s,无法点击,跳过弹窗处理动作！' % key)
        finally:
            return self

    # 取消按钮
    def cancle_click(self):
        from PageObjectDemo.Page.homePage import homePage
        self.find_by_name('取消').click()
        return homePage()

    # 用户添加关注
    def add_user_to_fllowed(self, userName):
        # __flowBtn_locator = ((By.XPATH,
        #                      "//*[contains(@resource-id,'user_name') and contains(@text,'%s')]/../..//*[contains(@resource-id,'follow_btn')]" % userName))
        # self.find(__flowBtn_locator).click()
        self.load_steps(_yaml_searchPage, "add_user_to_fllowed",xpath_args=userName)
        return self

    # 用户移除关注
    def remove_user_fllowed(self, userName):
        # self.find((By.XPATH,
        #                        "//*[contains(@text,'%s') and contains(@resource-id,'user_name')]/../../..//*[contains(@resource-id,'followed_btn')]" % userName)).click()
        self.load_steps(_yaml_searchPage, "remove_user_fllowed",xpath_args=userName)
        return self



