# coding=utf-8
import bottle
import time

sc_count = 0
qr_count = 0
rf_count = 0
co_count = 0
bs_count = 0


@bottle.route('/api/scannedCode', method='POST')
def scanned():
    # 测试不同场景flag
    global sc_count
    sc_count += 1

    # 开始被扫支付测试
    if sc_count == 1:
        print('\n开始被扫支付异常测试\n')

    # 打印被扫请求体
    req = bottle.request.json
    print('支付请求body:\n' + str(req) + '\n')

    # 开始被扫支付测试
    if sc_count == 1:
        print('\n返回未定义的values')
        return {
            "buyer_pay_fee": 0,
            "channel_type": 0,
            "code": 0,
            "customer_name": 0,
            "msg": 0,
            "pay_type": 0,
            "pp_trade_no": 0,
            "printType": 'ERROR',
            "real_fee": 0,
            "receipt": 0,
            "time_end": 0,
            "total_fee": 'ERROR',
            "transaction_id": 0,
            "user_order_no": 0
        }
    if sc_count == 2:
        print('\n返回未定义的key')
        return {
            "ERROR": "ERROR"
        }
    if sc_count == 3:
        print('\n返回空json')
        return {}
    if sc_count == 4:
        print('\n返非json格式数据')
        return
    if sc_count == 5:
        print('\n返回500 error')
        print('1' + 1)
    # 测试轮询
    if sc_count >= 6:
        print('\n ')
        return {
            "code": "FAIL",
            "msg": "需要用户输入支付密码",
            "pp_trade_no": "18c041456160c9053006",
            "sub_code": "USERPAYING",
            "sub_msg": "需要用户输入支付密码"
        }


@bottle.route('/api/query/order', method='POST')
def query_order():
    global qr_count
    qr_count += 1
    # 轮询开始
    if qr_count == 1:
        print('\n订单轮询异常测试\n')
    # 打印轮询次数
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('\n第' + str(qr_count) + '轮询 ' + timestamp)
    # 打印查单接口请求body
    req = bottle.request.json
    print('订单状态请求body:\n' + str(req) + '\n')
    if qr_count == 1:
        print('\n返回未定义的values')
        return {
            "buyer_pay_fee": "ERROR",
            "channel_type": 1,
            "code": "ERROR",
            "customer_name": "ERROR",
            "msg": "ERROR",
            "pay_type": "ERROR",
            "pp_trade_no": "ERROR",
            "printType": "ERROR",
            "real_fee": "ERROR",
            "receipt": "ERROR",
            "time_end": "ERROR",
            "total_fee": "ERROR",
            "transaction_id": "ERROR",
            "user_order_no": "ERROR"
        }
    if qr_count == 2:
        print('\n返回未定义的key')
        return {
            "ERROR": "ERROR"
        }
    if qr_count == 3:
        print('\n返回空json')
        return {}
    if qr_count == 4:
        print('\n返非json格式数据')
        return
    if qr_count == 5:
        print('\n返回500 error')
        print('1' + 1)
    # 测试撤单
    if qr_count >= 6:
        return {
            "code": "FAIL",
            "msg": "需要用户输入支付密码",
            "pp_trade_no": "18c041456160c9053006",
            "sub_code": "test order cancel",
            "sub_msg": "需要用户输入支付密码"
        }


@bottle.route('/api/cancel/order', method='POST')
def cancel_order():
    # 测试不同场景flag
    global co_count
    co_count += 1

    # 开始撤单异常测试
    if co_count == 1:
        print('\n撤单接口异常测试')
    # 打印撤单请求体
    req = bottle.request.json
    print('撤单请求body:\n' + str(req) + '\n')
    
    if co_count == 1:
        print('\n返回未定义的values')
        return {
            "code": 1,
            "msg": 0,
            "printType": "ERROR",
            "sub_code": 0,
            "sub_msg": 0
        }
    if co_count == 2:
        print('\n返回未定义的key')
        return {
            "ERROR": "ERROR"
        }
    if co_count == 3:
        print('\n返回空json')
        return {}
    if co_count == 4:
        print('\n返非json格式数据')
        return
    if co_count == 5:
        print('\n返回500 error')
        print('1' + 1)
    if co_count == 6:
        print('订单已撤销')
        return {
            "code": "FAIL",
            "msg": "order already closed",
            "printType": 0,
            "sub_code": "ORDERCLOSED",
            "sub_msg": "order already closed"
        }
    if co_count == 7:
        print('订单不存在')
        return {
            "code": "FAIL",
            "msg": "order does not exist",
            "printType": 0,
            "sub_code": "ORDERCLOSED",
            "sub_msg": "order does not exist"
        }
    if co_count == 8:
        print('未知错误')
        return {
            "code": "FAIL",
            "sub_msg": "FAIL"
        }
    if co_count >= 9:
        print('订单撤销成功')
        return {
            "code": "SUCCESS",
            "msg": "SUCCESS"
        }


@bottle.route('/api/deviceBillSummary', method='POST')
def device_bill_summary():
    global bs_count
    bs_count += 1
    # 轮询开始
    if bs_count == 1:
        print('\n设备账单查询异常测试\n')
    # 打印设备账单查询请求body
    req = bottle.request.json
    print('设备账单查询请求body:\n' + str(req) + '\n')
    
    if bs_count == 1:
        print('\n返回未定义的values')
        return {
            "code": 0,
            "msg": 0,
            "total_pay_amt": 'error',
            "total_pay_count": 'error',
            "total_refund_amt": 'error',
            "total_refund_count": 'error'
        }
    if bs_count == 2:
        print('\n返回未定义的key')
        return {
            "ERROR": "ERROR"
        }
    if bs_count == 3:
        print('\n返回空json')
        return {}
    if bs_count == 4:
        print('\n返非json格式数据')
        return
    if bs_count == 5:
        print('\n返回500 error')
        print('1' + 1)
    if bs_count >= 6:
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
    # 退款异常测试开始
    if rf_count == 1:
        print('\n设备账单查询异常测试\n')
    # 打印退款请求body
    req = bottle.request.json
    print('设备账单查询请求body:\n' + str(req) + '\n')
    if rf_count == 1:
        print('\n返回未定义的values')
        return {
            "channel_type": 0,
            "code": 0,
            "msg": 0,
            "out_refund_no": 0,
            "pay_type": 0,
            "printType": 'ERROR',
            "receipt": 0,
            "refundCurrency": 0,
            "refund_fee": 'ERROR',
            "time": 0,
            "user_order_no": 0
        }
    if rf_count == 2:
        print('\n返回未定义的key')
        return {
            "ERROR": "ERROR"
        }
    if rf_count == 3:
        print('\n返回空json')
        return {}
    if rf_count == 4:
        print('\n返非json格式数据')
        return
    if rf_count == 5:
        print('\n返回500 error')
        print('1' + 1)
    if rf_count >= 6:
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


bottle.run(host='192.168.20.94', port=8885)
