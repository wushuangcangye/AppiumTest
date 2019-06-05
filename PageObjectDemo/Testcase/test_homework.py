#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/31 2:41 PM
# software: PyCharm
import allure

from PageObjectDemo.Driver.Driver import App


@allure.feature('测试用例')
class TestHomework:
    @classmethod
    def setup_class(cls):
        cls.homePage = App.initApp()

    """
    作业1
    点击雪球行情，获得“深证成指”的指数，判断是否大于8000点
    """
    @allure.story('测试行情模块')
    @allure.title('测试深证成指是否大于800')
    def test_homework1(self):
        HZCZ_price=self.homePage.go_to_price().goToHS().get_HZCZ_price()
        assert HZCZ_price > 8000

    @allure.story('测试搜索模块')
    @allure.title('测试用户关注')
    #TODO：添加测试数据
    def test_homework2(self,userName):
        self.homePage.go_to_search().sendSearchKey(userName).searchResult_goto_user().add_user_to_fllowed(userName)



    @classmethod
    def teardown_class(cls):
        cls.homePage.closeDriver()
