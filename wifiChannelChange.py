# coding=utf-8
import time
from to_log import to_log
from networkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases
from honorRouter import rc

if rc.wc(name='QA', pwd='12345678', secure=2):
    # 生成网络配置二维码
    wifi_mode(name='QA', pwd='12345678', dh='dhcp')

    # 配网时间
    time.sleep(10)

    for i in range(1, 14):
        # 改变信道
        if rc.channel_set(i):
            # 10s后若设备属性可以上传，则说明盒子支持该信道
            time.sleep(10)
            # 获取系统当前时间
            nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            # 获取设备属性
            da = get_device_attribute(data_for_cases.get('deviceNo'))
            # 修正时间
            correction_time = nowTimestamp[:-4] + str(int(nowTimestamp[-4]) + 1)

            if da.get('time', 'failed')[:-3] == nowTimestamp[:-3] or da.get('time', 'failed')[:-3] == correction_time:
                if da.get('persist.net.type') == 'wifi' and da.get('persist.net.dhcp') == 'true':
                    to_log('WIFI信道为 ' + str(i) + ' 时网络配置测试Pass\n')
                    to_log('配网方式：'+da.get('persist.net.type'))
                    to_log('DHCP：' + da.get('persist.net.dhcp'))
                    to_log('IP：' + da.get('sys.net.ip'))
                    to_log('MAC：' + da.get('system.net.wifi.mac') + '\n')
                else:
                    to_log('请检查断言参数\n')
            else:
                to_log('WIFI信道为 ' + str(i) + ' 时网络配置测试Failed\n')

rc.finished()