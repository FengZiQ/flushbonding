# coding=utf-8
import bottle
import time

sc_count = 0
qr_count = 0
rf_count = 0
co_count = 0


@bottle.route('/api/scannedCode', method='POST')
def scanned():
    # 测试不同场景flag
    global sc_count
    sc_count += 1
    # 请求体
    req = bottle.request.json
    try:
        # 开始被扫支付测试
        if sc_count == 9:
            print('\n被扫支付测试')
        if sc_count >= 9:
            print('支付请求body:\n' + str(req))
        # 前3次被扫支付触发轮询
        if sc_count <= 8:
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
    print('订单状态请求body:\n' + str(req))

    print('第' + str(qr_count) + '轮询')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 第2次返回支付成功消息
    if qr_count == 2:
        print('第2次返回支付成功消息')
        return {
            "buyer_pay_fee": "100",
            "channel_type": "ALIPAY",
            "code": "SUCCESS",
            "customer_name": "sh1m1хнР",
            "msg": "SUCCESS",
            "pay_type": "ALIPAY",
            "pp_trade_no": "P154296563600",
            "printType": 100,
            "real_fee": "100",
            "receipt": "tqm1pbHgusU6IDIwMTgxMTIzMjIwMDE0MDI1MDEwMTU4NDIyNTcKvbvS18qxvOQ6IDIwMTgtMTEtMjMgMTc6MzM6NTcK19wgvfAgtu46IDAuMDEKyrW4tr3wtu46IDAuMDEK08W73b3wtu46IDAuMDAKyeixuLHgusU6IDQxMTMxODA0MDAxMjg4MDAKvbvS18Dg0M06INanuLaxpgrJzLunw/uzxjogc2gxbTHX0wqyu7LO0+vTxbvdvfC27jogMC4wMAoKCg==",
            "time_end": "2018-11-23 17:33:57",
            "total_fee": 100,
            "transaction_id": "2018112322001402501015842257",
            "user_order_no": "P387137821445425600"
        }
    # 第2次返回支付失败消息
    if qr_count == 4:
        print('第2次返回支付失败消息')
        # 输入密码时关闭密码框
        return {
            "code": "FAIL",
            "msg": "订单未支付",
            "pp_trade_no": "9878174162",
            "printType": 0,
            "sub_code": "NOTPAY|ORDER_CANCELED",
            "sub_msg": "订单未支付"
        }
    if qr_count == 10:
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
    # 请求体
    req = bottle.request.json
    print('设备账单查询请求body:\n' + str(req))
    return {
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "total_pay_amt": 5,
        "total_pay_count": 4,
        "total_refund_amt": 2,
        "total_refund_count": 2
    }


@bottle.route('/api/refund', method='POST')
def device_bill():
    # 测试不同场景flag
    global rf_count
    rf_count += 1
    # 请求体
    req = bottle.request.json
    print('退款请求body:\n' + str(req))

    if rf_count == 1:
        print('覆盖打印')
        return {
            "channel_type": "ONEPAY",
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "out_refund_no": "GR431686068318822912",
            "pay_type": "ALIPAY",
            "printType": 1,
            "receipt": "T3JkZXJObzogR1A0MzE2ODU5MDQ4NDI1MDA5MjgKVHJhbnNhY3Rpb25JZDogSjFBUDIwMTkwMzI2MTY1MjA5Mjc1ODU3ClRpbWU6IDIwMTktMDMtMjYgMTU6NTI6NDkKVG90YWxGZWU6IDMuMDAKUGF5RmVlOiAzLjAwCkRpc2NvdW50RmVlOiAwLjAwCkRldmljZU5vOiA0MTQwMTkwMjAwMTAwMDM2ClBheVR5cGU6IEFMSVBBWQpDdXN0b21lck5hbWU6IGZ6cW1kCgpSZWZ1bmRGZWU6IDMuMDAKUmVmdW5kTm86IEdSNDMxNjg2MDY4MzE4ODIyOTEyCgo=",
            "refundCurrency": "JPY",
            "refund_fee": req.get('refund_fee', ''),
            "time": "2019-03-26 15:52:47",
            "user_order_no": "GP431685904842500928"
        }
    if rf_count == 2:
        print('追加打印')
        return {
            "channel_type": "ONEPAY",
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "out_refund_no": "GR431686068318822912",
            "pay_type": "ALIPAY",
            "printType": 3,
            "receipt": "T3JkZXJObzogR1A0MzE2ODU5MDQ4NDI1MDA5MjgKVHJhbnNhY3Rpb25JZDogSjFBUDIwMTkwMzI2MTY1MjA5Mjc1ODU3ClRpbWU6IDIwMTktMDMtMjYgMTU6NTI6NDkKVG90YWxGZWU6IDMuMDAKUGF5RmVlOiAzLjAwCkRpc2NvdW50RmVlOiAwLjAwCkRldmljZU5vOiA0MTQwMTkwMjAwMTAwMDM2ClBheVR5cGU6IEFMSVBBWQpDdXN0b21lck5hbWU6IGZ6cW1kCgpSZWZ1bmRGZWU6IDMuMDAKUmVmdW5kTm86IEdSNDMxNjg2MDY4MzE4ODIyOTEyCgo=",
            "refundCurrency": "JPY",
            "refund_fee": req.get('refund_fee', ''),
            "time": "2019-03-26 15:52:47",
            "user_order_no": "GP431685904842500928"
        }
    return {
        "channel_type": "ONEPAY",
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "out_refund_no": "GR431686068318822912",
        "pay_type": "ALIPAY",
        "printType": 0,
        "receipt": "T3JkZXJObzogR1A0MzE2ODU5MDQ4NDI1MDA5MjgKVHJhbnNhY3Rpb25JZDogSjFBUDIwMTkwMzI2MTY1MjA5Mjc1ODU3ClRpbWU6IDIwMTktMDMtMjYgMTU6NTI6NDkKVG90YWxGZWU6IDMuMDAKUGF5RmVlOiAzLjAwCkRpc2NvdW50RmVlOiAwLjAwCkRldmljZU5vOiA0MTQwMTkwMjAwMTAwMDM2ClBheVR5cGU6IEFMSVBBWQpDdXN0b21lck5hbWU6IGZ6cW1kCgpSZWZ1bmRGZWU6IDMuMDAKUmVmdW5kTm86IEdSNDMxNjg2MDY4MzE4ODIyOTEyCgo=",
        "refundCurrency": "JPY",
        "refund_fee": req.get('refund_fee', ''),
        "time": "2019-03-26 15:52:47",
        "user_order_no": "GP431685904842500928"
    }


@bottle.route('/api/cancel/order', method='POST')
def device_bill():
    # 测试不同场景flag
    global co_count
    co_count += 1
    # 请求体
    req = bottle.request.json
    print('撤单请求body:\n' + str(req))
    if co_count == 1:
        print('订单已撤销')
        return {
            "code": "FAIL",
            "msg": "order already closed",
            "printType": 0,
            "sub_code": "ORDERCLOSED",
            "sub_msg": "order already closed"
        }
    if co_count == 2:
        print('订单不存在')
        return {
            "code": "FAIL",
            "msg": "order does not exist",
            "printType": 0,
            "sub_code": "ORDERCLOSED",
            "sub_msg": "order does not exist"
        }
    if co_count == 3:
        print('未知错误')
        return {
            "code": "FAIL",
            "sub_msg": "FAIL"
        }
    if co_count >= 4:
        print('订单撤销成功')
    return {
        "code": "SUCCESS",
        "msg": "SUCCESS"
    }


bottle.run(host='192.168.20.94', port=8885)
