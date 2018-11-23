# coding=utf-8
import sys
import re
import pyautogui
import time


class TextArea(object):
    def __init__(self):
        self.buffer = []

    def write(self, *args):
        self.buffer.append(args)


# 找到窗体坐标
def get_coordinate(window):
    coordinate = {}
    try:
        stdout = sys.stdout
        sys.stdout = TextArea()
        window.print_ctrl_ids()
        text_area, sys.stdout = sys.stdout, stdout
        temp = text_area.buffer[2][0]
        # (L349, T75, R1271, B857)   (L-8, T-8, R1928, B1048)
        if 'L-' in temp:
            coordinate['left'] = int(re.findall('\(L-(\d+), T', temp)[0])
        else:
            coordinate['left'] = int(re.findall('\(L(\d+), T', temp)[0])
        if 'T-' in temp:
            coordinate['top'] = int(re.findall('T-(\d+), R', temp)[0])
        else:
            coordinate['top'] = int(re.findall('T(\d+), R', temp)[0])
        coordinate['right'] = int(re.findall('R(\d+), B', temp)[0])
        coordinate['bottom'] = int(re.findall('B(\d+)\)\n', temp)[0])
    except Exception as e:
        print('坐标定位失败！')
        print(e)

    return coordinate


# 点击操作
def click_action(window, left, top):
    try:
        wcl = get_coordinate(window)
        if wcl:
            pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
            pyautogui.click()
            time.sleep(2)
        return
    except Exception as e:
        print(e)
        print('点击操作点击操作失败')


# 填充文本框操作
def fill_in_text(window, left, top, text):
    try:
        wcl = get_coordinate(window)
        if wcl:
            pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
            pyautogui.click()
            # 清空焦点所在区域的文本
            pyautogui.hotkey('ctrlleft', 'a')
            pyautogui.press('delete')
            pyautogui.typewrite(text)
            time.sleep(1)
        return
    except Exception as e:
        print(e)
        print('填充文本框操作失败')

