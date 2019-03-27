# coding=utf-8
import bottle
import time

sc_count = 0
qr_count = 0


@bottle.route('/api/scannedCode', method='POST')
def scanned():
    # 测试不同场景flag
    global sc_count
    sc_count += 1
    # 请求体
    req = bottle.request.json

    print('请求body：\n' + str(req) + '\n')

    if sc_count == 1:
        print('被扫支付请求发出后(被扫接口)断网测试')
        time.sleep(10)
        return {
            "buyer_pay_fee": req.get('total_fee', ''),
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": req.get('total_fee', ''),
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": req.get('total_fee', ''),
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    if sc_count == 2:
        print('被扫支付请求发出后(被扫接口)断电测试')
        time.sleep(10)
        return {
            "buyer_pay_fee": req.get('total_fee', ''),
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": req.get('total_fee', ''),
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": req.get('total_fee', ''),
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }

    return {
        "code": "FAIL",
        "msg": "需要用户输入支付密码",
        "pp_trade_no": "18c041456160c9053006",
        "sub_code": "USERPAYING",
        "sub_msg": "需要用户输入支付密码"
    }


@bottle.route('/api/query/order', method='POST')
def query():
    global qr_count
    qr_count += 1
    # 请求体
    req = bottle.request.json

    print('请求body：\n' + str(req) + '\n')

    if qr_count == 1:
        print('轮询请求发出后断网测试')
        time.sleep(10)
        return {
            "buyer_pay_fee": req.get('total_fee', ''),
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": req.get('total_fee', ''),
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": req.get('total_fee', ''),
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    if qr_count == 2:
        print('轮询请求发出后断电测试')
        time.sleep(10)
        return {
            "buyer_pay_fee": req.get('total_fee', ''),
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 1,
            "real_fee": req.get('total_fee', ''),
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": req.get('total_fee', ''),
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    return {
        "buyer_pay_fee": req.get('total_fee', ''),
        "channel_type": "ALIPAY",
        "code": "SUCCESS",
        "customer_name": "sh1m1хнР",
        "msg": "SUCCESS",
        "pay_type": "ALIPAY",
        "pp_trade_no": "P154296563600",
        "printType": 1,
        "real_fee": req.get('total_fee', ''),
        "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
        "time_end": "2018-11-23 17:33:57",
        "total_fee": req.get('total_fee', ''),
        "transaction_id": "2018112322001402501015842257",
        "user_order_no": "P387137821445425600"
    }


bottle.run(host='192.168.20.94', port=8886)
