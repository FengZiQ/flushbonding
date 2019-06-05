# coding=utf-8
# 实现串口连接成功后向设备发送命令、接受输出
import serial
import time
import base64
from to_log import to_log

s1 = 'cm9vdA=='
s2 = 'SW5zMjAxOHBvcw=='

try:
    ser = serial.Serial(
        port='COM3',
        baudrate=115200,
        timeout=5
    )
except serial.serialutil.SerialException:
    ser = None


def begin():
    data = execute_cmd('')
    print(data)
    if 'login:' in data or 'Login incorrect' in data:
        execute_cmd((base64.b64decode(s1)).decode())
        execute_cmd((base64.b64decode(s2)).decode())
    elif 'Password:' in data:
        execute_cmd('')
        execute_cmd((base64.b64decode(s1)).decode())
        execute_cmd((base64.b64decode(s2)).decode())
    elif '@Inspiry:~#' in data:
        pass
    else:
        to_log('begin failed', file='serial.log')


def execute_cmd(cmd):
    # 命令执行完，输出结果相对少时使用此方法
    data = ''
    try:
        ser.write((cmd+'\n').encode())
    except AttributeError:
        to_log('串口连接失败，请检查串口在系统中是否可识别', file='serial.log')
    else:
        while True:
            if ser.inWaiting():
                data += ser.read(128).decode()
                if 'login:' in data or 'Password:' in data or 'Inspiry:~#' in data:
                    break
                time.sleep(1)
    if 'root' not in data:
        to_log(data, file='serial.log')
    return data


def receipt_more(cmd, end_receipt_word='结束关键字', end_receipt_time=0):
    # 命令执行完，输出结果相对长时使用此方法
    # end_receipt_word--->结束关键字
    # end_receipt_time--->结束时间，单位为：s
    data = ''
    receive_count = 0
    try:
        ser.write((cmd+'\n').encode())
    except AttributeError:
        to_log('串口连接失败，请检查串口在系统中是否可识别', file='serial.log')
    else:
        while True:
            if ser.inWaiting():
                data += ser.read(2000).decode()
                if 'login:' in data or 'Password:' in data or 'Inspiry:~#' in data:
                    to_log(data, file='serial.log')
                    break
                time.sleep(1)
                receive_count += 1
                if end_receipt_time == receive_count:
                    break
                if end_receipt_word in data:
                    break

    to_log(data, file='serial.log')
    return data


if __name__ == '__main__':
    # pass
    begin()
    execute_cmd('logcat -c')
    receipt_more('logcat', end_receipt_word='Inspiry login:')






