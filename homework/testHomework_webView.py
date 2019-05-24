#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/22 1:19 PM
# software: PyCharm

import sys
sys.path.append("/Users/hongwei/PycharmProjects/AppiumTest")
from config import config
from util.appiumUtil import appiumUtilClass
from util.appDriver import initAppDriver
from pageElement import jiaoyiPage
from appium import webdriver
import pytest
import time


class TestWebView(object):
    driver=webdriver
    @classmethod
    def setup_class(cls):
        print("启动app")
        initApp=initAppDriver(config.REMOTE_DRIVER_URL, config.CAPS)
        cls.driver=initApp.driver


    def setup_method(self):
        # self.driver.find_element_by_xpath("//*[@text='基金']").click()
        #等待交易按钮出现
        appiumUtilClass.wait_until(self.driver,"//*[@text='交易']")
        #点击交易
        __jiaoyi_btn=self.driver.find_element_by_xpath(jiaoyiPage._jiaoyi_xpath)
        # __jiaoyi_btn=self.driver.find_element_by_xpath("//*[@text='交易']")
        __jiaoyi_btn.click()
        #点击基金
        __fund_btn=self.driver.find_element_by_id(jiaoyiPage._fund_id)
        __fund_btn.click()
    def teardown_method(self):
        self.driver.back()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_switch_context(self):
        print(self.driver.contexts)
        print(self.driver.current_context)
        time.sleep(5)
        self.driver.switch_to.context(self.driver.contexts[-1])
        time.sleep(5)
        print(self.driver.current_context)
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        time.sleep(5)
        # dj_btn=self.driver.find_element_by_class_name("dj-button")
        dj_btn=self.driver.find_element_by_xpath("//*[@id='my-money']/div[2]/div[2]/button[2]")
        # dj_btn=self.driver.find_element_by_css_selector(".dj-button.blank")
        dj_btn.click()


    """
     交易 基金 基金开户 蛋卷已有账户登录 密码登陆 输入错误的用户名和密码，点击安全登陆
    """
    @pytest.mark.parametrize('phoneno,password',[('18612345001','123456'),('13812345001','001'),('helloworld','nihao')])
    def testWebView(self,phoneno,password):
        appiumUtilClass.wait_until(self.driver,"//*[@content-desc='已有蛋卷基金账户登录']")
        #点击已有蛋卷基金账户登录
        __danjuan_login=self.driver.find_element_by_accessibility_id(jiaoyiPage._danjuan_fund_login_accessibility_id)
        __danjuan_login.click()
        #点击使用密码登录
        __account_login=self.driver.find_element_by_accessibility_id(jiaoyiPage._account_login_accessibility_id)
        __account_login.click()
        #点击手机号输入框
        __phone_input=self.driver.find_element_by_id(jiaoyiPage._telno_id)
        __phone_input.click()
        __phone_input.send_keys(phoneno)
        #点击密码登录框
        __password_input=self.driver.find_element_by_id(jiaoyiPage._password_id)
        __password_input.click()
        __password_input.send_keys(password)
        #点击安全登录
        __login_btn=self.driver.find_element_by_id(jiaoyiPage._next_btn_id)
        __login_btn.click()
        #弹框错误处理
        self.driver.find_element_by_id("buttonPanel").click()
