import openpyxl
from openpyxl import Workbook

workbook = Workbook()

workbook.save(filename="sample.xlsx")

wb = openpyxl.load_workbook("sample.xlsx") 

sheet = wb.active 

data = (
    (1, 2, 3),
    (4, 5, 6)
)
for row in data:
    sheet.append(row)

wb.save('sample.xlsx')