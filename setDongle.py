# coding=utf-8
from time import sleep
from selenium import webdriver


# 管理dongle网络
def set_dongle():
    flag = True
    # 打开火狐浏览器
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        # 打开dongle管理页面
        driver.get('http://XL.GO')
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div/div/ul/li[2]/a').click()
        sleep(3)
        try:
            driver.find_element_by_id('user').clear()
            driver.find_element_by_id('user').send_keys('admin')
            driver.find_element_by_id('pwd').clear()
            driver.find_element_by_id('pwd').send_keys('123456')
            driver.find_element_by_id('login').click()
            sleep(3)
        except:
            pass
        driver.find_element_by_id('btn_connect').click()
        sleep(5)
    except:
        flag = False
    driver.quit()
    return flag

