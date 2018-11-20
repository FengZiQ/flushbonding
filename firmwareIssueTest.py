# coding=utf-8
from dmSupport import *
from configFile import data_for_issueTest


device_info = get_device_info(data_for_issueTest.get('deviceNo', ''))
customer_info = customer_info(data_for_issueTest.get('customerName', ''))

print(device_info)
print(customer_info)