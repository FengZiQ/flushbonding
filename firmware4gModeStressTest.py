# coding=utf-8
import time
from to_log import to_log
from selenium import webdriver
from dmSupport import get_device_attribute


# 打开浏览器
driver = webdriver.Firefox(r'C:\Users\dell\AppData\Roaming\Mozilla\Firefox\Profiles\a4kze4xj.selenium')
driver.maximize_window()
driver.get('file:///D:/script/flushbonding/blank.png')
passCount = 0
failCount = 0

to_log('***网络配置成功率测试***', file='4gModeTest.log')
for i in range(500):
    # 配网
    driver.get('file:///D:/script/flushbonding/4gMode.png')
    # 识别时间
    time.sleep(1)
    # 打开空白图片
    driver.get('file:///D:/script/flushbonding/blank.png')
    # 日本4G卡配网时间35s，DM设备状态变更2min
    time.sleep(125)

    # 获取系统当前时间
    nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    to_log(nowTimestamp, file='4gModeTest.log')
    # 获取设备属性上传时间
    dmTimestamp1 = get_device_attribute('4140190200100062').get('time', '获取时间失败')
    to_log(dmTimestamp1, file='4gModeTest.log')
    if nowTimestamp[:-3] == dmTimestamp1[:-3]:
        to_log('第' + str(i + 1) + '配网成功 ^_^', file='4gModeTest.log')
        passCount += 1
    else:
        to_log('第' + str(i + 1) + '配网失败 -_-', file='4gModeTest.log')
        failCount += 1

    # 断网
    driver.get('file:///D:/script/flushbonding/lanMode.png')
    # 识别时间
    time.sleep(1)
    # 打开空白图片
    driver.get('file:///D:/script/flushbonding/blank.png')
    # 配网时间
    time.sleep(15)
    # 获取设备属性上传时间
    dmTimestamp2 = get_device_attribute('4140190200100062').get('time', '获取时间失败')
    print(dmTimestamp2)

    if dmTimestamp2[:-3] == dmTimestamp1[:-3]:
        to_log('第' + str(i + 1) + '断网成功 ^_^', file='4gModeTest.log')
    else:
        to_log('第' + str(i + 1) + '断网失败 -_-', file='4gModeTest.log')


to_log('\n\n配网总成功次数为：%d' % passCount, file='4gModeTest.log')
to_log('配网总失败次数为：%d' % failCount, file='4gModeTest.log')
to_log('配网成功率：%d%s' % ((passCount/500)*100, '%'), file='4gModeTest.log')
driver.close()
