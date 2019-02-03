#https://stackoverflow.com/questions/15793349/how-to-concatenate-three-excels-files-xlsx-using-python

import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob('myfolder/mydata*.xlsx'):
   df = pd.read_excel(f)
   all_data = all_data.append(df, ignore_index=True)

writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()


#https://stackoverflow.com/questions/46930575/append-multiple-excel-filesxlsx-together-in-python

#method 1: list and pd.concat
all_data = []
for f in glob.glob("output/test/*.xlsx"):
    all_data.append(pd.read_excel(f))
      
df = pd.concat(all_data, ignore_index=True)

#method 2: map and for loop

g = map(pd.read_excel, glob.glob("output/test/*.xlsx"))
df = pd.concat(list(g), ignore_index=True)

#method 3: list comprehension + concat
all_data = [pd.read_excel(f) for f in glob.glob("output/test/*.xlsx")]
df = pd.concat(all_data, ignore_index=True)

#https://stackoverflow.com/questions/20908018/import-multiple-excel-files-into-python-pandas-and-concatenate-them-into-one-dat

#method 1
import numpy as np
import pandas as pd
import glob
all_data = pd.DataFrame()
for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

# now save the data frame
writer = pd.ExcelWriter('output.xlsx')
all_data.to_excel(writer,'sheet1')
writer.save()

#method 2
import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files
files_xls = [f for f in files if f[-3:] == 'xls']
files_xls

df = pd.DataFrame()

for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)
df   
