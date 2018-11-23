# coding=utf-8
import xlrd

workbook = xlrd.open_workbook('apiResponse.xlsx')
sheet1 = workbook.sheet_by_index(0)

for i in range(2, sheet1.nrows):
    text = sheet1.cell(i, 5).value
    f = open(r'apiResponse/'+str(i-1)+'.txt', 'w')
    f.write(text)
    f.close()
