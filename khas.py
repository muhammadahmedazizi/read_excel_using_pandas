# Ref : https://www.caktusgroup.com/blog/2019/08/13/import-multiple-excel-sheets-pandas/
# Tutorial Followed

import pandas as pd

def read_excel_sheets(xls_path):
    """Read all sheets of an Excel workbook and return a single DataFrame"""
    print(f'Loading {xls_path} into pandas')
    xl = pd.ExcelFile(xls_path)
    df = pd.DataFrame()
    columns = None
    for idx, name in enumerate(xl.sheet_names):
        print(f'Reading sheet #{idx}: {name}')
        sheet = xl.parse(name)
        if idx == 0:
            # Save column names from the first sheet to match for append
            columns = sheet.columns
        sheet.columns = columns
        # Assume index of existing data frame when appended
        df = df.append(sheet, ignore_index=True)
    return df


stops = read_excel_sheets("data/fortuner2.xlsx")

stops.to_csv("end.csv", index=False)