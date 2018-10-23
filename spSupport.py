# coding=utf-8
import json
import time
from to_log import to_log
from login_sp import login_sp_api
from configFile import configuration


sp_session = login_sp_api()


# 获取设备属性
def verbose_payment(device_no):
    timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    url = 'order/pageList?customerId=5130&treeId=00010025002800010001&' + \
          'startDate=' + timestamp + '&endDate=' + timestamp +\
          '&payStatus=4&serialNum=' + device_no
    try:
        res = sp_session.get(
            configuration['spServer'] + url
        )
        temp = json.loads(res.text)['data']['list']
        return temp
    except:
        to_log('\n获取设备属性失败\n')
        return {}


if __name__ == "__main__":
    print(verbose_payment('4113180400130999'))

