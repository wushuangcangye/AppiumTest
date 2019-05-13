#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/11 8:46 PM
# software: PyCharm

import sys

sys.path.append("/Users/hongwei/PycharmProjects/AppiumTest")

import pytest
from util.appiumUtil import appiumUtilClass
from appium import webdriver


class TestXueqiuLogin(object):
    driver = webdriver

    @classmethod
    def setup_class(cls):
        print("安装app")
        # 安装app
        # cls.driver=cls.install_app()
        # cls.driver.implicitly_wait(10)
        # cls.driver.quit()
        # print("安装完成退出")

    @classmethod
    def teardown_class(cls):
        print("调用退出方法")
        # cls.driver.quit()

    def setup_method(self):
        print("启动app")
        self.driver = TestXueqiuLogin.restart_app()
        return self.driver

    def teardown_method(self):
        self.driver.quit()

    """
    作业2
    进入雪球首页，进入基金的新闻页（不是第一个基金按钮），对他以及它右侧的每个新闻栏目，执行上滑5次，进入下个栏目用从右边到左边滑动
    滑动使用相对坐标，而不是绝对坐标
    """
    def test_homework2(self):
        # 定位推荐栏的所有元素
        navigation_tabs = self.driver.find_elements_by_xpath(
            '//*[contains(@resource-id,"indicator")]//*[contains(@class,"TextView")]')

        # 判断基金右侧还有多少个元素
        over = None
        for index, value in enumerate(navigation_tabs):
            print(value.text)
            if value.text == "基金":
                over = len(navigation_tabs) - (index + 1)
                print("基金右侧还有%s个" % (over))

        # 点击基金
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"indicator")]//*[contains(@text,"基金")]') \
            .click()
        appiumUtilClass.moveUp_action(self.driver, 5)

        self.driver.find_element_by_xpath("//*[contains(@text,'基金')]")
        # 剩余元素右滑以及5次上滑
        for i in range(over):
            appiumUtilClass.moveLR_action(self.driver)
            appiumUtilClass.moveUp_action(self.driver, 5)

    """
    作业3
    完成雪球登录场景的测试
    要去带有setup_class setup_method体系
    微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
    作业上传到github，如果不会上传github，直接贴到回复里整个文件代码也可以。
    """
    @pytest.fixture()
    def enter_loginPage(self):
        #点击icon进入我的页面
        self.driver.find_element_by_id('user_profile_icon').click()
        #点击"点击登录"按钮进入登录页面
        self.driver.find_element_by_id("tv_login").click()

    def test_homework3_click_wechat(self,enter_loginPage):
        #点击微信登录
        wechat_btn=self.driver.find_element_by_xpath("//*[contains(@text,'微信登录')]")
        wechat_btn.click()
        assert wechat_btn

    def test_homework3_verify_code_login(self,enter_loginPage):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #手机号输入框
        phone_number_input=self.driver.find_element_by_id('register_phone_number')
        phone_number_input.click()
        phone_number_input.send_keys("18669162322")
        ##发送验证码
        self.driver.find_element_by_id("register_code_text").click()
        #验证码输入框
        verify_code_input=self.driver.find_element_by_id("register_code")
        verify_code_input.click()
        verify_code_input.send_keys("8421")
        #点击登录
        self.driver.find_element_by_id("button_next").click()






    def test_homework3_no_password(self,enter_loginPage):
        #点击手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #点击邮箱手机号密码登录
        self.driver.find_element_by_id("tv_login_with_account").click()
        #账号输入框
        acconnt_input=self.driver.find_element_by_id("login_account")
        acconnt_input.click()
        acconnt_input.send_keys("helloWorld")
        #密码输入框
        password_input=self.driver.find_element_by_id("login_password")
        #登录按钮
        self.driver.find_element_by_id("button_next")

    def test_homework3_wrong_password(self,enter_loginPage):
        pass

    def test_homework3_wrong_username(self,enter_loginPage):
        pass

    @classmethod
    def install_app(cls) -> webdriver:
        print("调用安装方法")
        ##安装app
        caps = {}
        # caps['app']='/Users/hongwei/Downloads/xueqiu_wxdialog.apk'

        caps['appPackage'] = 'com.xueqiu.android'
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['deviceName'] = 'MyPhone'
        caps['platformName'] = 'android'
        caps["autoGrantPermissions"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver

    @classmethod
    def restart_app(cls) -> webdriver:
        print("调用启动方法")
        # 启动已安装app
        caps = {}
        caps['deviceName'] = 'MyPhone'
        caps['platformName'] = 'android'
        caps['appPackage'] = 'com.xueqiu.android'
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'testMain.py'])
