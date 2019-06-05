#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:hongwei
# datetime:2019/5/24 1:50 PM
# software: PyCharm

import os
import sys
import subprocess
from Utils import logbookDemo
# import logging
import pytest

from PageObjectDemo.config import config

# logging.basicConfig(level=logging.INFO,
#                     format='[%(levelname)s %(asctime)s %(filename)s %(funcName)s line:%(lineno)d]: %(message)s',
#                     datefmt='%y%m%d %H:%M:%S')
log=logbookDemo.init_logger()

if __name__=='__main__':
    testcase_path=os.path.join(config.ROOT, "PageObjectDemo/Testcase")
    # testcase = sys.argv[1]
    testcase=testcase_path+'/test_get_price.py'
    log.info(testcase)
    xml_report_path = os.path.join(config.REPORT, 'xml')
    html_report_path = os.path.join(config.REPORT, 'html')
    pytest.main(['-s', '--alluredir', xml_report_path, testcase])
    cmd = 'allure generate --clean {xml} -o {html}'.format(xml=xml_report_path, html=html_report_path)
    log.info(cmd)
    subprocess.call(cmd, shell=True)
