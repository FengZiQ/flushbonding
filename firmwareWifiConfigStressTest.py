# coding=utf-8
from selenium import webdriver
import time
"""
1. wifi配网1万次压力测试脚本
2. wifi_config函数也可提供生成wifi配置码功能
"""

# 打开火狐浏览器
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()


def wifi_config(name, pwd, printer='USB'):
    # 打开网络配置页
    driver.get('http://dm.2dupay.com/wifi-config/wifiConfig.html')

    # 配置码信息
    driver.find_element_by_xpath('//option[@value="WIFI"]').click()
    driver.find_element_by_id('n').send_keys(name)
    driver.find_element_by_id('k').send_keys(pwd)
    driver.find_element_by_xpath('//option[@value="' + printer + '"]').click()

    # 点击“获取二维码”
    driver.find_element_by_id('btn').click()


def open_blank_picture():
    driver.get('file:///D:/script/flushbonding/blank.png')


if __name__ == "__main__":
    # 配置网络次数
    times = 5000
    count = 0

    # 开始测试
    while True:
        count += 1
        print('第' + str(count) + '次配网')

        # 生成wifi配置码，打开1s(如果一直打开，设备会一直配置)
        wifi_config('INSPIRY', 'Inspirymoin')
        time.sleep(1)
        open_blank_picture()

        # 配网成功后等待1min
        time.sleep(60)

        # 生成wifi配置码，打开1s(如果一直打开，设备会一直配置)
        wifi_config('weak', '12345678.')
        time.sleep(1)
        open_blank_picture()

        # 配网成功后等待1min
        time.sleep(60)

        # 达到测试次数后，结束程序
        if count == times:
            break
