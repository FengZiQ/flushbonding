# coding=utf-8
import time
from to_log import to_log
from QRCodeOfNetworkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases
from honorRouter import rc

if rc.wc(name='孙 _!@#$%sunnana', pwd='!_@#$%+4sunnana', secure=2):
    rc.finished()

    # 生成WiFi含中文、特殊字符、空格网络配置二维码
    wifi_mode(name='孙 _!@#$%sunnana', pwd='!_@#$%+4sunnana', dh='dhcp')

    # 配网时间
    time.sleep(10)

    # 获取系统当前时间
    nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    # 获取设备属性
    da = get_device_attribute(data_for_cases.get('deviceNo'))
    # 修正时间
    correction_time = nowTimestamp[:-4] + str(int(nowTimestamp[-4]) + 1)

    if da.get('time', 'failed')[:-3] == nowTimestamp[:-3] or da.get('time', 'failed')[:-3] == correction_time:
        if da.get('persist.net.type') == 'wifi' and da.get('persist.net.dhcp') == 'true':
            to_log('WiFi含中文、特殊字符、空格网络配置测试Pass\n')
            to_log('配网方式：'+da.get('persist.net.type'))
            to_log('DHCP：' + da.get('persist.net.dhcp'))
            to_log('IP：' + da.get('sys.net.ip'))
            to_log('MAC：' + da.get('system.net.wifi.mac'))
        else:
            to_log('请检查断言参数\n')
    else:
        to_log('WiFi含中文、特殊字符、空格网络配置测试Failed\n')
else:
    rc.finished()


