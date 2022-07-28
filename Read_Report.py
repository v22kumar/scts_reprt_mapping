import pandas
import tabula
import os
import openpyxl
import os
import re
import pandas as pd
import numpy as np
import PyPDF2
import camelot

FILES = ['TYPE-1 STANDARD.pdf','TYPE-10 STANDARD.pdf', 'TYPE-12 STANDARD1.pdf', 'TYPE-13 STANDARD1.pdf', 'TYPE-14 STANDARD.pdf',
'TYPE-2 STANDARD.pdf', 'TYPE-3 STANDARD.pdf', 'TYPE-4 STANDARD.pdf', 'TYPE-5 STANDARD.pdf', 'TYPE-6_STANDARD1....pdf',
'TYPE-7 STANDARD.pdf', 'TYPE-8 STANDARD.pdf', 'TYPE-9 STANDARD.pdf', 'TYPE_11_STANDARD.pdf']

j = 0
file_name = []
table_clms = []
# for file in FILES:
tables = tabula.read_pdf(f"pdf_reports/{FILES[j]}", pages="all")
table_1 = pd.DataFrame(tables[3]) #Imperfect table
# table_1_ = pd.DataFrame() #concat table having excess column
table_2 = pd.DataFrame(tables[2]) #Perfect table

# print(table_2.iloc[:,2].loc[3]) #getValue from table
# print(table_1.iloc[:,-3].to_numpy())

table_1_ = pd.DataFrame(data=[(table_1.iloc[:,1]).to_numpy(),(table_1.iloc[:,-3]).to_numpy()],index=[1,2],columns=([(str(table_2.columns[3])),(str(table_2.columns[-3]))]))

# table_1_ = pd.DataFrame({(str(table_2.columns[3])):(table_1.iloc[:,1]).to_numpy(),(str(table_2.columns[-3])):(table_1.iloc[:,1]).to_numpy()})
print(table_1_)

# missing_colm = tables[3].columns[:7]  #create dataframe using imperfect table column
colm_arry = tables[2].columns
# missing_arry = missing_colm.to_numpy()
# missin_df = pd.DataFrame(data=[missing_arry],columns=[colm_arry],index=[0])
# print(missin_df)

# if len(table_1.columns) != len(table_2.columns):
#     tabl_arry = table_.to_numpy()
#     # table_1_df = pd.DataFrame(data=[table_1_arry], columns=[colm_arry], index=[0])
#     for i in range(len(tabl_arry)):
#         print(tabl_arry)
# frames = [table_2,table_1]  #concat perfect table and imperfect table
# tbl = pd.concat(frames)
#
# tbl.to_csv("check.csv")
# print(tbl)
# print(len(table_2.columns))


# print(table_1_)
