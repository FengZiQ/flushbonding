# coding=utf-8
import time
from to_log import to_log
from networkConfig import lan_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases

# 生成LAN+DHCP+USB网络配置二维码
lan_mode(pr='usb', dh='dh')

# 获取系统当前时间
nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
# 获取设备属性
da = get_device_attribute(data_for_cases.get('deviceNo'))

if nowTimestamp[:-3] == da.get('time', 'failed')[:-3]:
    if da.get('persist.net.type') == 'eth' or da.get('persist.net.dhcp') == 'true':
        to_log('LAN+DHCP+USB网络配置成功！')
        to_log('配网方式：'+da.get('persist.net.type'))
        to_log('DHCP：' + da.get('persist.net.dhcp'))
        to_log('IP：' + da.get('sys.net.ip'))
        to_log('MAC：' + da.get('system.net.wifi.mac'))
    else:
        to_log('\n请检查断言参数\n')
else:
    to_log('\nLAN+DHCP+USB网络配置失败！\n')

