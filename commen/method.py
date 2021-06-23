# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : method.py 
# @Software: PyCharm
# @Time : 2021/6/21 21:44
# @Author : 李建国
# @AuthorEmail : 1650408189@qq.com
import time


# 打开网页
def open_page(driver, url):
    driver.get(url)  # 打开网址
    driver.maximize_window()  # 浏览器窗口最大化


# 登录函数
def login_fun(driver, name, password):
    driver.find_element_by_id('username').send_keys('test123')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('btnSubmit').click()


# 搜索函数
def search_fun(driver, url, name, password, key):
    open_page(driver, url)
    login_fun(driver, name, password)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")  # 获取id属性
    id_frame = id + "-frame"  # 通过字符串的拼接，得到iframe-id
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))  # 通过元素定位切换
    driver.find_element_by_id('searchNumber').send_keys(key)  # 输入框输入数据
    driver.find_element_by_id('searchBtn').click()  # 点击查询按钮
    time.sleep(1)  # 隐式等待+强制等待
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num
