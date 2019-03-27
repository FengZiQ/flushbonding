# coding=utf-8
import bottle


@bottle.route('/api/scannedCode', method='POST')
def scanned():

    return {

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


bottle.run(host='10.10.11.131', port=8885)
