import os
import numpy as np
import operator
import pandas as pd
import pickle
files=os.listdir("Data")

cash=100000
return_dict=dict()
number_of_stocks=dict()
open_today=dict()
close_today=dict()
open_tomorrow=dict()
close_tomorrow=dict()
data=pd.read_csv("PCT_CHANGE//ADANIENT.csv")
data.set_index(['Date'],inplace=True)
dates=data.index.values
for z,date in enumerate(dates):
    print("============="+date+"===============")
    for file in os.listdir("PCT_CHANGE"):
        data=pd.read_csv("PCT_CHANGE//"+file)
        data.set_index(['Date'],inplace=True)
        return_dict[file[:-4]]=data.ix[date,'Pct_change_OC']
        open_today[file[:-4]]=data.ix[date,'Open']
        close_today[file[:-4]]=data.ix[date,'Close']
        open_tomorrow[file[:-4]]=data.get_value(dates[z+1],'Open')
    sorted_x = sorted(return_dict.items(), key=operator.itemgetter(1))
    cash_start=cash
    #start selling
    if len(number_of_stocks.keys())!=0:
        for key in number_of_stocks.keys():
            cash=cash+(number_of_stocks[key]*open_today[key])
            print(key)
            print("Open Today",open_today[key])
    number_of_stocks=dict()
    cash_end=cash
    print("Cash End",cash_end)
    #start buying
    cash_per_stock = cash / 6.0
    for i in range(6):
        print(sorted_x[i])
        print("Closing Today",close_today[sorted_x[i][0]])
        number_of_stocks[sorted_x[i][0]]=cash_per_stock/close_today[sorted_x[i][0]]
        cash=cash-cash_per_stock
    print(number_of_stocks)


print(number_of_stocks)
with open("final_number_of_stocks.pkl","wb") as f:
    pickle.dump(number_of_stocks,f)



