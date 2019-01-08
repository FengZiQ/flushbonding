# coding=utf-8
import bottle


@bottle.route('/scannedCode', method='POST')
def scanned():

    return {
        "code": "FAIL",
        "msg": "需要用户输入支付密码",
        "pp_trade_no": "18c041456160c9053006",
        "sub_code": "USERPAYING",
        "sub_msg": "需要用户输入支付密码"
    }


bottle.run(host='192.168.20.94', port=8883)
