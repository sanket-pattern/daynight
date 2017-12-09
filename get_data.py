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
with open('bloomber_list.pkl', 'rb') as f:
    bloomberg_list=pickle.load(f)

def get_current_price(symbol):
    url=urllib.request.urlopen("https://www.bloomberg.com/quote/"+symbol+":IN")
    html=url.read()
    url.close()
    soup = BeautifulSoup(html,"html.parser")
    span=soup.find("span",{"class":"priceText__1853e8a5"})
    if span != None:
        price[symbol]=span.text
        print(symbol,span.text)
    else:
        print(symbol)




def multi_fetch():
    pool = Pool(os.cpu_count())
    pool.map(get_current_price, bloomberg_list)
    print(price)

if __name__ == '__main__':
    multi_fetch()
# def hello():
#     print("Hello")
# schedule.clear()
# schedule.every().day.at("00:40").do(hello)


# while True:
#     schedule.run_pending()
#     time.sleep(1)