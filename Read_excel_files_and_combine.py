#https://zhuanlan.zhihu.com/p/31541902 

import pandas as pd
import os
inputdir=r'C:\Users\数据\Desktop\新建文件夹'
df_empty=pd.DataFrame(columns=['名称','列1','列2'])
for parents, dirnames, filenames in os.walk(inputdir):
    for filename in filenames:
        df=pd.read_excel(os.path.join(parent,filename))
        df_empty=df_empty.append(df,ignore_index=True)

#https://blog.csdn.net/d1240673769/article/details/74513206

# -*- coding: utf-8 -*-
#将多个Excel文件合并成一个
import xlrd
import xlsxwriter

#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh

#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()

#获取sheet表的行数
def getnrows(fh,sheet):
    table=fh.sheets()[sheet]
    return table.nrows

#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue

#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)
    for sheet in sh:
        x+=1
    return x


if __name__=='__main__':
    #定义要合并的excel文件列表
    allxls=['F:/test/excel1.xlsx','F:/test/excel2.xlsx']
    #存储所有读取的结果
    datavalue=[]
    for fl in allxls:
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(fl,shnum)
    #定义最终合并后生成的新文件
    endfile='F:/test/excel3.xlsx'
    wb1=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")
        
#https://blog.csdn.net/u012209894/article/details/80097271

#!/usr/bin/env python
# coding=utf-8
import xlrd
import shutil
from xlutils.copy import copy
import datetime
 
 
class excel_cp:
    def __init__(self, ):
        day = datetime.date.today()
        self.str_day = str(day).replace('-', '')
 
    # 处理excel合并
    def excel_merge(self, old_name, new_name):
        if old_name == '降价通知.xls':
            lead_source = 'r510'
        elif old_name == 'BI5096.xls':
            lead_source = 'r953'
        elif old_name == '400溢出.xls':
            lead_source = 'r880'
        elif old_name == '潜客推荐.xls':
            lead_source = 'r722'
        else:
            lead_source = 'r520'
        old_dir = 'E:\\load_bi\\' + self.str_day + '\\' + old_name
        new_dir = 'E:\\load_bi\\' + self.str_day + '\\' + new_name
        # 打开要使用的excel,获取要需要写入的行数
        bk = xlrd.open_workbook(old_dir)
        sh = bk.sheet_by_name("Page 1")
        nrows = sh.nrows
        # 打开要插入的excel,获取sheet页面的行数,再获取输入的sheet
        oldWb = xlrd.open_workbook(new_dir, formatting_info=True)
        in_sheet = oldWb.sheet_by_name("Sheet1")
        in_nrows = in_sheet.nrows
        newWb = copy(oldWb)
        sheet = newWb.get_sheet(0)
        for i in range(1, nrows):
            row_data = sh.row_values(i)
            print(row_data)
            for j in (in_nrows-1+i, i+in_nrows-1):
            # ---------写出文件到excel--------
                print("-----正在往j写入 " + str(j) + " 行")
                sheet.write(j, 0, label=sh.cell_value(i, 4))   # 将old_dir的第i行第5列数据写入到new_dir第j行第1列
                sheet.write(j, 1, label=sh.cell_value(i, 1))   # 将old_dir的第i行第2列数据写入到new_dir第j行第2列
                sheet.write(j, 3, lead_source)                 # 将指定数据写入到new_dir第2行第4列
                sheet.write(j, 14, label=sh.cell_value(i, 2))  # 将old_dir的第i行第3列数据写入到new_dir第j行第15列
                sheet.write(j, 15, label=sh.cell_value(i, 3))  # 将old_dir的第i行第4列数据写入到new_dir第j行第16列
                sheet.write(j, 28, label=sh.cell_value(i, 7))  # 将old_dir的第i行第8列数据写入到new_dir第j行第29列
                sheet.write(j, 29, label=sh.cell_value(i, 8))  # 将old_dir的第i行第9列数据写入到new_dir第j行第30列
                sheet.write(j, 30, label=sh.cell_value(i, 9))  # 将old_dir的第i行第10列数据写入到new_dir第j行第31列
        newWb.save(new_dir)
 
    # 复制文件到指定路径
    def file_copy(self, rm_file):
        rm_file_dir = 'E:\\load_bi\\' + self.str_day + '\\' + rm_file
        new_file_dir = 'C:\\fakepath\\' + rm_file
        shutil.copyfile(rm_file_dir, new_file_dir)
 
 
if __name__ == '__main__':
    # @version : 3.4
    # @Author  : robot_lei
    # @Software: PyCharm Community Edition
    # 将这多个excel合并成一张
    old_file_name_s = ('降价通知.xls', 'BI5096.xls', '车库线索.xls', '400溢出.xls', '潜客推荐.xls')
    leads_source_str = ('r510', 'r953', 'r520', 'r880', 'r722')
    new_file_name = '5096.xls'
    for old_file_name in old_file_name_s:
        excel_cp().excel_merge(old_file_name, new_file_name)
    # 复制文件到指定路径
    excel_cp().file_copy(new_file_name)

        
        
