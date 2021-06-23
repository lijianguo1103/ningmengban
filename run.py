# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : run.py 
# @Software: PyCharm
# @Time : 2021/6/21 21:56
# @Author : 李建国
# @AuthorEmail : 1650408189@qq.com

from commen import method
from testdata import data
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 取数据---字典取值
url = data.data_test.get("url")
name = data.data_test.get("name")
password = data.data_test.get("password")
key = data.data_test.get("key")

result = method.search_fun(driver=driver, url=url, name=name, password=password, key=key)  # 调用函数，取值
if key in result:
    print("搜索成功")
