#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/26 3:37 PM
# software: PyCharm
import os
import yaml
from appium.webdriver.common.mobileby import MobileBy
from Utils.logbookDemo import logger
from PageObjectDemo.config import config
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjectDemo.Driver.Android_Clent import AndroidDriver


class basePage(object):
    # 初始化driver
    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls) -> WebDriver:
        from PageObjectDemo.Driver.Driver import App
        cls.driver = App.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidDriver

    # 封装一个find方法
    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    # 封装一个findText方法
    def find_by_name(self, name) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % name))

    # 封装一个partialText方法
    def find_by_partialText(self, partialName) -> WebElement:
        return self.find((By.XPATH, "//*contains[@text='%s']" % partialName))

    # 封装获取屏幕大小方法
    def getWindoSize(self):
        return self.driver.get_window_size()

    # 封装滑动动作
    def move_action(self, turned: str):
        # 获取屏幕大小
        __size = self.getWindoSize()
        __height = __size["height"]
        __width = __size["width"]
        __actions = TouchAction(self.driver)
        if turned == 'left':
            __actions.press(x=int(__width * 0.9), y=int(__height * 0.5)).move_to(x=int(__width * 0.1), y=int(
                __height * 0.5)).release().perform()
        elif turned == 'right':
            __actions.press(x=int(__width * 0.1), y=int(__height * 0.5)).move_to(x=int(__width * 0.9), y=int(
                __height * 0.5)).release().perform()
        elif turned == 'up':
            __actions.press(y=int(__height * 0.8), x=int(__width * 0.3)).move_to(y=int(__height * 0.2), x=int(
                __width * 0.3)).release().perform()
        elif turned == 'down':
            __actions.press(y=int(__height * 0.2), x=int(__width * 0.3)).move_to(y=int(__height * 0.8), x=int(
                __width * 0.3)).release().perform()
        else:
            raise Exception('Please check your turned!')
        return self

    # 封装显示等待
    def wait_until(self, locator, limit=10):
        for i in range(3):
            try:
                __wait = WebDriverWait(self.driver, limit)
                __wait.until(EC.presence_of_element_located(*locator))
            except:
                self.wait_until(locator,limit=10)

    def closeDriver(self):
        self.driver.quit()

    # 封装yaml文件读取方法
    def load_steps(self, file_name, key, **kwargs):
        # file_path = config.YAML + file_name
        file_path = os.path.join(config.YAML, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            _po_data = yaml.load(file)
            _method = _po_data[key]

            for step in _method:
                # 指定_element类型
                _element: WebElement
                _locator:str=step['locator']
                # 定位方式
                logger.info(self.by_from_yaml(step.get('by')))
                _yamlBy = str(self.by_from_yaml(step.get('by'))).lower()
                # 判断定位方式 xpathName时调用封装的find_by_name方法
                if _yamlBy == 'xpathname':
                    _element = self.find_by_name(_locator)
                else:
                    #将locator中的%s替换为xpath_args=的值
                    _locator=self.replace_s(kwargs.get('xpath_args'),_locator)
                    _element = self.driver.find_element(by=_yamlBy, value=_locator)

                _action = str(step['action']).lower()

                #TODO:get_attribute
                if _action=="get_attribute":
                    self.do_action(_element,_action,attrkey=step['key'])
                else :
                    self.do_action(_element, _action,**kwargs)
                # todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待

                # if _action == 'click':
                #     _element.click()
                # elif _action == 'sendkeys':
                #     _text = str(step['text'])
                #     for key, value in kwargs.items():
                #         _text = _text.replace('$%s' % key, value)
                #     _element.send_keys(_text)
                # elif _action == 'get_text':
                #     return _element.text
                # #约定get_attribute中key关键字为attrkey
                # elif _action=='get_attribute':
                #     return _element.get_attribute(kwargs['attrkey'])
                # elif _action == 'left_move':
                #     self.move_action('left')
                # elif _action == 'right_move':
                #     self.move_action('right')
                # elif _action == 'up_move':
                #     self.move_action('up')
                # elif _action == 'down_move':
                #     self.move_action('down')
                # else:
                #     return "UnKnow Command %s" % step

    # 将文本中的%s替换为key
    def replace_s(self,rekey,content:str):
        if '%s' in content:
            # 将yaml中的%s替换为xpath_args
            return content.replace('%s', rekey)
        else:
            return content

    # 封装读取yaml中定位的方法
    def by_from_yaml(self, key):
        if key == 'id':
            by: By = By.ID
        elif key=='xpathName':
            by='xpathName'
        elif key == 'xpath':
            by: By = By.XPATH
        elif key == 'css':
            by: By = By.CSS_SELECTOR
        elif key == 'class':
            by: By = By.CLASS_NAME
        elif key == 'acc':
            by: MobileBy = MobileBy.ACCESSIBILITY_ID
        elif key == 'viewtag':
            by: MobileBy = MobileBy.ANDROID_VIEWTAG
        elif key == 'name':
            by: By = By.NAME
        elif key == 'text':
            by: By = By.LINK_TEXT
        elif key == 'partial':
            by: By = By.PARTIAL_LINK_TEXT
        return by

    # 封装读取yaml中的动作
    def do_action(self,element:WebElement,key:str,**kwargs):
        if key=='click':
            element.click()
        elif key=='clear':
            element.clear()
        elif key=='sendkeys':
            _text = str(kwargs['text'])
            #将yaml中的'$变量名'替换为对应的'value'
            for key, value in kwargs.items():
                _text = _text.replace('$%s' % key, value)
            element.send_keys(_text)
        elif key=='get_text':
            return element.text()
        # 约定get_attribute中key关键字为attrkey
        elif key == 'get_attribute':
            return element.get_attribute(kwargs['attrkey'])
        elif key == 'left_move':
            self.move_action('left')
            return self
        elif key == 'right_move':
            self.move_action('right')
            return self
        elif key == 'up_move':
            self.move_action('up')
            return self
        elif key == 'down_move':
            self.move_action('down')
            return self
        else:
            raise NameError('please check your key! key:click,get_text,get_attribute,left_move,right_move,up_move,down_move')


"""
    # 拼接yaml的方法,看不懂，暂时注释掉，参考地址：http://sanjiely.blogspot.com/2014/06/pythonyaml.html
    import yaml

    ## define custom tag handler for yaml
    def join(loader, node):
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])

    ## register the tag handler
    yaml.add_constructor('!join', join)
"""
