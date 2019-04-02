# coding=utf-8
import bottle


@bottle.route('/api/scannedCode', method='POST')
def scanned():

    return {
        "bid_currency":"JPY",
        "buyer_pay_fee":"300",
        "channel_type":"ONEPAY",
        "code":"SUCCESS",
        "customer_name":"fzqmd",
        "msg":"SUCCESS",
        "pay_currency":"JPY",
        "pay_type":"ALIPAY",
        "pp_trade_no":"15535867268514532P",
        "printType":0,
        "real_fee":"300",
        "settlement_currency":"JPY",
        "time_end":"2019-03-26 15:52:10",
        "total_fee":300,
        "transaction_id":"J1AP20190326165209275857",
        "user_order_no":"GP431685904842500928"
    }


@bottle.route('/api/refund', method='POST')
def scanned():

    return {
        "channel_type":"ALIPAY_GLOBAL",
        "code":"SUCCESS",
        "msg":"SUCCESS",
        "out_refund_no":"GR431667973693325568",
        "pay_type":"ALIPAY",
        "printType":0,
        "receipt":"T3JkZXJObzogR1A0MzE2Njc1MzAzNTkyMTU2ODAKVHJhbnNhY3Rpb25JZDogMjAxOTAzMjYyMjAwMTQwMjUwMDU2MzcyNzkxOApUaW1lOiAyMDE5LTAzLTI2IDE0OjQwOjUzClRvdGFsRmVlOiAzLjAwClBheUZlZTogMC4xOApEaXNjb3VudEZlZTogMi44MgpEZXZpY2VObzogMjIxMTE2MDkwMDAwNTg2NQpQYXlUeXBlOiBBTElQQVkKQ3VzdG9tZXJOYW1lOiBmenFtZAoKUmVmdW5kRmVlOiAzLjAwClJlZnVuZE5vOiBHUjQzMTY2Nzk3MzY5MzMyNTU2OAoK",
        "refundCurrency":"JPY",
        "refund_fee":300,
        "time":"2019-03-26 14:40:52",
        "user_order_no":"GP431667530359215680"
    }


bottle.run(host='10.10.44.56', port=8885)
