# coding=utf-8
configuration = {
    # 升级设备
    'upgradeDeviceNo': '4113180400129053',
    # 扫码成功率测试设备及测试次数
    'scanDeviceNo': '4113180400129053',
    'scanTestTime': 3,
    # 配网成功率测试设备及测试次数
    'networkDeviceNo': '4113180400129053',
    'netConfigTestTime': 2,
    # 图片地址
    'filePath': r'D:/script/flushbonding/',
    # dm server
    'dmServer': 'http://dm.preo.inspos.cn/',
    # sp server
    'spServer': 'http://spadmin.preo.2dupay.com/',
    # cas server
    'casServer': 'http://cas.preo.2dupay.com/'
}

# 固件配网cases的测试数据
data_for_networkTest = {
    'deviceNo': '4113180400130999',
    'ip': '192.168.233.5',
    'mask': '255.255.255.0',
    'gw': '192.168.233.1',
    'dns': '10.10.2.6',
    'mobileWifiName': 'fzq',
    'mobileWifiPwd': '123456789'
}

# 固件升级cases的测试数据
data_for_upgradeTest = {
    'deviceNo': '4113180400130999',
    'fwPBeforeName': 'A5公版4.1.0.5',
    'fwPBeforeVersion': '4.1.0.5',
    'fwPCurrentName': 'A5公版4.1.0.8',
    'fwPCurrentVersion': '4.1.0.8',
}
