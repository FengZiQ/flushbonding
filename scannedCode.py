# coding=utf-8
import requests
import time
from sign import jm
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def scanned_code(polling_flag='server'):
    # 请求体
    body = {
          "nonce_str": "test",
          "device_no": '4113171200100204',
          "auth_code": '134522254316672147',
          "goods_desc": "测试",
          "pp_trade_no": 'P' + str(int(time.time())*100),
          "total_fee": 1,
          "bill_create_ip": "192.168.2.109",
          "polling_flag": polling_flag,
          "undiscount_fee": 1
        }

    # 签名
    body['sign'] = jm(body, '12345')
    # 发起支付请求
    requests.post(
        'http://pay-api.testing.2dupay.com/api/scannedCode',
        json=body,
        verify=False
    )
    return None


if __name__ == "__main__":
    print(scanned_code())
