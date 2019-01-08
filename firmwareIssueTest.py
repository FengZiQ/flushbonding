# coding=utf-8
from dmSupport import *
from to_log import to_log
from configFile import data_for_issueTest

# 测试数据
device_info = get_device_info(data_for_issueTest['deviceNo'])
cus_info = customer_info(data_for_issueTest['customerName'])
para_config_info = get_para_config(data_for_issueTest['paraConfigName'])
self_config_id = get_self_common_config_id(data_for_issueTest['userDefineConfigName'])
self_config_info = get_self_common_config_info(self_config_id)

# 前置条件
# 参数配置绑定设备
if para_config_info.get('isDefault', '') != 1:
    bind_device_for_para_config(
        para_config_info.get('id', ''),
        device_info.get('id', ''),
        data_for_issueTest['deviceNo']
    )
# 自定义通用配置绑定设备
bind_or_unbind_self_common_config(
    self_config_id,
    action_type=1,
    device_id=device_info.get('id', ''),
    device_no=data_for_issueTest['deviceNo']
)

# 参数配置下发
to_log('参数配置与自定义通用配置下发测试')
issue_para_config(
    para_config_info.get('id', ''),
    device_info.get('id', ''),
    data_for_issueTest['deviceNo'],
    cus_info.get('id', '')
)

# 自定义通用配置下发
issue_user_defined_config(
    self_config_id,
    device_info.get('id', ''),
    data_for_issueTest['deviceNo']
)

# 获取设备属性
time.sleep(5)
device_attr = get_device_attribute(data_for_issueTest['deviceNo'])
# 断言：参数配置下发成功与否
para_config_issue_flag = False
assert1 = [
    para_config_info.get('scannedPayUrl', 'getFailed'),
    para_config_info.get('refundUrl', 'getFailed'),
    para_config_info.get('queryOrderUrl', 'getFailed')
]
for a in assert1:
    if a not in str(device_attr):
        to_log('url"' + a + '"不在设备属性中')
        para_config_issue_flag = True
if para_config_issue_flag:
    to_log('参数下发Fail\n')
else:
    to_log('参数下发PASS\n')

# 断言：自定义通用配置下发成功与否
self_config_issue_flag = False
for c in self_config_info:
    if c.get('paramValue', 'getFailed') not in str(device_attr):
        to_log('参数"' + c.get('paramShortname', 'getFailed') + '"不在设备属性中')
        self_config_issue_flag = True
if self_config_issue_flag:
    to_log('自定义通用配置下发Fail\n')
else:
    to_log('自定义通用配置下发PASS\n')

dm_session.close()
