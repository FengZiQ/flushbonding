# coding=utf-8
import os
import time


def auto_backups(file_list=list(), size=1024000):
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    for file in file_list:
        file_size = os.path.getsize(file)
        print(file_size)
        if file_size > size and '/' in file:
            file_name = file.split('/')[-1]
            path = file.replace(file_name, '')

            os.system('mv ' + file + ' ' + path + timestamp + '_' + file_name)
            os.system('touch ' + file)
        elif file_size > size:
            os.system('mv ' + file + ' ' + timestamp + '_' + file)
            os.system('touch ' + file)

    return None


def manual_backups(file_list=list()):
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    for file in file_list:
        if '/' in file:
            file_name = file.split('/')[-1]
            path = file.replace(file_name, '')

            os.system('mv ' + file + ' ' + path + timestamp + '_' + file_name)
            os.system('touch ' + file)
        else:
            os.system('mv ' + file + ' ' + timestamp + '_' + file)
            os.system('touch ' + file)

    return None


if __name__ == "__main__":
    auto_backups(
        [
            '/home/qa/script/paymentStressTest/nohup.out',
            '/home/qa/script/paymentStressTest/paymentStressTest.log',
            '/home/qa/script/successRateOfUpgrade/testLog.log'
        ],
        size=512000
    )