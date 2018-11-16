# coding=utf-8
import time
from to_log import to_log
from QRCodeOfNetworkConfig import g3
from dmSupport import get_device_attribute
from configFile import data_for_cases

# 生成3G有打印机网络配置二维码
g3(pr='usb')

# 配网时间
time.sleep(10)

# 获取系统当前时间
nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
# 获取设备属性
da = get_device_attribute(data_for_cases.get('deviceNo'))
# 修正时间
correction_time = nowTimestamp[:-4] + str(int(nowTimestamp[-4]) + 1)

if da.get('time', 'failed')[:-3] == nowTimestamp[:-3] or da.get('time', 'failed')[:-3] == correction_time:
    if da.get('persist.net.type') == '3g' and da.get('persist.net.dhcp') == 'true':
        to_log('3G有打印机网络配置测试Pass\n')
        to_log('配网方式：'+da.get('persist.net.type'))
        to_log('DHCP：' + da.get('persist.net.dhcp'))
        to_log('IP：' + da.get('sys.net.ip'))
        to_log('MAC：' + da.get('system.net.wifi.mac'))
    else:
        to_log('\n请检查断言参数\n')
else:
    to_log('\n3G有打印机网络配置测试Failed\n')

