# coding=utf-8
import bottle
import time

sc_count = 0
qr_count = 0
rf_count = 0
co_count = 0


@bottle.route('/api/scannedCode', method='POST')
def scanned():
    # 请求体
    req = bottle.request.json
    print('支付请求body:\n' + str(req) + '\n')
    # return {
    #     "code": "FAIL",
    #     "msg": "需要用户输入支付密码",
    #     "pp_trade_no": req.get('pp_trade_no', ''),
    #     "sub_code": "USERPAYING",
    #     "sub_msg": "需要用户输入支付密码"
    # }
    return {
        "buyer_pay_fee":"1",
        "channel_type":"WXPAY",
        "code":"SUCCESS",
        "customer_name":"sh1m1子",
        "msg":"SUCCESS",
        "pay_type":"WXPAY",
        "pp_trade_no":"15561771177476001P",
        "printType":1,
        "real_fee":"1",
        "receipt":"tqm1pbHgusU6IDQyMDAwMDAzMTYyMDE5MDQyNTg5MDIwODE1OTEKvbvS18qxvOQ6IDIwMTktMDQtMjUgMTU6MjU6MjcK19y98LbuOiAwLjAxCsq1uLa98LbuOiAwLjAxCtPFu9298LbuOiAwLjAwCsnosbix4LrFOiA0MTEzMTgwNDAwMTMwOTk5Cr270tfA4NDNOiDOotDFCsnMu6fD+7PGOiBzaDFtMdfTCrK7ss7T69PFu9298LbuOiAwLjAwCgoK",
        "time_end":"2019-04-25 15:25:25",
        "total_fee": req.get('total_fee', ''),
        "transaction_id":"4200000316201904258902081591",
        "user_order_no":"P442550801724158976"
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

    return {
        # "code": "FAIL",
        "msg": "需要用户输入支付密码",
        "pp_trade_no": req.get('pp_trade_no', ''),
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


bottle.run(host='192.168.1.100', port=8881)
