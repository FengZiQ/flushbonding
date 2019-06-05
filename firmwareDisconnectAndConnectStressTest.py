# coding=utf-8
import time
from to_log import to_log
from honorRouter import Configuration

rc = Configuration()

count = 0
while True:
    count += 1
    to_log('第' + str(count) + '断网')
    # 重新登录路由器管理后台
    rc.re_login()
    # 断网：通过改变路由器密码
    rc.wc(name='QA', pwd='123456789', secure=2)
    # 断网后等待1min
    time.sleep(60)

    # 重新登录路由器管理后台
    rc.re_login()
    rc.wc(name='QA', pwd='12345678', secure=2)
    # 网络恢复后等待1min
    time.sleep(60)

    if count == 2160:
        break

