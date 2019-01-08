# coding=utf-8
from dmSupport import *
from configFile import configuration, data_for_networkTest


custom_common_config_id = None
if 'testing' in configuration.get('dmServer', ''):
    custom_common_config_id = 106
elif 'preo' in configuration.get('dmServer', ''):
    custom_common_config_id = 90
else:
    custom_common_config_id = 90

device_info = get_device_info(data_for_networkTest.get('deviceNo', ''))

# 自定义通用配置参数下发
issue_user_defined_config(custom_common_config_id, device_info['id'], device_info.get('serialNum', ''))
