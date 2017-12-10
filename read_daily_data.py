'''
The code will be used to collect daily open price and close price data everyday 9.30am and 3.30pm and update the csv files.

'''
import datetime
from selenium import webdriver
import pyautogui
from selenium.common.exceptions import WebDriverException
import schedule
import os
import pandas as pd
from multiprocessing import Pool
symbols=pd.read_csv('Symbols.csv')
sym=symbols['Symbol']
symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
symbol_list=sorted(symbol_list)
prices=dict()
symbol_price=[]
import time
def str_to_float(str):
    str = str.replace(",", "")
    return float(str)


def update_close_price(symbol):
    # for symbol in symbol_list
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.co.in/")
    time.sleep(1)
    driver.find_element_by_class_name("gsfi").send_keys(symbol + " Stock Price")
    driver.find_element_by_name("btnK").submit()
    # driver.find_elements_by_name("btnK")[0].click()
    val = driver.find_element_by_class_name("fac-l").text
    print([symbol,str_to_float(val)])
    driver.close()
    return symbol_price+[symbol,val]

def update_open_price(symbol):
    # for symbol in symbol_list
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.co.in/")
    time.sleep(1)
    driver.find_element_by_class_name("gsfi").send_keys(symbol + " Stock Price")
    driver.find_element_by_name("btnK").submit()
    val = driver.find_element_by_class_name("_Sl").text
    print([symbol, str_to_float(val)])
    driver.close()
    return symbol_price + [symbol, str_to_float(val)]


def fetch_open():
    pool = Pool(os.cpu_count())
    symbol_price=pool.map(update_open_price, symbol_list)
    df = pd.DataFrame(symbol_price, columns=['Symbol', 'Open_Price'])
    df.to_csv("Todays_Open2.csv")

def fetch_close():
    pool = Pool(os.cpu_count())
    symbol_price=pool.map(update_close_price, symbol_list)
    df = pd.DataFrame(symbol_price, columns=['Symbol', 'Close_Price'])
    df.to_csv("Todays_Close2.csv")

if __name__ == '__main__':

    schedule.every().day.at("00:37").do(fetch_open)
    schedule.every().day.at("03:24").do(fetch_close)

    while True:
        schedule.run_pending()
        time.sleep(1)