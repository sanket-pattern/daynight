import pandas as pd
import schedule
import time
df1=pd.read_csv("Todays_Open.csv")
df2=pd.read_csv("Todays_Close.csv")
Cash=100000
number_of_stocks=dict()
df1.set_index(df1.columns.values[0],inplace=True)
df2.set_index(df2.columns.values[0],inplace=True)
df3=pd.merge(df1,df2,on='Symbol',how='outer')
df3["PCT_Change"]=(df3["Close_Price"]-df3["Open_Price"])/df3["Open_Price"]
df3.set_index(["Symbol"],inplace=True)
# print(df3)
def buy():
    df1 = pd.read_csv("Todays_Open.csv")
    df2 = pd.read_csv("Todays_Close.csv")
    f=open("Cash.txt","r")
    Cash=float(f.read())
    df1.set_index(df1.columns.values[0], inplace=True)
    df2.set_index(df2.columns.values[0], inplace=True)
    df3 = pd.merge(df1, df2, on='Symbol', how='outer')
    df3["PCT_Change"] = (df3["Close_Price"] - df3["Open_Price"]) / df3["Open_Price"]
    df3.set_index(["Symbol"], inplace=True)
    df_sorted=df3.sort_values('PCT_Change')
    buying_df=(df_sorted[:6])
    buying_list=buying_df.index.values
    quantity=[]
    for item in buying_list:
        quantity.append([item,(Cash/6)/buying_df.ix[item]["Close_Price"]])
    df_quantity=pd.DataFrame(quantity,columns=["Symbol","Quantity"])
    df_quantity.set_index(["Symbol"],inplace=True)
    df_quantity.to_csv("Quantity.csv")

def sell():
    df1 = pd.read_csv("Todays_Open.csv")
    df2 = pd.read_csv("Todays_Close.csv")
    df1.set_index(df1.columns.values[0], inplace=True)
    df2.set_index(df2.columns.values[0], inplace=True)
    df3 = pd.merge(df1, df2, on='Symbol', how='outer')
    df3["PCT_Change"] = (df3["Close_Price"] - df3["Open_Price"]) / df3["Open_Price"]
    df3.set_index(["Symbol"], inplace=True)
    cash=0
    df_quantity=pd.read_csv("Quantity.csv")
    df_quantity.set_index(["Symbol"],inplace=True)
    print(df_quantity)
    f=open("Cash","w")
    for item in list(df_quantity.index.values):
        cash=cash+(df_quantity.ix[item]["Quantity"]*df3.ix[item]["Open_Price"])
    f.write(str(cash))
#
#
schedule.every().day.at("9:15").do(sell)
schedule.every().day.at("03:27").do(buy)

while True:
    schedule.run_pending()
    time.sleep(1)