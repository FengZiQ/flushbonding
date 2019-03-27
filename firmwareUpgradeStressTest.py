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
    if a0.get('sys.software.version', '') == '4.1.0.15':
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '549')
    elif a0.get('sys.software.version', '') == '':
        to_log('获取设备属性失败！')
    else:
        send_upgrade_cmd(configuration['upgradeDeviceNo'], '587')
    # 平均升级时间，是一个经验时间
    time.sleep(180)

    # 日本立扫4G设备升级最长时间25min
    # 国内公版设备升级最长时间为16min
    # 升级过程进行3min后开始检测升级是否成功
    # 如果最后一次属性上传时间与上次上传时间相等，则升级过程结束
    for ii in range(276):
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
