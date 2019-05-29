#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 5:04 PM
# software: PyCharm
import allure
import pytest

from PageObjectDemo.Driver.Driver import App
import time


@allure.feature('测试用例')
class TestGetPrice:

    @classmethod
    def setup_class(cls):
        cls.homePage = App.initApp()

    # 跳转到自选页
    @allure.story('测试自选模块')
    @allure.title('获取股票价格')
    def test_goto_zixuan(self):
        with allure.step('启动app进入自选页面'):
            choiceBySelfPage = self.homePage.go_to_choiceBySelf()
        with allure.step('获取贵州茅台股票价格'):
            time.sleep(2)
        price = float(choiceBySelfPage.get_price_by_name('贵州茅台'))
        assert price > 869
        assert choiceBySelfPage.find_by_name("基金").text in '基金'

    @allure.story('测试搜索模块')
    @allure.story('股票搜索')
    @pytest.mark.parametrize('searchName,code', [
        ('alibaba', 'BABA'),
        ('贵州茅台', 'SH600519')
    ])
    def test_search_by_name(self, searchName, code):
        # ComprehensivePage 综合页
        ComprehensivePage = self.homePage.go_to_search().sendSearchKey(searchName).searchResult_goto_Comprehensive()
        time.sleep(1)
        # 如果已经关注，则移除
        # if ComprehensivePage.stockCode_in_fllow(code):
        ComprehensivePage.remove_stockCode_fllowed(code)
        # 点击关注
        ComprehensivePage.add_stockCode_to_fllowed(code)
        # 点击取消,页面归位
        ComprehensivePage.cancle_click()

    @classmethod
    def teardown_class(cls):
        cls.homePage.closeDriver()
