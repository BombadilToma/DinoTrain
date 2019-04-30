import xlrd

file_location = "D:/Programozas/DinoDTB.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print sheet.cell_value(0,0)

