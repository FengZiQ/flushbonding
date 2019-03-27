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
    try:
        # 开始被扫支付测试
        if sc_count == 4:
            print('\n被扫支付测试')
        if sc_count >= 4:
            print('请求body:\n' + str(req))
        # 前3次被扫支付触发轮询
        if sc_count <= 3:
            return {
                "code": "FAIL",
                "msg": "需要用户输入支付密码",
                "pp_trade_no": "18c041456160c9053006",
                "sub_code": "USERPAYING",
                "sub_msg": "需要用户输入支付密码"
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
    except Exception as e:
        print(e)
        return {
        }


@bottle.route('/api/query/order', method='POST')
def query():
    global qr_count
    qr_count += 1
    # 请求体
    req = bottle.request.json

    if qr_count == 1:
        print('\n订单轮询测试')
        print('请求body:\n' + str(req))

    print('第' + str(qr_count) + '轮询')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 第4次返回支付成功消息
    if qr_count == 4:
        print('第4次返回支付成功消息')
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
    # 第3次返回支付失败消息
    if qr_count == 7:
        print('第3次返回支付失败消息')
        return {
            "code": "FAIL",
            "msg": "101 付款码无效，请重新扫码",
            "pp_trade_no": "9878174153",
            "printType": 0,
            "sub_code": "AUTH_CODE_INVALID|FAIL",
            "sub_msg": "101 付款码无效，请重新扫码"
        }
    if qr_count == 14:
        print('第6次轮询仍然没有返回支付结果')
    return {
        "code": "FAIL",
        "msg": "需要用户输入支付密码",
        "pp_trade_no": "18c041456160c9053006",
        "sub_code": "USERPAYING",
        "sub_msg": "需要用户输入支付密码"
    }


@bottle.route('/api/deviceBillSummary', method='POST')
def device_bill():
    return {
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "total_pay_amt": 5,
        "total_pay_count": 4,
        "total_refund_amt": 2,
        "total_refund_count": 2
    }


bottle.run(host='192.168.20.94', port=8885)
