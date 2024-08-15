import pandas as pd
import openpyxl


def ReadExcel(file_path):
    # Load the Excel file
    # file_path = 'D:\\01.餐饮\\交易时间.xlsx'
    data = pd.read_excel(file_path)

    # Display the content of the Excel file to understand its structure
    data.head()
    print(data)
    return data
