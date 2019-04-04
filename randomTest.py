# coding=utf-8
import bottle


@bottle.route('/api/scannedCode', method='POST')
def scanned():
    req = bottle.request.json
    print('撤单请求body:\n' + str(req))
    return {
        "bid_currency": "JPY",
        "buyer_pay_fee": "300",
        "channel_type": "ONEPAY",
        "code": "SUCCESS",
        "customer_name": "fzqmd",
        "msg": "SUCCESS",
        "pay_currency": "JPY",
        "pay_type": "ALIPAY",
        "pp_trade_no": "15535867268514532P",
        "printType": 0,
        "real_fee": "300",
        "settlement_currency": "JPY",
        "time_end": "2019-03-26 15:52:10",
        "total_fee": req.get("total_fee", 0),
        "transaction_id": "J1AP20190326165209275857",
        "user_order_no": "GP431685904842500928"
    }


@bottle.route('/api/refund', method='POST')
def scanned():
    req = bottle.request.json
    print('撤单请求body:\n' + str(req))
    return {
        "channel_type": "ALIPAY_GLOBAL",
        "code": "SUCCESS",
        "msg": "SUCCESS",
        "out_refund_no": "GR431667973693325568",
        "pay_type": "ALIPAY",
        "printType": 0,
        "receipt": "T3JkZXJObzogR1A0MzE2Njc1MzAzNTkyMTU2ODAKVHJhbnNhY3Rpb25JZDogMjAxOTAzMjYyMjAwMTQwMjUwMDU2MzcyNzkxOApUaW1lOiAyMDE5LTAzLTI2IDE0OjQwOjUzClRvdGFsRmVlOiAzLjAwClBheUZlZTogMC4xOApEaXNjb3VudEZlZTogMi44MgpEZXZpY2VObzogMjIxMTE2MDkwMDAwNTg2NQpQYXlUeXBlOiBBTElQQVkKQ3VzdG9tZXJOYW1lOiBmenFtZAoKUmVmdW5kRmVlOiAzLjAwClJlZnVuZE5vOiBHUjQzMTY2Nzk3MzY5MzMyNTU2OAoK",
        "refundCurrency": "JPY",
        "refund_fee": req.get('refund_fee', ''),
        "time": "2019-03-26 14:40:52",
        "user_order_no": "GP431667530359215680"
    }


bottle.run(host='10.10.44.56', port=8885)
