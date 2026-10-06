from xlrd import *

data = []

def get_test_data():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")

    for i in range(2,sheet.nrows):
        rows = sheet.row_values(i)
        testcase = rows[0]
        username = rows[1]
        password = rows[2]
        data.append((testcase,username,password))
    return data

def get_testcase1_data():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")

    rows = sheet.row_values(1)
    test_case = rows[0]
    user_name = rows[1]
    pwd = rows[2]
    return test_case,user_name,pwd


# reading second row with zipcode
def get_row2():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")
    rows = sheet.row_values(1)    #rows=[1,'standard_user','secret_sauce','keerthana','S',560032]
    return rows

def get_invalid_fname():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")
    rows = sheet.row_values(2)
    fn = rows[3]
    ln = rows[4]
    zip_code = rows[5]
    return fn,ln,zip_code