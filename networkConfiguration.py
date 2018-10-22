# coding=utf-8
import time
from to_log import to_log
from selenium import webdriver
from configFile import configuration
from dmSupport import get_device_attribute


# 打开浏览器
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///' + configuration['filePath'] + 'blank.png')
start = input('输入1开始，输入0结束:\n')
passCount = 0
failCount = 0

if start:
    to_log('***网络配置成功率测试***')
    for i in range(configuration['netConfigTestTime']):
        # 配网
        driver.get('file:///' + configuration['filePath'] + 'netPass.png')
        # 识别时间
        time.sleep(1)
        # 打开空白图片
        driver.get('file:///' + configuration['filePath'] + 'blank.png')
        # 配网时间
        time.sleep(15)

        # 获取系统当前时间
        nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        to_log(nowTimestamp)
        # 获取设备属性上传时间
        dmTimestamp1 = get_device_attribute('networkDeviceNo')['time']
        to_log(dmTimestamp1)
        if nowTimestamp[-3:] == dmTimestamp1[-3:]:
            to_log('第' + str(i + 1) + '配网成功 ^_^')
            passCount += 1
        else:
            to_log('第' + str(i + 1) + '配网失败 -_-')
            failCount += 1

        # 断网
        driver.get('file:///' + configuration['filePath'] + 'netFail.png')
        # 识别时间
        time.sleep(1)
        # 打开空白图片
        driver.get('file:///' + configuration['filePath'] + 'blank.png')
        # 配网时间
        time.sleep(15)
        # 获取设备属性上传时间
        dmTimestamp2 = get_device_attribute('networkDeviceNo')['time']
        print(dmTimestamp2)

        if dmTimestamp2[-3:] == dmTimestamp1[-3:]:
            to_log('第' + str(i + 1) + '断网成功 ^_^')
        else:
            to_log('第' + str(i + 1) + '断网失败 -_-')


to_log('\n\n配网总成功次数为：%d' % passCount)
to_log('配网总失败次数为：%d' % failCount)
to_log('配网成功率：%d%s' % ((passCount/configuration['netConfigTestTime'])*100, '%'))
driver.close()
