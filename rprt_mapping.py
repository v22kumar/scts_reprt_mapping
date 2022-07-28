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

# files = os.listdir("pdf_reports")
FILES = ['TYPE-1 STANDARD.pdf']
# 'TYPE-10 STANDARD.pdf', 'TYPE-12 STANDARD1.pdf', 'TYPE-13 STANDARD1.pdf', 'TYPE-14 STANDARD.pdf',
# 'TYPE-2 STANDARD.pdf', 'TYPE-3 STANDARD.pdf', 'TYPE-4 STANDARD.pdf', 'TYPE-5 STANDARD.pdf', 'TYPE-6_STANDARD1....pdf',
# 'TYPE-7 STANDARD.pdf', 'TYPE-8 STANDARD.pdf', 'TYPE-9 STANDARD.pdf', 'TYPE_11_STANDARD.pdf'

i = 0
file_name = []
table_clms = []
print(FILES[i])
# tables = tabula.read_pdf(f"pdf_reports/", pages="all")
# print(tables)
for file in FILES:
    tables = tabula.read_pdf(f"pdf_reports/{FILES[i]}", pages="all")
#     df_tables = pd.DataFrame(tables[1])
# for df_t in range(len(df_tables)):
#     print((df_tables["Unnamed: 1"]))





    for i in range(len(tables)):

        table_column = tables[i].columns.to_list()
        table_column_ = tables[i+1].columns.to_list()
        if ')' in table_column[0]:
            if ')' not in table_column_[0]:
                df_dfa = pd.DataFrame(table_column)
                df_dff = pd.DataFrame(table_column_)
                df_dff__ = df_dff.replace(regex=r"\s*\.\s*", columns= df_dfa.columns)


# df = pd.DataFrame(table_clms)
# df.to_csv("output_df1.csv")



# print(file_name)

# tbl_df = pd.DataFrame(table_clms)
# tbl_df.to_csv("output_df.csv")

