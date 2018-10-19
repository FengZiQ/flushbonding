# coding=utf-8
import json
import time
from to_log import to_log
from login_dm import login_api
from configFile import configuration


dm_session = login_api()


# 设备属性上传
def upload_device_attribute():
    dm_session.post(
        configuration['dmServer'] + 'device/flushConfig/edit',
        json=int(configuration['netDeviceNo'])
    )


# 获取设备属性
def get_device_attribute():
    upload_device_attribute()
    time.sleep(5)
    try:
        res = dm_session.get(
            configuration['dmServer']+'device/getConfig/query?deviceNo='+configuration['netDeviceNo']
        )
        temp = json.loads(res.text)['data']['data']
        return json.loads(temp)['time']
    except:
        to_log('\n获取设备属性失败\n')


if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())))
    print(get_device_attribute())

