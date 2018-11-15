# coding=utf-8
import time
from to_log import to_log
from networkConfig import wifi_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases
from honorRouter import rc

if rc.wc(name='QA', pwd='12345678', secure=2):
    rc.finished()

    # 生成WIFI+DHCP+USB网络配置二维码
    wifi_mode(name='QA', pwd='12345678', pr='usb', dh='dhcp')

    # 配网时间
    time.sleep(10)

    # 获取系统当前时间
    nowTimestamp1 = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    # 获取设备属性
    da1 = get_device_attribute(data_for_cases.get('deviceNo'))
    # 修正时间
    correction_time1 = nowTimestamp1[:-4] + str(int(nowTimestamp1[-4]) + 1)

    if da1.get('time', 'failed')[:-3] == nowTimestamp1[:-3] or da1.get('time', 'failed')[:-3] == correction_time1:
        # 生成WIFI+DHCP+USB网络配置二维码
        wifi_mode(name='wrong name', pwd='wrong pwd', pr='usb', dh='dhcp')
        # 配网时间
        time.sleep(10)
        # 获取系统当前时间
        nowTimestamp2 = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        # 获取设备属性
        da2 = get_device_attribute(data_for_cases.get('deviceNo'))
        if da2.get('time', 'failed')[:-3] != nowTimestamp2[:-3]:
            # 生成WIFI+DHCP+USB网络配置二维码
            wifi_mode(name='QA', pwd='12345678', pr='usb', dh='dhcp')

            # 配网时间
            time.sleep(10)

            # 获取系统当前时间
            nowTimestamp3 = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            # 获取设备属性
            da3 = get_device_attribute(data_for_cases.get('deviceNo'))
            # 修正时间
            correction_time3 = nowTimestamp3[:-4] + str(int(nowTimestamp3[-4]) + 1)
            if da3.get('time', 'failed')[:-3] == nowTimestamp3[:-3] or da3.get('time', 'failed')[:-3] == correction_time3:
                to_log('断网重连测试PASS\n')
            else:
                to_log('断网重连测试Failed\n')
        else:
            to_log('断网时失败了。。。断网重连测试Failed\n')
    else:
        to_log('连接网络时失败了。。。断网重连测试Failed\n')

else:
    rc.finished()
