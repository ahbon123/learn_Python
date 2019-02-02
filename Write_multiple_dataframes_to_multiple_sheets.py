#https://stackoverflow.com/questions/35707723/writing-multiple-pandas-dataframes-to-multiple-excel-worksheets

import pandas as pd
#initialze the excel writer
writer = pd.ExcelWriter('MyFile.xlsx', engine='xlsxwriter')

#store your dataframes in a  dict, where the key is the sheet name you want
frames = {'sheetName_1': dataframe1, 'sheetName_2': dataframe2,
        'sheetName_3', dataframe3}

#now loop thru and put each on a specific sheet
for sheet, frame in frames.items(): # .use .iteritems for python 2.X
    frame.to_excel(writer, sheet_name = sheet, index = False)

#critical last step
writer.save()
