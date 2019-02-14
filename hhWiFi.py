# coding=utf-8
import time
import json
import requests
from sign import jm
from to_log import to_log

data = [
    '4113180800106489',
    '4113180800106239',
    '4113180700102921'
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


while True:
    for d in data:
        status = device_connect_status(d)
        if status == '2':
            to_log('设备' + d + '断开连接')
    time.sleep(10)