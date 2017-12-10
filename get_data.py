from bs4 import BeautifulSoup
import time
import csv
import os
import schedule
import datetime
import pandas as pd
from multiprocessing import Pool
import pickle
import urllib.request
price=dict()
f=open("final_list","r")
bloomberg_list=f.read().split("\n")
bloomberg_list.remove('')
import pandas as pd

def str_to_float(str):
    str = str.replace(",", "")
    return float(str)
symbol_price=[]

# print(set(bloomberg_list))

def multi_fetch():
    print(bloomberg_list)
    for symbol in bloomberg_list:
        str="https://www.bloomberg.com/quote/"+symbol+":IN"
        print(str)
        url=urllib.request.urlopen("https://www.bloomberg.com/quote/"+symbol+":IN")
        html=url.read()
        url.close()
        soup = BeautifulSoup(html,"html.parser")
        span=soup.find("span",{"class":"priceText__1853e8a5"})
        price=str_to_float(span.text)
        print([symbol,price])
    # return (symbol_price+[symbol,price])




# def multi_fetch():
#     print("hello world")
#     pool = Pool(os.cpu_count())
#     print(bloomberg_list[:10])
#     pool.map(get_current_price, bloomberg_list[:10])
#     print(symbol_price)
#     print(len(symbol_price))
    # df=pd.DataFrame(symbol_price,columns=['Symbol','Open_Price'])
    # print(df)
    # df.to_csv("Todays_Close.csv")
def hello():
    print("Hello")

if __name__ == '__main__':
    # schedule.clear()
    multi_fetch()
    # schedule.every().day.at("13:44").do(multi_fetch)
    # schedule.every().day.at("01:14").do(multi_fetch)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)