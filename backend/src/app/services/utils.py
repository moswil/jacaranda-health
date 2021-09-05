import pandas as pd


def read_excel_data(excel_file, sheet_name):
    data = pd.read_excel(excel_file, sheet_name)

    return data
