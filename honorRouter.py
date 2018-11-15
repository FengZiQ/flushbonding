# coding=utf-8
from selenium import webdriver
from time import sleep
from to_log import to_log


class Configuration(object):

    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.get('http://192.168.233.1/html/index.html')
            sleep(3)
            self.driver.find_element_by_id('userpassword').send_keys('inspiry123')
            self.driver.find_element_by_id('loginbtn').click()
            sleep(3)
        except:
            to_log('请确认电脑是否连接了华为的路由器；如果连接，请确认路由器的管理地址是否为192.168.233.1')

    # WiFi名字、密码、加密方式设置(secure:'1 is not pwd;2 is WPA2;other is mixed')
    def wc(self, name, pwd, secure, ssid=False):
        try:
            self.driver.find_element_by_class_name('want_wifi').click()
            sleep(3)
            self.driver.find_element_by_id('content_wifi_name2G_ctrl').clear()
            self.driver.find_element_by_id('content_wifi_name2G_ctrl').send_keys(name)
            self.driver.find_element_by_id('wifi_secopt2G_ctrl_selectlist_parenselect').click()
            sleep(1)
            if secure == 1:
                self.driver.find_element_by_id('None_BigSelectBoxItemID').click()
                sleep(1)
            elif secure == 2:
                self.driver.find_element_by_id('11i_BigSelectBoxItemID').click()
                sleep(1)
                self.driver.find_element_by_id('content_wifi_password2G_ctrl').clear()
                self.driver.find_element_by_id('content_wifi_password2G_ctrl').send_keys(pwd)
            else:
                self.driver.find_element_by_id('WPAand11i_BigSelectBoxItemID').click()
                sleep(1)
                self.driver.find_element_by_id('content_wifi_password2G_ctrl').clear()
                self.driver.find_element_by_id('content_wifi_password2G_ctrl').send_keys(pwd)

            self.driver.find_element_by_id('SsidSettings_submitbutton').click()
            sleep(5)
            if ssid:
                self.ssid_set()
            return True
        except:
            to_log('WiFi设置Failed')
            return False

    # WiFi信道设置
    def channel_set(self, channel=0):
        try:
            if channel == 1:
                self.driver.find_element_by_class_name('want_more').click()
                sleep(3)
                self.driver.find_element_by_id('wifiadvancesetparent_menuId').click()
                sleep(2)
                self.driver.find_element_by_id('wlanadvance_menuId').click()
                sleep(1)
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('1_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 2:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('2_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 3:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('3_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 4:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('4_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 5:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('5_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 6:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('6_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 7:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('7_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 8:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('8_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 9:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('9_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 10:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('10_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 11:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('11_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 12:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('12_BigSelectBoxScrollItemID').click()
                sleep(1)
            elif channel == 13:
                self.driver.find_element_by_id('wifi_channel24g_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('13_BigSelectBoxScrollItemID').click()
                sleep(1)

            self.driver.find_element_by_id('SendSettings_submitbutton').click()
            sleep(5)
            return True
        except:
            to_log('WiFi信道设置Failed')
            return False

    # Wifi模式设置
    def mode_set(self, mode='bgn'):
        try:
            if mode == 'bg':
                self.driver.find_element_by_class_name('want_more').click()
                sleep(3)
                self.driver.find_element_by_id('wifiadvancesetparent_menuId').click()
                sleep(2)
                self.driver.find_element_by_id('wlanadvance_menuId').click()
                sleep(1)
                self.driver.find_element_by_id('wlan_mode_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('b/g_BigSelectBoxItemID').click()
                sleep(1)
            elif mode == 'b':
                self.driver.find_element_by_id('wlan_mode_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('b_BigSelectBoxItemID').click()
                sleep(1)
            elif mode == 'g':
                self.driver.find_element_by_id('wlan_mode_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('g_BigSelectBoxItemID').click()
                sleep(1)

            self.driver.find_element_by_id('SendSettings_submitbutton').click()
            sleep(5)
            return True
        except:
            to_log('WiFi模式设置Failed')
            return False

    # WiFi频宽设置
    def hz_set(self, hz='40'):
        try:
            if hz == '20':
                self.driver.find_element_by_class_name('want_more').click()
                sleep(3)
                self.driver.find_element_by_id('wifiadvancesetparent_menuId').click()
                sleep(2)
                self.driver.find_element_by_id('wlanadvance_menuId').click()
                sleep(1)
                self.driver.find_element_by_id('wlan_mode_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('b/g/n_BigSelectBoxItemID').click()
                sleep(1)
                self.driver.find_element_by_id('wifi_bind_set_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('20_BigSelectBoxItemID').click()
                sleep(1)
            elif hz == '40/20':
                self.driver.find_element_by_id('wifi_bind_set_ctrl_selectlist_childselect').click()
                sleep(1)
                self.driver.find_element_by_id('20_40_BigSelectBoxItemID').click()
                sleep(1)

            self.driver.find_element_by_id('SendSettings_submitbutton').click()
            sleep(5)
            return True
        except:
            to_log('WiFi频宽设置Failed')
            return False

    # WiFi是否隐藏
    def ssid_set(self):
        try:
            self.driver.find_element_by_class_name('want_more').click()
            sleep(3)
            self.driver.find_element_by_id('wifiadvancesetparent_menuId').click()
            sleep(2)
            self.driver.find_element_by_id('wlanadvance_menuId').click()
            sleep(1)

            self.driver.find_element_by_id('wifi_display_ssid_ctrl_selectlist_childselect').click()
            sleep(1)
            self.driver.find_element_by_id('true_BigSelectBoxItemID').click()
            sleep(1)

            self.driver.find_element_by_id('SendSettings_submitbutton').click()
            sleep(5)
            return True
        except:
            to_log('WiFi是否隐藏设置Failed')
            return False

    def finished(self):
        self.driver.close()


rc = Configuration()

