# coding=utf-8

# LAN方式网络配置
import lanDhcpUsb, lanDhcp, lanStaticIP, lanStaticIpUsb

# WIFI方式DHCP、非DHCP，加密、混合加密
import wifiDhcpUsb, wifiDhcpWPA2, wifiStaticIpWPA_WPA2, wifiStaticIpUsb

# WIFI不同信道、模式、频宽
import wifiChannelChange, wifiModeChange, wifiBandwidthChange

# WIFI名字、密码相关
import wifiName32Pwd63, wifiNameSpecial, wifiPwdIsEmpty, wifiNameWasWrong, wifiPwdWasWrong

# WIFI是否隐藏
import wifiOfHideAndNoPwd, wifiOfHideConfigYes, wifiOfHideConfigNo

# 手机热点
import wifiOfMobile

# 断网重连
import wifiBreakAndReconnection

# 3G网络配置
import g3Dhcp, g3DhcpUsb
