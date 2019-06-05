#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 12:04 PM
# software: PyCharm
import os

from appium.webdriver.webdriver import WebDriver
from appium import webdriver
import yaml
from PageObjectDemo.config import config


class AndroidDriver(object):
    driver: WebDriver

    # 初始化driver
    @classmethod
    def install_App(cls) -> webdriver:
        return cls.initApp_from_yaml('install_App')

    # 重启应用
    @classmethod
    def restart_App(cls) -> webdriver:
        return cls.initApp_from_yaml('restart_App')

    # 从yaml中获取配置文件信息
    @classmethod
    def initApp_from_yaml(cls, fucName:str) -> webdriver:
        yaml_path=os.path.join(config.YAML,'driver.yaml')
        with open(yaml_path, 'r', encoding='utf-8') as file:
            cls.driver_data = yaml.load(file)
        # 获取REMOTE_DRIVER_URL
        _REMOTE_DRIVER_URL = cls.driver_data['BASE']['REMOTE_DRIVER_URL']
        # 获取隐式等待时长IMPLICITLY_TIME
        _IMPLICITLY_TIME = cls.driver_data['BASE']['IMPLICITLY_TIME']
        print(type (_IMPLICITLY_TIME))
        # 获取平台
        _PLATFORM = cls.driver_data['PLATFORM']
        _CAPS: str
        # 根据平台获取配置信息
        if _PLATFORM == 'android':
            # 获取caps
            _CAPS = cls.driver_data[fucName]['caps']['android']
        elif _PLATFORM == 'ios':
            # TODO:ios平台初始化配置
            pass
        elif _PLATFORM=='':
            #TODO:其他平台初始化配置
            pass

        # 初始化driver
        cls.driver = webdriver.Remote(_REMOTE_DRIVER_URL, _CAPS)
        cls.driver.implicitly_wait(_IMPLICITLY_TIME)
        return cls.driver

    # 用adb命令重启应用
    # # -W：等待启动完成    -S:关闭Activity所属的App进程后再启动Activity
    # __shell = "adb shell am start -W -S {package}/{activity}".format(package=config.CAPS['appPackage'],
    #                                                                  activity=config.CAPS['appActivity'])
    # subprocess.call(__shell, shell=True)
