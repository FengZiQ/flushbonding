# coding=utf-8

configuration = {
    # 升级设备
    'upgradeDeviceNo': '4113190300115191',
    # 扫码成功率测试设备及测试次数
    'scanDeviceNo': '4126180500100018',
    'scanTestTime': 3,
    # 配网成功率测试设备及测试次数
    'networkDeviceNo': '4126180500100018',
    'netConfigTestTime': 2,
    # 图片地址
    'filePath': r'D:/script/flushbonding/',
    # dm server
    'dmServer': 'http://dm.inspos.cn/',
    # sp server
    'spServer': 'http://spadmin.2dupay.com/',
    # cas server
    'casServer': 'http://cas.2dupay.com/',
}

# 固件配网cases的测试数据
data_for_networkTest = {
    'deviceNo': '4113180400130999',
    'ip': '192.168.233.215',
    'mask': '255.255.255.0',
    'gw': '192.168.233.1',
    'dns': '192.168.233.1',
    'mobileWifiName': 'fzq',
    'mobileWifiPwd': '123456789',
}

# 固件升级cases的测试数据
data_for_upgradeTest = {
    'deviceNo': '4126180500100018',
    'fwPBeforeName': 'A5公版4.1.0.5',
    'fwPBeforeVersion': '4.1.0.5',
    'fwPCurrentName': 'A5公版4.1.0.8',
    'fwPCurrentVersion': '4.1.0.8',
}

# 支付相关cases测试数据
data_for_paymentTest = {
    'deviceNo': '4126180500100018',
    'merchantName': 'sh1m1子',
    'merchantType': '门店',
    'payServer': 'https://sp.preo.2dupay.com/',
}

# 下发相关cases测试数据
data_for_issueTest = {
    'deviceNo': '4113180400130999',
    'customerName': '测试账户INSPOS',
    'paraConfigName': 'test_fengziqi',
    'userDefineConfigName': '测试_fengziqi'
}


# 用浏览器打开图片
def open_picture(picture_name):
    from selenium import webdriver
    from time import sleep

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('file:///' + configuration['filePath'] + picture_name)
    sleep(1)
    driver.close()
    return None


# 一定时间内检查网络配置是否成功
def check_network_config_if_success(want_time, device_no=data_for_networkTest.get('deviceNo')):
    import time
    from dmSupport import get_device_attribute
    from to_log import to_log

    flag = False
    try:
        for i in range(int(want_time/5)):
            # 获取系统当前时间
            ts = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            # 获取设备属性
            da = get_device_attribute(device_no)
            # 修正时间
            ct = ts[:-4] + str(int(ts[-4]) + 1)
            if da.get('time', 'failed')[:-3] == ts[:-3] or da.get('time', 'failed')[:-3] == ct:
                flag = True
                break
    except:
        to_log('检查网络配置模块异常, 请确认输入的时间是否为5的整数倍')

    return flag
