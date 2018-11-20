# coding=utf-8
import json
import time
from to_log import to_log
from login_sp import login_sp_api
from configFile import configuration


sp_session = login_sp_api()


# 获取商户信息
def get_merchant_info(merchant_name, m_type):
    m_info = None
    mt = None
    if m_type == '门店':
        mt = 3
    elif m_type == '商户':
        mt = 2
    else:
        print('输入的商户类型不正确！！！')
    try:
        res = sp_session.get(
            configuration['spServer'] + 'customer/keyTree/query?abb='+merchant_name
        )
        temp = json.loads(res.text)['data']
        for m in temp:
            if m.get('abb', '') == merchant_name and m.get('type', '') == mt:
                m_info = m
                break
        return m_info
    except:
        to_log('获取门店信息失败\n')
        return {}


# 支付明细列表
def verbose_payment(merchant_name, m_type, device_no):
    timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    m_info = get_merchant_info(merchant_name, m_type)
    try:
        url = 'order/pageList?customerId=' + str(m_info.get('id', '')) + '&treeId=' + m_info.get('treeId', '') + \
              '&startDate=' + timestamp + '&endDate=' + timestamp + \
              '&payStatus=0&pageIndex=1&pageSize=300&serialNum=' + device_no
        res = sp_session.get(
            configuration['spServer'] + url
        )
        temp = json.loads(res.text)['data']['list']
        return temp
    except:
        to_log('获取支付明细列表失败\n')
        return {}


if __name__ == "__main__":
    print(verbose_payment('sh1m1子', '门店', '4113180400130999'))

