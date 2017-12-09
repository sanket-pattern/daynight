'''
The code will be used to collect daily open price and close price data everyday 9.30am and 3.30pm and update the csv files.

'''
import datetime
from selenium import webdriver
import os
import pandas as pd
from multiprocessing import Pool
symbols=pd.read_csv('Symbols.csv')
sym=symbols['Symbol']
symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
prices=dict()

def get_current_price(symbol):

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.co.in/")
    driver.find_element_by_class_name("gsfi").send_keys(symbol + " Stock Price")
    search_button = driver.find_elements_by_name("btnK")
    search_button[0].click()
    val = driver.find_element_by_class_name("fac-l").text
    prices[symbol]=val
    print(symbol,val)
    driver.close()

if __name__ == '__main__':
    pool = Pool(1)                         # Create a multiprocessing Pool
    pool.map(get_current_price, symbol_list)