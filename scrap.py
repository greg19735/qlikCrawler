import pandas as pd
import xlrd
from datetime import date
import pickle


totals = pd.read_excel ('C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheetname='Total Links')
#print (totals)


today = date.today()


#Errors = pd.read_excel (r'C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheet_name='Errors')
#Errors = pd.read_excel (r'C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx', sheet_name='Errors')

xl = pd.ExcelFile('C:\\Users\\greg\\PycharmProjects\\qlikCrawler\\totals\\linkHistory.xlsx')



links = xl.parse(xl.sheet_names[0],skiprows=9 )

links.columns = ['Month', 'OMS', 'OA', 'OAS', 'OHR', 'OGD' ,'ORBO', 'Cinci', 'Careers', 'FACA', 'Greening', 'Contracts', 'NSCEP', 'Grants', 'OEI', 'TEST1', 'TEST2', 'TEST3']


errorSheet = xl.parse(xl.sheet_names[1])

#print (links.columns)
print (links.shape)
print (links.head)


pickle.dump(links, open("pickle/test.pkl","wb"))


d = {'col1': ['Month99', 'OMS99', 'OA99', 'OAS99', 'OHR99', 'OGD99' ,'ORBO99', 'Cinci99', 'Careers99', 'FACA99', 'Greening99', 'Contracts99', 'NSCEP99', 'Grants99', 'OEI99', 'TEST199', 'TEST299', 'TEST399']}

month = 'CurrentMonth'
OMSNum = 123
OANum = 455
OASNum = 1232
OHRNum = 1233
OGDNum = 1234
ORBONum = 1235
CinciNum = 1236
CareersNum = 123777
FACANum = 1238888
GreeningNum = 123883
ContractsNum = 12
NSCEPNum = 11266
GrantsNum = 1564
OEINum = 255145
TEST1Num = 1251252
TEST2Num = 1235125
TEST3Num = 123125125125





d = {'Month': [month], 'OMS': [OMSNum], 'OA': [OANum], 'OAS': [OASNum], 'OHR': [OHRNum], 'OGD': [OGDNum], 'ORBO': [ORBONum], 'Cinci': [CinciNum],
     'FACA': [FACANum], 'Greening': [GreeningNum], 'Contracts': [ContractsNum], 'NSCEP': [NSCEPNum], 'Grants': [GrantsNum], 'OEI': [OEINum], 'TEST1': [TEST1Num], 'TEST2': [TEST2Num], 'TEST3': [TEST3Num]}


df = pd.DataFrame(data=d)

asd = links.append(df)
print("tails")

print (asd.tail)
print(links.shape)

print(links.tail(1))
print(links.iloc[-1]['Month'])



lastMonth = links.iloc[-1]['Month']

print("Last Month: " + str(lastMonth))


for i, j in links.iterrows():
    #print(i, j)
    index = "a"





def dateTest(month):
    newDate = ""

    return newDate







#if Excel's last month is different to current month, add a new line with the current month.