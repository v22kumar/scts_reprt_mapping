import math

import pandas
import tabula
import os
import openpyxl
import os


def convert_to_array(in_data):
    measure_values_allowed = ["TRUE", "HIGH", "LOW", "OPEN"]
    out_data = []
    for data in in_data:
        if not isinstance(data, float):
            if "." in data:
                out_data.append(data)
            else:
                if data in measure_values_allowed:
                    out_data.append(data)
    return out_data


def create_excel_data(tabula_dataframe):
    i = 0
    excel_data_list = []
    while i != len(tabula_dataframe):
        print(tabula_dataframe[i].columns)
        try:
            if (")" in tabula_dataframe[i].columns[0]) and (")" in tabula_dataframe[i+1].columns[0]):
                excel_data_list.append({
                    "Test_name": tabula_dataframe[i].columns[1],
                    "Measured_value": convert_to_array(tabula_dataframe[i].iloc[:, -3].to_list())
                })
                i += 1
            elif "named" in tabula_dataframe[i].columns[0]:
                print(tabula_dataframe[i].columns[0])
                pass
                i += 1
            else:
                n = 1
                test_name = tabula_dataframe[i].columns[1]
                measured_data = convert_to_array(tabula_dataframe[i].iloc[:, -3].to_list())
                while ")" not in tabula_dataframe[i+n].columns[0]:
                    measured_data.append(tabula_dataframe[i+n].columns[-3])
                    measured_data.append(convert_to_array(tabula_dataframe[i+n].iloc[:, -3].to_list()))
                    n += 1
                excel_data_list.append({
                    "Test_name": test_name,
                    "Measured_value": measured_data
                })
        except IndexError:
            pass
        i += 1
    return excel_data_list


files = os.listdir("pdf_reports")
for file in files:
    tables = tabula.read_pdf(f"pdf_reports/{file}", pages="1")
    new_report_data = create_excel_data(tables)









