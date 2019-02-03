#https://stackoverflow.com/questions/26521266/using-pandas-to-pd-read-excel-for-multiple-worksheets-of-the-same-workbook

import pandas as pd

df = pd.read_excel('excel_file_path.xls')
# this will read the first sheet into df

xls = pd.ExcelFile('excel_file_path.xls')

# Now you can list all sheets in the file
xls.sheet_names
# ['house', 'house_extra', ...]

# to read just one sheet to dataframe:
df = pd.read_excel(file_name, sheetname="house")

# to read all sheets to a map
sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
    
# @ihightower pointed out in the comments that all sheets can be 
# directly read into an ordered dictionary in 1 step

# for pandas version >= 0.21.0
sheet_to_df_map = pd.read_excel(file_name, sheet_name=None)

# for pandas version < 0.21.0
sheet_to_df_map = pd.read_excel(file_name, sheetname=None)

#https://stackoverflow.com/questions/42887663/reading-multiple-tabs-from-excel-in-different-dataframes

xl = pd.read_excel('Unique.xlsx', sheetname=None)
xl_dict = {}
sheetname_list = ['blah1', 'blah2', 'blah3']
for sheet in sheetname_list:
    xl_dict[sheet] = pd.read_excel('Unique.xlsx', sheetname=sheet)

xl = pd.read_excel('Unique.xlsx', sheetname=sheetname_list)
