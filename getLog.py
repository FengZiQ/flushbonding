# coding=utf-8
import time
from viewLog import view_log
from configFile import configuration
from scannedCode import scanned_code


# log是否触发
def log_content():
    # 获取时间戳
    timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_path = '/data/log/' + timestamp + '/payment-pay-api/'
    cmd = 'tail -n 10 ' + log_path + 'payment-pay-api.0.log | grep "' + configuration['scanDeviceNo'] + '"'
    log_text = {'lc': view_log('sp1t', cmd)}
    if len(log_text['lc']) <= len(cmd)+5:
        log_text['lc'] = view_log('sp2t', cmd)
    # 给log末尾追加内容
    scanned_code()
    return log_text


if __name__ == "__main__":
    print(log_content()['lc'])
    print(log_content()['lc'])
