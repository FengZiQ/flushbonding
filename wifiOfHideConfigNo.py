# coding=utf-8
import time
from to_log import to_log
from networkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases
from honorRouter import rc

if rc.wc(name='QA', pwd='12345678', secure=2, ssid=True):
    rc.finished()

    # 生成WIFI设成隐藏，配置界面选择否网络配置二维码
    wifi_mode(name='QA', pwd='12345678', ss_id=False, dh='dhcp')

    # 配网时间
    time.sleep(10)

    # 获取系统当前时间
    nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    # 获取设备属性
    da = get_device_attribute(data_for_cases.get('deviceNo'))

    if nowTimestamp[:-3] != da.get('time', 'failed')[:-3]:
        to_log('WIFI设成隐藏，配置界面选择否网络配置测试Pass\n')
    else:
        to_log('WIFI设成隐藏，配置界面选择否网络配置测试Failed\n')
else:
    rc.finished()


