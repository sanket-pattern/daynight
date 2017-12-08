from selenium import webdriver
import time
import pandas as pd
driver=webdriver.Chrome("chromedriver.exe")
symbols=pd.read_csv('Symbols.csv')
sym=symbols['Symbol']
symbol_list=list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT']
# symbol_list=symbol_list[23:]
# print(symbol_list[47:])
for sym in symbol_list[48:]:
    print("==================================================")
    print(sym)
    driver.get("https://finance.yahoo.com/quote/"+sym+".BO/history?period1=1441218600&period2=1504377000&interval=1d&filter=history&frequency=1d")
    elem=driver.find_elements_by_partial_link_text("Download Data")
    elem[0].click()
    time.sleep(10)



