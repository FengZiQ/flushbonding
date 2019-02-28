# coding=utf-8
import time
import json
import requests
from sign import jm
from to_log import to_log


# 设备连接状态接口
def open_api(device_no):
    body = {
        "device_no": device_no,
        'key': 'key',
        "nonce_str": "test",
    }
    body['sign'] = jm(body, '12345')
    res = requests.post(
        url='http://dm.inspos.cn/api/getServerUri',
        json=body
    )

    temp = json.loads(res.text)

    return temp


while True:
    res = open_api('4113180300111057')
    print(res)
    if res.get('code', '') == 'SUCCESS' and '80/ppcpws' in res.get('ppcp_uri', ''):
        to_log('get open api success')
    else:
        to_log('get open api failed')

    time.sleep(5)


