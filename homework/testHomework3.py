#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/21 9:54 PM
# software: PyCharm

import os
import pytest
import sys
sys.path.append("/Users/hongwei/PycharmProjects/AppiumTest")
from config import config
from util.appDriver import initAppDriver
from util.appiumUtil import appiumUtilClass
from pageElement import loginPage
from appium.webdriver.webdriver import By


"""
    作业3
    完成雪球登录场景的测试
    要去带有setup_class setup_method体系
    微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
    作业上传到github，如果不会上传github，直接贴到回复里整个文件代码也可以。
    """
class TestHomework3:
    def setup_class(self):
        print("启动app")
        initApp=initAppDriver(config.REMOTE_DRIVER_URL, config.CAPS)
        self.driver=initApp.driver
        return self.driver

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self):
        #点击icon进入我的页面
        self.driver.find_element_by_id('user_profile_icon').click()
        #点击"点击登录"按钮进入登录页面
        self.driver.find_element_by_id("tv_login").click()

    def teardown_method(self):
        #回到首页
        self.driver.back()


    @pytest.mark.case1
    def test_homework3_click_wechat(self):
        #点击微信登录
        wechat_btn=self.driver.find_element_by_xpath(loginPage._wechat_btn_xpath)
        wechat_btn.click()
        #识别toast提示，未安装微信
        appiumUtilClass.wait_until(self.driver,"//*contains[@text='未安装微信']")


    @pytest.mark.case2
    def test_homework3_verify_code_login(self):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #手机号输入框
        phone_number_input=self.driver.find_element_by_id('register_phone_number')
        phone_number_input.click()
        phone_number_input.send_keys("18669162322")
        #发送验证码
        self.driver.find_element_by_id("register_code_text").click()
        #获取验证码
        os.system("adb shell dumpsys activity broadcasts  | grep senderName=|\
awk -F 'message=|senderName=|testerhome=' '{print $2}' | grep -oE '[0-9]{4,}'")
        #验证码输入框
        verify_code_input=self.driver.find_element_by_id("register_code")
        verify_code_input.click()
        verify_code_input.send_keys("8421")
        #点击登录
        self.driver.find_element_by_id("button_next").click()
        #断言验证码错误

    @pytest.mark.case3
    def test_homework3_no_password(self):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #点击邮箱手机号密码登录
        self.driver.find_element_by_id("tv_login_with_account").click()
        #账号输入框
        acconnt_input=self.driver.find_element_by_id("login_account")
        acconnt_input.click()
        acconnt_input.send_keys("noPassword")
        #密码输入框
        password_input=self.driver.find_element_by_id("login_password")
        #登录按钮
        self.driver.find_element_by_id("button_next")
        #断言toast提示，密码不能为空

    @pytest.mark.case4
    def test_homework3_no_loginName(self):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #点击邮箱手机号密码登录
        self.driver.find_element_by_id("tv_login_with_account").click()
        #账号输入框
        acconnt_input=self.driver.find_element_by_id("login_account")
        #密码输入框
        password_input=self.driver.find_element_by_id("login_password")
        password_input.click()
        password_input.send_keys("123456")
        #登录按钮
        self.driver.find_element_by_id("button_next")
        #断言toast提示,用户名不能为空

    @pytest.mark.case5
    def test_homework3_login(self):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #点击邮箱手机号密码登录
        self.driver.find_element_by_id("tv_login_with_account").click()
        #账号输入框
        acconnt_input=self.driver.find_element_by_id("login_account")
        acconnt_input.click()
        acconnt_input.send_keys("18669162322")
        #密码输入框
        password_input=self.driver.find_element_by_id("login_password")
        password_input.click()
        password_input.send_keys("123654")
        #登录按钮
        self.driver.find_element_by_id("button_next")
        #断言登录成功