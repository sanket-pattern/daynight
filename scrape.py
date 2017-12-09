from bs4 import BeautifulSoup
import time
import csv
import os
import pandas as pd
import urllib.request
symbols=pd.read_csv('Symbols.csv')
sym=symbols['Symbol']
symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
for symbol in symbol_list:
    df1=pd.read_csv("Data2//"+symbol+".csv")
    df1.set_index(["Date"],inplace=True)
    df1.to_csv("Data2//"+symbol+".csv")
    df2=pd.read_csv("Data//"+symbol+".csv")
    df2.set_index(["Date"], inplace=True)
    df3=pd.concat([df1,df2])
    df3.to_csv("Data//"+symbol+".csv")
for symbol in symbol_list:
    print("===========================================================================================================")
    print(symbol)
    url=urllib.request.urlopen("https://finance.yahoo.com/quote/"+symbol+".BO/history?period1=1459621800&period2=1491157800&interval=1d&filter=history&frequency=1d")

    html=url.read()
    url.close()
    soup = BeautifulSoup(html,"html.parser")
    table=soup.find('table',{'data-test':'historical-prices'})
    rows=table.find_all('tr')
    data_list=[]
    print(len(rows))

    for t in rows[1:-1]:
        td=t.find_all('td')
        row=[i.text for i in td]
        if len(row)!=7:
            continue
        open=float(row[1].replace(",",""))
        close=float(row[4].replace(",",""))
        final=[row[0],open,close]
        data_list.append(final)
        # final=row[1]+row[-2]
    df=pd.DataFrame(data_list,columns=['Date','Open','Close'])
    df.set_index(['Date'],inplace=True)
    print(df.head())
    print(df.tail())
    df.to_csv("Data3//"+symbol+".csv")
# files=os.listdir("Data")
# for symbol in files:
#     print(symbol)
#     data=pd.read_csv("Data2//"+symbol)
#     data.set_index(['Date'],inplace=True)
#     print(data.index.values)
#     print(len(data))
#     if len(data)==99:
#         data.drop(data.index[98],inplace=True)
#         data.to_csv("Data2//"+symbol+".csv")
#     data=data.reindex(index=data.index[::-1])
#     c=data.columns.values
#     data=data[['Open','Close']]
#     data.to_csv("Data2//"+symbol)
#     print(data.head())


#
# print(len(files))
#
#
#
