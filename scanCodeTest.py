# coding=utf-8
from selenium import webdriver
from spSupport import verbose_payment
from configFile import configuration
from to_log import to_log
import time


# 打开浏览器
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///' + configuration['filePath'] + 'blank.png')
start = input('输入1开始，输入0结束:\n')
passCount = 0
failCount = 0

if start:
    to_log('***扫码后成功发起支付请求率测试***')
    for i in range(configuration['scanTestTime']):
        bill1 = verbose_payment('4113180400130999')
        driver.get('file:///' + configuration['filePath'] + 'wxCode.png')
        time.sleep(1)
        driver.get('file:///' + configuration['filePath'] + 'blank.png')
        time.sleep(5)
        bill2 = verbose_payment('4113180400130999')
        # print(logContent['lc'])
        if len(bill1) + 1 == len(bill2):
            to_log('第' + str(i+1) + '次扫码后发起支付请求成功 ^_^')
            passCount += 1
        else:
            to_log('第' + str(i+1) + '次扫码后发起支付请求失败 -_-')
            failCount += 1

to_log('\n\n成功次数为：%d' % passCount)
to_log('失败次数为：%d' % failCount)
to_log('成功率：%d%s' % ((passCount/(passCount + failCount))*100, '%'))
driver.close()

