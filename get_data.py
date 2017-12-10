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


# print(set(bloomberg_list))
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
    print("hello world")
    pool = Pool(os.cpu_count())
    pool.map(get_current_price, bloomberg_list)
    print(price)
def hello():
    print("Hello")

if __name__ == '__main__':
    schedule.clear()
    schedule.every().day.at("13:19").do(multi_fetch)
    # schedule.every().day.at("01:14").do(multi_fetch)

    while True:
        schedule.run_pending()
        time.sleep(1)