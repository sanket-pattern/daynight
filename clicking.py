from selenium import webdriver
import time
import os
import pandas as pd
driver=webdriver.Chrome("chromedriver.exe")
symbols=pd.read_csv('Symbols.csv')
sym=symbols['Symbol']
symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
for sym in symbol_list:
    print("==================================================")
    print(sym)
    driver.get("https://finance.yahoo.com/quote/"+sym+".BO/history?period1=1441218600&period2=1504377000&interval=1d&filter=history&frequency=1d")
    elem=driver.find_elements_by_partial_link_text("Download Data")
    while  (os.path.isfile("C:\\Users\\HP\\Downloads\\"+sym+"BO.csv")==False):
        print("true")
        elem[0].click()
        time.sleep(5)
        if os.path.isfile("C:\\Users\\HP\\Downloads\\"+sym+"BO.csv"):
            break
