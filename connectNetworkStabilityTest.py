# coding=utf-8
import time
import json
import requests
from send_email import send_email
from sign import jm

data = [
    '4113180400131017',
    '4113180500100917',
    '4113180400113418',
    '4113181000108996',
    '4113180800100010',
    '4131180800100005',
    '4135180700101600',
    '4113180400129091',
    '4113180400131015',
    '4113180400130996',
    '4113180400131005',
    '4113171200100030',
    '4113180400129066',
    '4113180400129099',
    '4113180400129071',
    '4135180600100158'
]
bad_data = []


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


while True:
    # 检查是否有设备断开
    for d in data:
        status1 = device_connect_status(d)
        if status1 == '1':
            # 等待15min后再检查一次设备状态是否在线，因为这里拿到的设备状态是点
            time.sleep(15)
            status2 = device_connect_status(d)
            if status2 == '1':
                bad_data.append(d)
                data.remove(d)
    # 如果有断开设备
    if bad_data:
        send_email(
            '盒子断网，平台设备状态为已连接',
            '问题设备：\n' + str(bad_data),
            [
                'fengziqi@inspiry.cn'
            ]
        )
    # 若设备连接状态正常，恢复网络，等5min，再次断网
    if len(data) == 0:
        break
    # 每每隔5min检查设备连接状态
    time.sleep(300)


