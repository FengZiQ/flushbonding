# coding=utf-8
import requests
from sign import jm
from configFile import data_for_paymentTest
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def refund(refund_no, refund_fee=1):

    body = {
        "nonce_str": "test",
        "device_no": data_for_paymentTest.get('deviceNo', ''),
        "pp_trade_no": refund_no,
        "refund_fee": refund_fee,
        "bill_create_ip": "192.168.25.165"
    }
    body['sign'] = jm(body, '12345')

    try:
        requests.post(
            data_for_paymentTest.get('payServer', '')+'api/refund',
            json=body,
            verify=False
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    from spSupport import verbose_payment
    vp = verbose_payment(
        data_for_paymentTest.get('merchantName', ''),
        data_for_paymentTest.get('merchantType', ''),
        data_for_paymentTest.get('deviceNo', ''),
    )[0]

    refund(vp.get('uOrderNo', ''))
