# coding=utf-8
import time
from to_log import to_log
from QRCodeOfNetworkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_networkTest, open_picture
from honorRouter import Configuration

rc = Configuration()

to_log('WiFi名称错误网络配置测试\n')

if rc.wc(name='QA', pwd='12345678', secure=2):
    # 生成WiFi名称错误网络配置二维码
    wifi_mode(name='QA1', pwd='12345678', pr='usb', dh='dhcp')

    # 配网时间
    time.sleep(15)

    # 获取系统当前时间
    nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    # 获取设备属性
    da = get_device_attribute(data_for_networkTest.get('deviceNo'))

    if nowTimestamp[:-3] != da.get('time', 'failed')[:-3]:
        to_log('WiFi名称错误网络配置测试Pass\n')
        # 打开设备信息码
        open_picture('deviceInfoCode.png')
    else:
        to_log('WiFi名称错误网络配置测试Failed\n')

rc.finished()


