# coding=utf-8
import time
from to_log import to_log
from configFile import configuration
from dmSupport import get_device_attribute, send_upgrade_cmd

passCount = 0
failCount = 0
to_log('***升级成功率测试***')
for i in range(20):
    # 获取升级前的设备属性
    a0 = get_device_attribute(configuration['upgradeDeviceNo'])
    to_log('第' + str(i+1) + '次升级前版本为：' + a0.get('sys.software.version', ''))

    # 下发升级（4.0.38:153/4.0.38.4:172）
    if a0.get('sys.software.version', '') == '4.0.38':
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '172')
    elif a0.get('sys.software.version', '') == '':
        to_log('获取设备属性失败！')
    else:
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '153')
    time.sleep(15)

    # 升级过程等待20min，期间每个5秒获取一次设备属性
    # 如果最后一次属性上传时间与上次上传时间相等，则升级过程结束
    for ii in range(240):
        a1 = get_device_attribute(configuration['upgradeDeviceNo'])
        if a1.get('time', '') != a0.get('time', ''):
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
