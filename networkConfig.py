# coding=utf-8
from selenium import webdriver
from time import sleep
from to_log import to_log


# wifi配置
def wifi_mode(name, pwd, ss_id=False, pr='', **dh: 'key: dh,ip,mask,gw,dns'):
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('http://dm.2dupay.com/wifi-config/wifiConfig.html')
        sleep(3)
        driver.find_element_by_id('net').click()
        sleep(1)
        driver.find_element_by_xpath('//option[@value="WIFI"]').click()
        sleep(1)
        driver.find_element_by_id('n').send_keys(name)
        driver.find_element_by_id('k').send_keys(pwd)
        if ss_id:
            driver.find_element_by_xpath('//div[@id="s"]/div/div/span[2]').click()
        driver.find_element_by_id('pr').click()
        sleep(1)
        if pr:
            driver.find_element_by_xpath('//option[@value="USB"]').click()
        else:
            driver.find_element_by_xpath('//option[@value="无"]').click()
        driver.find_element_by_id('br1').click()
        sleep(1)
        if dh.get('dh', ''):
            driver.find_element_by_xpath('//option[@value="自动"]').click()
        else:
            driver.find_element_by_xpath('//option[@value="手动"]').click()
            driver.find_element_by_id('ip').send_keys(dh.get('ip', ''))
            driver.find_element_by_id('mask').send_keys(dh.get('mask', ''))
            driver.find_element_by_id('gw').send_keys(dh.get('gw', ''))
            driver.find_element_by_id('dns').send_keys(dh.get('dns', ''))
        driver.find_element_by_id('btn').click()
        sleep(5)
        driver.close()
    except:
        to_log('网络配置码生成失败！')


# LAN配置
def lan_mode(pr='', **dh: 'key: dh(DHCP),ip,mask,gw,dns'):
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('http://dm.2dupay.com/wifi-config/wifiConfig.html')
        sleep(3)
        driver.find_element_by_id('net').click()
        sleep(1)
        driver.find_element_by_xpath('//option[@value="LAN"]').click()
        sleep(1)
        driver.find_element_by_id('pr').click()
        sleep(1)
        if pr:
            driver.find_element_by_xpath('//option[@value="USB"]').click()
        else:
            driver.find_element_by_xpath('//option[@value="无"]').click()
        driver.find_element_by_id('br1').click()
        sleep(1)
        if dh.get('dh', ''):
            driver.find_element_by_xpath('//option[@value="自动"]').click()
            sleep(1)
        else:
            driver.find_element_by_xpath('//option[@value="手动"]').click()
            sleep(1)
            driver.find_element_by_id('ip').send_keys(dh.get('ip', ''))
            driver.find_element_by_id('mask').send_keys(dh.get('mask', ''))
            driver.find_element_by_id('gw').send_keys(dh.get('gw', ''))
            driver.find_element_by_id('dns').send_keys(dh.get('dns', ''))
            sleep(1)
        driver.find_element_by_id('btn').click()
        sleep(5)
        driver.close()
    except:
        to_log('网络配置码生成失败！')


# 3G-4G配置
def g3(pr=''):
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('http://dm.2dupay.com/wifi-config/wifiConfig.html')
        sleep(3)
        driver.find_element_by_id('pr').click()
        sleep(1)
        if pr:
            driver.find_element_by_xpath('//option[@value="USB"]').click()
        else:
            driver.find_element_by_xpath('//option[@value="无"]').click()
        driver.find_element_by_id('btn').click()
        sleep(5)
        driver.close()
    except:
        to_log('网络配置码生成失败！')