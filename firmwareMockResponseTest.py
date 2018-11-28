# coding=utf-8
import time
from pywinauto import Desktop
from to_log import to_log
from findCoordinate import *
from configFile import configuration


window = Desktop(backend="uia").window(title=u'Progress Telerik Fiddler Web Debugger')
# window.print_ctrl_ids()


def flag():
    f = False
    try:
        if window.child_window(title=u"Run to Completion").Exists:
            f = True
    except:
        pass
    return f


# 被扫接口mock数据
def mock_scanned_code_api():
    i = 1
    while True:
        if i == 64:
            break
        # 点击第一行请求
        click_action(window, left=30, top=93)
        time.sleep(1)
        if flag():
            f = open(configuration['mockDataPath'] + str(i) + '.txt')
            res = f.read()
            f.close()
            # 替换Response
            fill_in_text(
                window,
                left=1776,
                top=900,
                text=res
            )
            # 点击Run to Completion
            cw = window.child_window(title=u"Run to Completion")
            click_action(cw, left=1, top=1)
            to_log('文件：' + str(i) + '.txt已测试\n')
            i += 1
        # 清掉旧的请求
        click_action(window, left=30, top=110)
        pyautogui.press('delete')

    return None


# 退款接口mock数据
def mock_refund_api():
    i = 1
    while True:
        if i == 15:
            break
        # 点击第一行请求
        click_action(window, left=30, top=93)
        time.sleep(1)
        if flag():
            f = open(configuration['mockDataPath'] + 'refund' + str(i) + '.txt')
            res = f.read()
            f.close()
            # 替换Response
            fill_in_text(
                window,
                left=1776,
                top=900,
                text=res
            )
            # 点击Run to Completion
            cw = window.child_window(title=u"Run to Completion")
            click_action(cw, left=1, top=1)
            to_log('文件：' + 'refund' + str(i) + '.txt已测试\n')
            i += 1
        # 清掉旧的请求
        click_action(window, left=30, top=110)
        pyautogui.press('delete')

    return None


if __name__ == "__main__":
    mock_scanned_code_api()
    # mock_refund_api()
