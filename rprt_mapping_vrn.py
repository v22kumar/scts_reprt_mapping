import math

import pandas
import pandas as pd
import tabula
import os
import openpyxl
import os

read_data = tabula.read_pdf('TYPE-7 STANDARD.pdf',pages= 'all')
data_sheet = pd.DataFrame(columns=['Test_name','Measured_Values'])
for i in range(len(read_data)):
    if ':' not in read_data[i].columns[1]:
        # print(read_data[i].values[:,-3])
        db_s = pd.DataFrame(columns=['Test_name','Measured_Values'],value = [read_data[i-1].columns[1],read_data[i].values[:,-3]])
        print(db_s)