
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

route = ''

docXLS = xlrd.open_workbook("employeedata.xls")
 
sheetXLS = docXLS.sheet_by_index(0)

seconddocXLS = open_workbook("employeedata.xls")
copyXLS = copy(seconddocXLS)
sheetGetterXLS = copyXLS.get_sheet(0)
 
modifier = ''
for rx in range(sheetXLS.nrows - 1):
    modifier = sheetXLS.cell_value(rowx=rx + 1, colx=1)
    modifier = modifier.replace("helpinghands.cm", "handinhand.org")
    sheetGetterXLS.write(rx + 1, 1, modifier)
copyXLS.save('employeedata.xls')
print("xls file modification Done")

print("everything are Done")
