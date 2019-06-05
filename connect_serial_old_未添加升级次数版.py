# coding=utf-8
import serial
import time

try:
    ser = serial.Serial(
        port='COM3',
        baudrate=115200,
        timeout=5
    )
except serial.serialutil.SerialException:
    ser = None


def login():
    com_output('')#发送空,使出现用户名、密码提示(相当于鼠标点击+回车)
    com_output('root')#login: 提示符后输入‘root’
    com_output('Ins2018pos')#Password: 提示符后输入密码‘Ins2018pos’


def com_output(cmd, end_receipt_word='', end_receipt_time=0):
    try:
        ser.write((cmd+'\n').encode())
    except AttributeError:
        print('串口连接失败，请检查串口在系统中是否可识别')
    else:
        with open('update.log', 'a+', encoding='utf-8') as write_f:
            while True:
                if ser.inWaiting():
                    data = ser.read(500).decode()
                    if 'login:' in data or 'Password:' in data or 'Inspiry:~#' in data:
                        # print(data)
                        break
                    print('-'*16+data+'+'*16)
                    print('开始写入咯')
                    write_f.write(data)
            time.sleep(1)


if __name__ == '__main__':

    while True:
        try:
            ser = serial.Serial(
                port='COM3',
                baudrate=115200,
                timeout=5
            )
        except serial.serialutil.SerialException:
            ser = None
        try:
            login()
            com_output('logcat', end_receipt_time=10)
        except:
            print('重启中请稍后'+'.'*66)
            time.sleep(40)














