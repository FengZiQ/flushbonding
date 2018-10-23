# coding=utf-8
import json
import time
from to_log import to_log
from login_dm import login_api
from configFile import configuration


dm_session = login_api()


# 设备属性上传
def upload_device_attribute(device_no):
    dm_session.post(
        configuration['dmServer'] + 'device/flushConfig/edit',
        json=int(device_no)
    )


# 获取设备属性
def get_device_attribute(device_no):
    upload_device_attribute(device_no)
    time.sleep(5)
    try:
        res = dm_session.get(
            configuration['dmServer']+'device/getConfig/query?deviceNo='+device_no
        )
        temp = json.loads(res.text)['data']['data']
        result = json.loads(temp)
        return result
    except:
        to_log('\n获取设备属性失败\n')
        return {}


# 设备升级
def send_upgrade_cmd(upgrade_id):
    dm_session.post(
        configuration['dmServer'] + 'device/upgradeEx/edit',
        json={
            "code": "firmware",
            "deviceNoList": [configuration['upgradeDeviceNo']],
            "upgradeInfoList": [{"upgradeId": str(upgrade_id)}]
        }
    )
    return None


if __name__ == "__main__":
    print(get_device_attribute(configuration['upgradeDeviceNo']).get('time', '获取时间失败'))
    print(get_device_attribute(configuration['upgradeDeviceNo']).get('time', '获取时间失败'))

