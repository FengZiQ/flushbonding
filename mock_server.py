import bottle
import xlrd

scannedCodeIndex = -1
refundIndex = -1
paymentResponseData = []
refundResponseData = []
workbook = xlrd.open_workbook('apiResponseData.xlsx')
table1 = workbook.sheet_by_name('paymentData')
table2 = workbook.sheet_by_name('refundData')

for i in range(1, table1.nrows):
    paymentResponseData.append(table1.cell(i, 4).value)

for i in range(1, table2.nrows):
    refundResponseData.append(table2.cell(i, 4).value)


@bottle.route('/api/scannedCode', method='POST')
def scannedCode():
    global scannedCodeIndex
    scannedCodeIndex += 1
    print('返回response为：\n'+paymentResponseData[scannedCodeIndex])
    return paymentResponseData[scannedCodeIndex]


@bottle.route('/api/refund', method='POST')
def refund():
    global refundIndex
    refundIndex += 1
    print('返回response为：\n' + refundResponseData[refundIndex])
    return refundResponseData[refundIndex]


bottle.run(host='192.168.20.94', port=8800)


