# coding=utf-8
from dmSupport import *
from configFile import data_for_issueTest


device_info = get_device_info(data_for_issueTest.get('deviceNo', ''))
customer_info = customer_info(data_for_issueTest.get('customerName', ''))
commonconfig_info = get_self_common_config_id(data_for_issueTest.get('userDefinedCommonConfig',''))

#自定义通用配置参数绑定
device_and_self_common_config(commonconfig_info,'1',device_info['id'],device_info['serialNum'])
#自定义通用配置参数下发
user_defined_config(commonconfig_info,device_info['id'],device_info['serialNum'])
