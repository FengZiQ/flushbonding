# coding=utf-8
from selenium import webdriver
from time import sleep
from to_log import to_log


class Configuration(object):

    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.get('http://www.tplogin.cn/')
            sleep(3)
            self.driver.find_element_by_id('lgPwd').send_keys('123456')
            sleep(3)
        except:
            to_log('请确认电脑是否连接了TPLINK的路由器！')

    # WiFi名字、密码
    def wc(self, name, pwd):
        try:
            # 点击”高级设置“
            self.driver.find_element_by_xpath('//ul[@id="headFunc"]/li[2]/label').click()
            sleep(3)
            # 点击“无线设置”
            self.driver.find_element_by_id('wifiSet_menu').click()
            sleep(3)
            # 填写wifi名称、密码
            self.driver.find_element_by_id('ssid').clear()
            self.driver.find_element_by_id('ssid').send_keys(name)
            self.driver.find_element_by_id('wlanPwd').clear()
            self.driver.find_element_by_id('wlanPwd').send_keys(pwd)
            # 保存
            self.driver.find_element_by_id('save').click()
            sleep(5)
            return True
        except:
            to_log('WiFi设置Failed')
            return False

    # 退出
    def finished(self):
        self.driver.quit()

