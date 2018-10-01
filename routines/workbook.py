#!/usr/bin/env python3

from openpyxl import Workbook
#creates an xlsx file or modifies cur
def ExcelColumnsMod(name, list1, r, c):
    wb = Workbook()
    ws = wb.active

    for item in list1:
        ws.cell(row= r, column= c) = item
        r = += 1
    wb.save(name)

list1 = [for x in range(15)]
print(list1)
