from bs4 import BeautifulSoup
import time
import csv
import os
import pandas as pd
from multiprocessing import Pool
import pickle
import urllib.request
from selenium import webdriver
with open('bloomber_list.pkl', 'rb') as f:
    l=pickle.load(f)
def get_price(symbol):

    url=urllib.request.urlopen("https://www.bloomberg.com/quote/"+symbol+":IN")
    html=url.read()
    url.close()
    soup = BeautifulSoup(html,"html.parser")
    span=soup.find("span",{"class":"priceText__1853e8a5"})
    print(symbol,span.text)
# symbols=pd.read_csv('Symbols.csv')
# sym=symbols['Symbol']
# symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
# bloomberg_symbol_list=[]
# with open('bloomber_list.pkl', 'wb') as f:
#     pickle.dump(bloomberg_symbol_list, f)
# s="https://www.bloomberg.com/quote/JUBILANT:IN"
# pos=s.rfind("/")+1
# pos2=s.rfind(":")

# s[pos:pos2]

# def get_symbol(symbol):
#     driver = webdriver.Chrome("chromedriver.exe")
#     driver.get("https://www.google.co.in/")
#     driver.find_element_by_class_name("gsfi").send_keys( symbol+" Share Price Bloomberg")
#     search_button = driver.find_elements_by_name("btnK")
#     search_button[0].click()
#     s=str(driver.find_element_by_class_name("_Rm").text)
#     print(s)
#     pos=s.rfind("/")+1
#     pos2=s.rfind(":")
#     sym=s[pos:pos2]
#     print(sym)
#     bloomberg_symbol_list.append(sym)
#
#     with open('bloomber_list.pkl', 'rb') as f:
#         l=pickle.load(f)
#         l.append(sym)
#     with open('bloomber_list.pkl', 'wb') as f:
#         pickle.dump(l,f)
#     driver.close()
#
if __name__ == '__main__':
    pool = Pool(os.cpu_count())                         # Create a multiprocessing Pool
    pool.map(get_price, l)
#
# with open('bloomber_list.pkl', 'rb') as f:
#     l=pickle.load(f)
#
# with open('bloomber_list.pkl', 'rb') as f:
#     l=pickle.load(f)
#     l.remove('')
#     l.remove('1208')
# with open('bloomber_list.pkl', 'wb') as f:
#     pickle.dump(l,f)
