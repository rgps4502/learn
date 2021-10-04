# * -*- coding: utf-8 -*-
import xlrd
import xlwt

file = 'MKT1.xlsx'
xlsx = xlrd.open_workbook(file)
table = xlsx.sheets()[0]  # 打開第一張表
nrows = table.nrows
for i in range(nrows):
    print(table.row_values(i)[:7])
# print(nrow)
