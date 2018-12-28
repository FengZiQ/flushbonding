# coding=utf-8
import bottle
import time

cn_count, en_count, jp_count, ko_count = 0, 0, 0, 0


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
    req = bottle.request.json
    if req.get('device_no', '') == '4126180500100106':
        global cn_count
        cn_count += 1
        to_log('CnPaymentLog.log', '已请求：' + str(cn_count) + '次')
        return {
            "buyer_pay_fee": "1",
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": "1",
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": 1,
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }

    elif req.get('device_no', '') == '4126180500100091':
        global en_count
        en_count += 1
        to_log('EnPaymentLog.log', '已请求：' + str(en_count) + '次')
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
    elif req.get('device_no', '') == '4126180500100043':
        global jp_count
        jp_count += 1
        to_log('JpPaymentLog.log', '已请求：' + str(jp_count) + '次')
        return {
            "bid_currency": "JPY",
            "buyer_pay_fee": "100",
            "channel_type": "STARPAY",
            "code": "SUCCESS",
            "customer_name": "门店1",
            "msg": "SUCCESS",
            "pay_currency": "JPY",
            "pay_type": "WXPAY",
            "pp_trade_no": "1545293685882760P",
            "printType": 1,
            "real_fee": "100",
            "receipt": "1qe4tre9yr06IFdFQ0hBVAoKCg==",
            "settlement_currency": "JPY",
            "time_end": "2018-12-20 17:14:52",
            "total_fee": 100,
            "transaction_id": "100110010016GP396902369273989376",
            "user_order_no": "GP396902369273989376"
        }
    elif req.get('device_no', '') == '4126180500100119':
        global ko_count
        ko_count += 1
        to_log('KoPaymentLog.log', '已请求：' + str(ko_count) + '次')
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
    else:
        return {}


bottle.run(host='192.168.20.94', port=8883)
