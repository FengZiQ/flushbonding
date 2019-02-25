# coding=utf-8
import time
import json
import requests
from send_email import send_email
from sign import jm
from to_log import to_log
from setDongle import set_dongle

data = [
    '4113171200100030',
    '4113180400129063'
]


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


count = 0
bug_device0 = []
bug_device1 = []
while True:
    count += 1
    to_log('第' + str(count) + '断网')
    # 断网
    if set_dongle():
        time.sleep(180)
        # 3min后查询设备连接状态
        for d in data:
            status = device_connect_status(d)
            to_log('设备' + d + '连接状态为：' + status)
            if status == '1':
                bug_device0.append(d)

        # 断网3min后是否有“已连接”设备
        if bug_device0:
            # 等3min后再次查询设备连接状态
            time.sleep(180)
            for db in bug_device0:
                if device_connect_status(db) == '1':
                    bug_device1.append(db)
        # 断网6min后若有“已连接”设备，发送邮件
        if bug_device1:
            send_email(
                '盒子断网，平台设备状态为已连接',
                '问题设备：\n' + str(bug_device1),
                [
                    'fengziqi@inspiry.cn'
                ]
            )
        # 若设备连接状态正常，恢复网络，等5min，再次断网
        else:
            set_dongle()
            time.sleep(300)



