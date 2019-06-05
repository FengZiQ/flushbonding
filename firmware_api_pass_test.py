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
        if sc_count == 6:
            print('\n被扫支付测试')
        if sc_count >= 7:
            print('支付请求body:\n' + str(req) + '\n')
        # 前3次被扫支付触发轮询
        if sc_count <= 5:
            return {
                "code": "FAIL",
                "msg": "需要用户输入支付密码",
                "pp_trade_no": "18c041456160c9053006",
                "sub_code": "USERPAYING",
                "sub_msg": "需要用户输入支付密码"
            }
        return {
            "buyer_pay_fee":str(req.get('total_fee', '')),
            "channel_type":"WXPAY",
            "code":"SUCCESS",
            "customer_name":"sh1m1子",
            "msg":"SUCCESS",
            "pay_type":"WXPAY",
            "pp_trade_no":"15561771177476001P",
            "printType":1,
            "real_fee": str(req.get('total_fee', '')),
            "receipt":"tqm1pbHgusU6IDQyMDAwMDAzMTYyMDE5MDQyNTg5MDIwODE1OTEKvbvS18qxvOQ6IDIwMTktMDQtMjUgMTU6MjU6MjcK19y98LbuOiAwLjAxCsq1uLa98LbuOiAwLjAxCtPFu9298LbuOiAwLjAwCsnosbix4LrFOiA0MTEzMTgwNDAwMTMwOTk5Cr270tfA4NDNOiDOotDFCsnMu6fD+7PGOiBzaDFtMdfTCrK7ss7T69PFu9298LbuOiAwLjAwCgoK",
            "time_end":"2019-04-25 15:25:25",
            "total_fee":req.get('total_fee', ''),
            "transaction_id":"4200000316201904258902081591",
            "user_order_no":"P442550801724158976"
        }
    except Exception as e:
        print(e)
        return {
        }


@bottle.route('/api/query/order', method='POST')
def query_order():
    global qr_count
    qr_count += 1
    # 轮询开始
    if qr_count == 1:
        print('\n订单轮询测试\n')
    # 打印轮询次数
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('\n第' + str(qr_count) + '轮询 ' + timestamp)
    # 打印查单接口请求body
    req = bottle.request.json
    print('订单状态请求body:\n' + str(req) + '\n')
    # 第2次返回支付成功消息
    if qr_count == 2:
        print('第2次返回支付成功消息')
        return {
            "buyer_pay_fee":"100",
            "channel_type":"WXPAY",
            "code":"SUCCESS",
            "customer_name":"sh1m1子",
            "msg":"SUCCESS",
            "pay_type":"WXPAY",
            "pp_trade_no":"15561771177476001P",
            "printType":1,
            "real_fee":"100",
            "receipt":"tqm1pbHgusU6IDQyMDAwMDAzMTYyMDE5MDQyNTg5MDIwODE1OTEKvbvS18qxvOQ6IDIwMTktMDQtMjUgMTU6MjU6MjcK19y98LbuOiAwLjAxCsq1uLa98LbuOiAwLjAxCtPFu9298LbuOiAwLjAwCsnosbix4LrFOiA0MTEzMTgwNDAwMTMwOTk5Cr270tfA4NDNOiDOotDFCsnMu6fD+7PGOiBzaDFtMdfTCrK7ss7T69PFu9298LbuOiAwLjAwCgoK",
            "time_end":"2019-04-25 15:25:25",
            "total_fee":100,
            "transaction_id":"4200000316201904258902081591",
            "user_order_no":"P442550801724158976"
        }
    # 轮询时，订单查询接口第三方接口返回的错误消息
    if qr_count == 3:
        print('第1次轮询时返回失败，但原因不详,此时发起撤单')
        return {
            "code": "FAIL",
            "msg": "UNKNOW ERROR",
            "pp_trade_no": "9878174162",
            "printType": 0,
            "sub_code": "UNKNOW ERROR",
            "sub_msg": "UNKNOW ERROR"
        }
    # 第2次返回支付失败消息
    if qr_count == 5:
        print('第2次返回订单支付失败消息，停止轮询，不发起撤单')
        # 输入密码时关闭密码框
        return {
            "code": "FAIL",
            "msg": "订单未支付",
            "pp_trade_no": "9878174162",
            "printType": 0,
            "sub_code": "NOTPAY|ORDER_CANCELED",
            "sub_msg": "订单未支付"
        }
    if qr_count >= 6 or qr_count == 4:
        return {
            "code": "FAIL",
            "msg": "需要用户输入支付密码",
            "pp_trade_no": "18c041456160c905300",
            "sub_code": "USERPAYING",
            "sub_msg": "需要用户输入支付密码"
        }


