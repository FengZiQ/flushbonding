# coding=utf-8
import time
from to_log import to_log
from configFile import data_for_upgradeTest
from dmSupport import get_device_attribute, send_upgrade_cmd, get_upgrade_package_info


# 升级包信息
p1 = get_upgrade_package_info(
    data_for_upgradeTest['fwPBeforeName'],
    data_for_upgradeTest['fwPBeforeVersion']
)
p2 = get_upgrade_package_info(
    data_for_upgradeTest['fwPCurrentName'],
    data_for_upgradeTest['fwPCurrentVersion']
)


def upgrade_to_old_version():
    # 向低版本升级测试
    to_log('向低版本升级测试')
    # 获取升级前的设备属性
    a0 = get_device_attribute(data_for_upgradeTest['deviceNo'])
    to_log('升级前版本号为：' + a0.get('sys.software.version', ''))
    # 发送升级命令
    send_upgrade_cmd(data_for_upgradeTest['deviceNo'], p1.get('id', ''))
    time.sleep(10)
    # 检查升级过程是否完成
    for ii in range(240):
        a1 = get_device_attribute(data_for_upgradeTest['deviceNo'])
        if a1.get('time', '1') != a0.get('time', ''):
            break
    # 升级完成后获取设备属性
    a2 = get_device_attribute(data_for_upgradeTest['deviceNo'])
    to_log('升级后版本号为：' + a2.get('sys.software.version', ''))
    # 断言升级是否成功
    if a0.get('sys.software.version', '') != a2.get('sys.software.version', ''):
        to_log('向低版本升级测试PASS\n')
        return True
    else:
        to_log('向低版本升级测试Failed\n')
        return False


if upgrade_to_old_version():
    # 低版本向当前版升级测试
    to_log('低版本向当前版升级测试')
    # 获取升级前的设备属性
    a3 = get_device_attribute(data_for_upgradeTest['deviceNo'])
    to_log('升级前版本号为：' + a3.get('sys.software.version', ''))
    # 发送升级命令
    send_upgrade_cmd(data_for_upgradeTest['deviceNo'], p2.get('id', ''))
    time.sleep(10)
    # 检查升级过程是否完成
    for ii in range(240):
        a4 = get_device_attribute(data_for_upgradeTest['deviceNo'])
        if a3.get('time', '') != a4.get('time', ''):
            break
    # 升级完成后获取设备属性
    a5 = get_device_attribute(data_for_upgradeTest['deviceNo'])
    to_log('升级后版本号为：' + a5.get('sys.software.version', ''))
    # 断言升级是否成功
    if a3.get('sys.software.version', '') != a5.get('sys.software.version', ''):
        to_log('低版本向当前版升级测试PASS\n')

    else:
        to_log('低版本向当前版升级测试Failed\n')
else:
    to_log('低版本向当前版升级测试的前置条件Failed\n')