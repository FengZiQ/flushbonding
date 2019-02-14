# coding=utf-8
import bottle
import time

count = 0


def to_log(file, str_info):

    with open(file, "r+", encoding='UTF-8', errors='ignore') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ": " + str_info + '\n' + content
        )
        f.close()


@bottle.route('/scannedCode', method='POST')
def scanned():
    global count
    count += 1
    to_log('en_paymentStressTest.log', '已请求：' + str(count) + '次')
    if count % 5 == 0:
        return {
            "pp_trade_no": "19102165527e20388816",
            "total_fee": 100,
            "pay_type": "ALIPAY",
            "printType": "0",
            "code": "FAIL",
            "sub_code": "USERPAYING",
            "sub_msg": "In user payment, need to enter password."
        }
    else:
        return {
            "bid_currency": "USD",
            "buyer_pay_fee": "7",
            "channel_type": "ALIPAY_GLOBAL",
            "code": "SUCCESS",
            "customer_name": "fzq",
            "msg": "SUCCESS",
            "pay_currency": "CNY",
            "pay_type": "ALIPAY",
            "pp_trade_no": "15452944623612564P",
            "printType": 1,
            "real_fee": "1",
            "receipt": "RGV2aWNlTm86IDQxMTMxODA0MDAxMjkwNTMKcGF5VHlwZTogQUxJUEFZCuiuouWNleWPtzogR1AzOTY5MDU2MjU0MTI1MzE1MjAK7Yuw7JeU65SU7JeUOiBmenEKCgo=",
            "settlement_currency": "USD",
            "time_end": "2018-12-20 17:27:44",
            "total_fee": 1,
            "transaction_id": "2018122022001402500505538484",
            "user_order_no": "GP396905625412531520"
        }


@bottle.route('/order/query', method='POST')
def query():
    return {
        "bid_currency": "USD",
        "buyer_pay_fee": "7",
        "channel_type": "ALIPAY_GLOBAL",
        "code": "SUCCESS",
        "customer_name": "fzq",
        "msg": "SUCCESS",
        "pay_currency": "CNY",
        "pay_type": "ALIPAY",
        "pp_trade_no": "15452944623612564P",
        "printType": 1,
        "real_fee": "1",
        "receipt": "RGV2aWNlTm86IDQxMTMxODA0MDAxMjkwNTMKcGF5VHlwZTogQUxJUEFZCuiuouWNleWPtzogR1AzOTY5MDU2MjU0MTI1MzE1MjAK7Yuw7JeU65SU7JeUOiBmenEKCgo=",
        "settlement_currency": "USD",
        "time_end": "2018-12-20 17:27:44",
        "total_fee": 1,
        "transaction_id": "2018122022001402500505538484",
        "user_order_no": "GP396905625412531520"
    }


bottle.run(host='192.168.20.94', port=8881)
