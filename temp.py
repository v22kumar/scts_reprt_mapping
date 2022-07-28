# import pandas
# import tabula
# import os
# import openpyxl
# import os
# import re
# import pandas as pd
# import numpy as np
# from numpy import ndarray
# FILES = ['TYPE-1 STANDARD.pdf', 'TYPE-10 STANDARD.pdf', 'TYPE-12 STANDARD1.pdf', 'TYPE-13 STANDARD1.pdf', 'TYPE-14 STANDARD.pdf',
#          'TYPE-2 STANDARD.pdf', 'TYPE-3 STANDARD.pdf', 'TYPE-4 STANDARD.pdf', 'TYPE-5 STANDARD.pdf', 'TYPE-6_STANDARD1....pdf',
#          'TYPE-7 STANDARD.pdf', 'TYPE-8 STANDARD.pdf', 'TYPE-9 STANDARD.pdf', 'TYPE_11_STANDARD.pdf']
#
# tables = tabula.read_pdf(f"pdf_reports/{FILES[10]}", pages="all")
# tb_df = pd.DataFrame(tables)
# tb_df.to_csv("temp.csv")
# # print(tb_df[4:5])
# # table_column = tables[4].columns.to_list()
# # print(table_column[1])
# # print(len(tables))
list_1 = [2.5, "unnamed", 2.5]
measure_values_allowed = ["TRUE", "HIGH", "LOW", "OPEN"]
data = [value for value in list_1 if ((value in measure_values_allowed) or (isinstance(value, float)))]
print(data)
