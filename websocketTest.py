# coding=utf-8
from websocket import create_connection

ws0 = create_connection('ws://118.190.137.54/ppcpws')
res0 = ws0.recv()
print('请求IP：118.190.137.54')
print(res0, '\n')
# print(res0.decode(encoding="utf-8", errors="ignore"))


ws1 = create_connection('ws://115.28.166.207/ppcpws')
res1 = ws1.recv()
print('请求IP：115.28.166.207')
print(res1, '\n')


ws2 = create_connection('ws://118.190.232.69/ppcpws')
res2 = ws2.recv()
print('请求IP：118.190.232.69')
print(res2, '\n')

ws3 = create_connection('ws://139.129.36.53/ppcpws')
res3 = ws3.recv()
print('请求IP：118.190.137.54')
print(res3, '\n')


ws4 = create_connection('ws://ppcpnodes.inspos.cn/ppcpws')
res4 = ws4.recv()
print('请求IP：ppcpnodes.inspos.cn')
print(res4)



