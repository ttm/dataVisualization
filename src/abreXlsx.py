import openpyxl as px

W = px.load_workbook("../data/Times World University Rankings (2016).xlsx")
data = [i for i in W["Sheet1"].values]
