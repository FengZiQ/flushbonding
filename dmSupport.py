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
        dm_session.close()
        return result
    except:
        to_log('\n获取设备属性失败\n')
        return {}


# 获取升级包信息
def get_upgrade_package_info(name, version):
    try:
        res = dm_session.get(
            configuration['dmServer']+'upgradePackage/pageList?softName='+name+'&version='+version
        )
        temp = json.loads(res.text)['data']['list'][0]
        dm_session.close()
        return temp
    except:
        to_log('获取升级包信息失败')
        return None


# 设备升级
def send_upgrade_cmd(device_no,upgrade_id):
    dm_session.post(
        configuration['dmServer'] + 'device/upgradeEx/edit',
        json={
            "code": "firmware",
            "deviceNoList": [str(device_no)],
            "upgradeInfoList": [{"upgradeId": str(upgrade_id)}]
        }
    )
    dm_session.close()
    return None


# 获取设备信息
def get_device_info(device_no):
    try:
        res = dm_session.get(
            configuration['dmServer'] + 'deviceSale/pageList?connectState=0&operateType=customer&serialNum=' + device_no
        )
        temp = json.loads(res.text)
        device_info = temp['data']['list'][0]
        dm_session.close()
        return device_info
    except:
        to_log('获取设备信息失败')
        return {}


# 获取服务商信息
def customer_info(customer_name):
    cus_info = {}
    try:
        res = dm_session.get(
            configuration['dmServer'] + 'customer/pageList?salesName=sadmin&name=' + customer_name
        )
        temp0 = json.loads(res.text)
        temp1 = temp0['data']['list']
        for c in temp1:
            if c.get('name', '') == customer_name:
                cus_info = c

        dm_session.close()
    except:
        to_log('获取服务商信息失败')

    return cus_info


# 获取参数配置信息
def get_para_config(config_name):
    try:
        res = dm_session.get(
            configuration['dmServer']+'payChannelConfig/pageList?description='+config_name
        )
        temp = json.loads(res.text)
        config_info = temp['data']['list'][0]
        dm_session.close()
        return config_info
    except:
        return {}


# 给非默认参数配置绑定设备
def bind_device_for_para_config(pay_channel_id, device_id, device_no):
    try:
        dm_session.post(
            configuration['dmServer'] + 'editDeviceBindChannel/modify',
            json={
                "payChannelId": pay_channel_id,
                "deviceIds": [device_id],
                "deviceNos": [device_no]
            }
        )
        dm_session.close()
    except:
        to_log('给非默认参数配置绑定设备失败')


# 参数配置下发
def issue_para_config(pay_channel_id, device_id, device_no, cus_id):
    try:
        dm_session.post(
            configuration['dmServer'] + 'editDeviceUnBindChannel/modify',
            json={
                "payChannelId": str(pay_channel_id),
                "deviceIds": [str(device_id)],
                "deviceNos": [device_no],
                "operateType": "singleEdit",
                "customerId": str(cus_id)
            }
        )
        dm_session.close()
    except:
        to_log('参数配置下发失败')


# 获取自定义通用配置信息
def get_self_common_config_id(config_name):
    try:
        res = dm_session.get(
            configuration['dmServer'] + 'paramListConfig/pageList?name=' + config_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        dm_session.close()
        return config_id
    except:
        to_log('获取自定义通用配置信息失败')
        return {}


# 自定义通用配置绑定解绑设备: action_type=1为绑定，=0为解绑
def device_and_self_common_config(self_cc_id, action_type, device_id, device_no):
    try:
        dm_session.post(
            configuration['dmServer'] + 'deviceIsBindParamList/modify',
            json={
                "paramListId": str(self_cc_id),
                "deviceIds": [str(device_id)],
                "serialNums": [str(device_no)],
                "type": action_type
            }
        )
        dm_session.close()
    except:
        to_log('自定义通用配置绑定(解绑)设备失败')
        return {}


# 自定义通用配置下发
def user_defined_config(config_id, device_id, device_no):
    try:
        dm_session.post(
            configuration['dmServer'] + 'deviceIsBindParamList/modify',
            json={
                "paramListId": str(config_id),
                "deviceIds": [str(device_id)],
                "serialNums": [device_no],
                "type": "2"
            }
        )
        dm_session.close()
    except:
        to_log('自定义通用配置下发失败')


if __name__ == "__main__":
    print(get_device_info('4113180400130999'))

