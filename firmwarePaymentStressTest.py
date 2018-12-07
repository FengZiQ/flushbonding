# coding=utf-8
import bottle
import time

count = 0


def to_log(str_info):

    with open('paymentStressTest.log', "r+", encoding='UTF-8', errors='ignore') as f:
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
    to_log('已请求：' + str(count) + '次')
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


bottle.run(host='192.168.20.94', port=8880)
