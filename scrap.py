import pandas as pd
import xlrd
from datetime import date

#totals = pd.read_excel ('C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheet_name='Total Links')
#print (totals)


today = date.today()


#Errors = pd.read_excel (r'C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheet_name='Errors')
#Errors = pd.read_excel (r'C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheet_name='Errors')

xl = pd.ExcelFile('C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx')

linkSheet = xl.parse(xl.sheet_names[0])

errorSheet = xl.parse(xl.sheet_names[1])

print (linkSheet.columns)

w