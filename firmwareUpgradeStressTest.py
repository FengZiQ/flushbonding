# coding=utf-8
import time
from to_log import to_log
from configFile import configuration
from dmSupport import get_device_attribute, send_upgrade_cmd

passCount = 0
failCount = 0
to_log('***升级成功率测试***')
for i in range(10000):
    # 获取升级前的设备属性
    a0 = get_device_attribute(configuration['upgradeDeviceNo'])
    to_log('第' + str(i+1) + '次升级前版本为：' + a0.get('sys.software.version', ''))

    if a0.get('sys.software.version', '') == '5.1.0.16' and a0.get('sys.ppcp.status', '') == 'on':
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '748')
    if a0.get('sys.software.version', '') == '5.1.0.15' and a0.get('sys.ppcp.status', '') == 'on':
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '747')
    # 这里等待的时间为设备收到升级命令至重启连网的时间
    time.sleep(90)

    for ii in range(30):
        a1 = get_device_attribute(configuration['upgradeDeviceNo'])
        if a1.get('sys.net.status', '') == 'CONNECTED' and a1.get('sys.ppcp.status', '') == 'on':
            break

    # 升级完成后获取设备属性
    a3 = get_device_attribute(configuration['upgradeDeviceNo'])
    to_log('第' + str(i+1) + '次升级后版本为：' + a3.get('sys.software.version', ''))

    if a0.get('sys.software.version', '') != a3.get('sys.software.version', ''):
        to_log('第' + str(i + 1) + '次升级成功 ^_^')
        passCount += 1
    else:
        to_log('第' + str(i + 1) + '次升级失败 -_-')
        failCount += 1

to_log('\n\n升级总成功次数为：%d' % passCount)
to_log('升级总失败次数为：%d' % failCount)
to_log('升级成功率：%d%s' % ((passCount/(passCount + failCount))*100, '%'))
