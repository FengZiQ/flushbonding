# coding=utf-8
import time
from dmSupport import get_device_attribute, issue_user_defined_config


# 写测试log
def to_log(str_info):

    with open('issueTest.log', "r+", encoding='UTF-8', errors='ignore') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ": " + str_info + '\n' + content
        )
        f.close()
    print(str_info)


# A5下发稳定性测试1: 2126
# A5下发稳定性测试2: 2127
count = 0
for i in range(10):
    device_att = get_device_attribute('4113180400131017')
    if '下发稳定性测试1' in device_att.get('send.test1', ''):
        issue_user_defined_config('2127', '2767390', '4113180400131017')
        time.sleep(10)
        count += 1
        temp0 = get_device_attribute('4113180400131017')
        if '下发稳定性测试2' in temp0.get('send.test1', ''):
            to_log('第' + str(count) + '次下发成功^_^')
        else:
            to_log('第' + str(count) + '次下发成功-_-')
    elif '下发稳定性测试2' in device_att.get('send.test1', ''):
        issue_user_defined_config('2126', '2767390', '4113180400131017')
        time.sleep(10)
        count += 1
        temp1 = get_device_attribute('4113180400131017')
        if '下发稳定性测试1' in temp1.get('send.test1', ''):
            to_log('第' + str(count) + '次下发成功^_^')
        else:
            to_log('第' + str(count) + '次下发成功-_-')
    else:
        issue_user_defined_config('2126', '2767390', '4113180400131017')
        time.sleep(10)
        count += 1
        temp2 = get_device_attribute('4113180400131017')
        if '下发稳定性测试1' in temp2.get('send.test1', ''):
            to_log('第' + str(count) + '次下发成功^_^')
        else:
            to_log('第' + str(count) + '次下发成功-_-')
