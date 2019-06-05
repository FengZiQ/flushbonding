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
    # 获取设备属性
    da = get_device_attribute('4140190200100062')
    # 修正时间
    correction_time = nowTimestamp[:-4] + str(int(nowTimestamp[-4]) + 1)

    if da.get('time', 'failed')[:-3] == nowTimestamp[:-3] or da.get('time', 'failed')[:-3] == correction_time:
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
    time.sleep(10)
    # 获取设备属性上传时间
    dmTimestamp1 = get_device_attribute('4140190200100062').get('time', '获取时间失败')
    time.sleep(5)
    dmTimestamp2 = get_device_attribute('4140190200100062').get('time', '获取时间失败')

    if dmTimestamp2 != dmTimestamp1:
        to_log('第' + str(i + 1) + '断网失败 -_-', file='4gModeTest.log')
    else:
        to_log('第' + str(i + 1) + '断网成功 ^_^', file='4gModeTest.log')


to_log('\n\n配网总成功次数为：%d' % passCount, file='4gModeTest.log')
to_log('配网总失败次数为：%d' % failCount, file='4gModeTest.log')
to_log('配网成功率：%d%s' % ((passCount/500)*100, '%'), file='4gModeTest.log')
driver.close()
