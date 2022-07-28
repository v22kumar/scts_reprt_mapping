import pandas
import tabula
import os
import openpyxl
import os


def create_excel_data(tabula_dataframe):
    i = 0
    excel_data_list = []
    while i != len(tabula_dataframe):
        i += 1
        try:
            if (")" in tabula_dataframe[i].columns[0]) and (")" in tabula_dataframe[i+1].columns[0]):
                excel_data_list.append({
                    "Test_name": tabula_dataframe[i].columns[1],
                    "Measured_value": tabula_dataframe[1]["Unnamed: 2"].to_list()
                })
            else:
                print(i)
        except IndexError:
            pass
    return excel_data_list


files = os.listdir("pdf_reports")
for file in files:
    tables = tabula.read_pdf(f"pdf_reports/{file}", pages="all")
    new_report_data = create_excel_data(tables)
    print(file)
    print(new_report_data)
