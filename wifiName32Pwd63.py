# coding=utf-8
import time
from to_log import to_log
from QRCodeOfNetworkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_networkTest
from honorRouter import Configuration

rc = Configuration()

to_log('SSID长度32/密码长度63网络配置测试\n')

if rc.wc(name='123a'*8, pwd='12'*30 + 'abc', secure=2):
    # 生成SSID长度32/密码长度63网络配置二维码
    wifi_mode(name='123a'*8, pwd='12'*30 + 'abc', dh='dhcp')

    # 配网时间
    time.sleep(10)

    # 获取系统当前时间
    nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    # 获取设备属性
    da = get_device_attribute(data_for_networkTest.get('deviceNo'))
    # 修正时间
    correction_time = nowTimestamp[:-4] + str(int(nowTimestamp[-4]) + 1)

    if da.get('time', 'failed')[:-3] == nowTimestamp[:-3] or da.get('time', 'failed')[:-3] == correction_time:
        if da.get('persist.net.type') == 'wifi' and da.get('persist.net.dhcp') == 'true':
            to_log('SSID长度32/密码长度63网络配置测试Pass\n')
            to_log('配网方式：'+da.get('persist.net.type', ''))
            to_log('DHCP：' + da.get('persist.net.dhcp', ''))
            to_log('IP：' + da.get('sys.net.ip', ''))
            to_log('MAC：' + da.get('system.net.wifi.mac', '') + '\n')
        else:
            to_log('请检查断言参数\n')
    else:
        to_log('SSID长度32/密码长度63网络配置测试Failed\n')

rc.finished()


