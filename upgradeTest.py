# coding=utf-8
import time
from to_log import to_log
from configFile import configuration
from dmSupport import get_device_attribute, send_upgrade_cmd

passCount = 0
failCount = 0
to_log('***升级成功率测试***')
for i in range(2):
    # 获取升级前的设备属性
    a0 = get_device_attribute(configuration['upgradeDeviceNo'])

    # 下发升级（417/484）
    upgrade_id = ['417', '484']
    if i % 2 == 0:
        send_upgrade_cmd('417')
    else:
        send_upgrade_cmd('484')
    time.sleep(5)
    # 升级过程等待20min，期间每个5秒获取一次设备属性
    # 如果最后一次属性上传时间与上次上传时间相等，则升级过程结束
    for ii in range(240):
        a1 = get_device_attribute(configuration['upgradeDeviceNo'])

        if a1['time'] != a0['time']:
            break

    # 升级完成后获取设备属性
    a3 = get_device_attribute(configuration['upgradeDeviceNo'])

    if a0['sys.software.version'] != a3['sys.software.version']:
        to_log('第' + str(i + 1) + '次升级成功 ^_^')
        passCount += 1
    else:
        to_log('第' + str(i + 1) + '次升级失败 -_-')
        failCount += 1

