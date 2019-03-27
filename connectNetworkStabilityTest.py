# coding=utf-8
import time
import json
import requests
from tplinkRouter import Configuration
from send_email import send_email
from sign import jm

data = [
    '4113171200100030',
    '4113180400130996',
    '4113180400131015',
    '4113180800106239',
    '4113180700102921',
    '4113180800105465',
]
bad_disconnect = []
bad_connect = []


# 设备连接状态接口
def device_connect_status(device_no):
    body = {
            "device_no": device_no,
            "nonce_str": "232323",
            "token": "1c7c54925f153eaaa12758d70af17d2",
        }
    body['sign'] = jm(body, '12345')
    res = requests.post(
        url='http://common-api.2dupay.com/api/getDevice/v1.0/connectStatus',
        json=body
    )

    temp = json.loads(res.text)

    return temp.get('connect_status', 'error')


for i in range(2000):
    # 设备断网
    r = Configuration()
    r.wc('errorName', 'qa12345678')
    r.finished()
    time.sleep(180)
    # 3min后设备断开连接，否则发邮件：平台连接状态有问题
    for d in data:
        status1 = device_connect_status(d)
        if status1 == '1':
            # 等待15min后再检查一次设备状态是否在线，因为这里拿到的设备状态是点
            time.sleep(15)
            status2 = device_connect_status(d)
            if status2 == '1':
                bad_disconnect.append(d)
                data.remove(d)
    # 如果有断开设备
    if bad_disconnect:
        send_email(
            '盒子断网，平台设备状态为已连接',
            '问题设备：\n' + str(bad_disconnect),
            [
                'fengziqi@inspiry.cn'
            ]
        )
    # 恢复网络
    r = Configuration()
    r.wc('weak', 'qa12345678')
    r.finished()
    time.sleep(180)

    # 设备连网3min后平台状态为已连接，否则发邮件：平台连接状态有问题
    for d in data:
        status1 = device_connect_status(d)
        if status1 == '1':
            # 等待15min后再检查一次设备状态是否在线，因为这里拿到的设备状态是点
            time.sleep(15)
            status2 = device_connect_status(d)
            if status2 == '1':
                bad_connect.append(d)
                data.remove(d)
    # 如果有断开设备
    if bad_disconnect:
        send_email(
            '盒子断网，平台设备状态为已连接',
            '问题设备：\n' + str(bad_connect),
            [
                'fengziqi@inspiry.cn'
            ]
        )