@bottle.route('/api/cancel/order', method='POST')
def cancel_order():
    # 打印撤单请求体
    req = bottle.request.json
    print('撤单请求body:\n' + str(req) + '\n')
    return {
        "code": "SUCCESS",
        "msg": "SUCCESS"
    }


@bottle.route('/api/deviceBillSummary', method='POST')
def device_bill_summary():
    # 打印设备账单查询请求体
    req = bottle.request.json
    print('设备账单查询请求body:\n' + str(req) + '\n')
    return {
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "total_pay_amt": 999999900,
        "total_pay_count": 4,
        "total_refund_amt": 900,
        "total_refund_count": 2
    }


@bottle.route('/api/refund', method='POST')
def refund():
    # 测试不同场景flag
    global rf_count
    rf_count += 1
    # 打印退款请求体
    req = bottle.request.json
    print('退款请求body:\n' + str(req) + '\n')

    if rf_count == 1:
        print('覆盖打印')
        return {
            "channel_type": "WXPAY",
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "out_refund_no": "GR437099612317680896",
            "pay_type": "WXPAY",
            "printType": 1,
            "refund_fee": req.get('refund_fee', 100),
            "time": "2019-04-10 13:24:16",
            "user_order_no": "GP437098913521119040",
            "receipt": "T3JkZXJObzogR1A0MzE2ODU5MDQ4NDI1MDA5MjgKVHJhbnNhY3Rpb25JZDogSjFBUDIwMTkwMzI2MTY1MjA5Mjc1ODU3ClRpbWU6IDIwMTktMDMtMjYgMTU6NTI6NDkKVG90YWxGZWU6IDMuMDAKUGF5RmVlOiAzLjAwCkRpc2NvdW50RmVlOiAwLjAwCkRldmljZU5vOiA0MTQwMTkwMjAwMTAwMDM2ClBheVR5cGU6IEFMSVBBWQpDdXN0b21lck5hbWU6IGZ6cW1kCgpSZWZ1bmRGZWU6IDMuMDAKUmVmdW5kTm86IEdSNDMxNjg2MDY4MzE4ODIyOTEyCgo="
        }
    if rf_count == 2:
        print('追加打印')
        return {
            "channel_type": "WXPAY",
            "code": "SUCCESS",
            "msg": "SUCCESS",
            "out_refund_no": "GR437099612317680896",
            "pay_type": "WXPAY",
            "printType": 2,
            "refund_fee": req.get('refund_fee', 100),
            "time": "2019-04-10 13:24:16",
            "user_order_no": "GP437098913521119040",
            "receipt": "T3JkZXJObzogR1A0MzE2ODU5MDQ4NDI1MDA5MjgKVHJhbnNhY3Rpb25JZDogSjFBUDIwMTkwMzI2MTY1MjA5Mjc1ODU3ClRpbWU6IDIwMTktMDMtMjYgMTU6NTI6NDkKVG90YWxGZWU6IDMuMDAKUGF5RmVlOiAzLjAwCkRpc2NvdW50RmVlOiAwLjAwCkRldmljZU5vOiA0MTQwMTkwMjAwMTAwMDM2ClBheVR5cGU6IEFMSVBBWQpDdXN0b21lck5hbWU6IGZ6cW1kCgpSZWZ1bmRGZWU6IDMuMDAKUmVmdW5kTm86IEdSNDMxNjg2MDY4MzE4ODIyOTEyCgo="
        }
    return {
        "channel_type": "WXPAY",
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "out_refund_no": "GR437099612317680896",
        "pay_type": "WXPAY",
        "printType": 0,
        "refund_fee": req.get('refund_fee', 100),
        "time": "2019-04-10 13:24:16",
        "user_order_no": "GP437098913521119040"
    }


bottle.run(host='192.168.1.100', port=8881)
