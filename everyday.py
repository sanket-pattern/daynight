
import pandas as pd
# # f=open("symbols.txt","r")
# # l=f.read().split(",")
# # l.remove('')
# # symbols=pd.read_csv('Symbols.csv')
# # sym=symbols['Symbol']
# # # symbol_list=sorted(list(sym)+['ADANIENT','BALRAMCHIN','CHAMBLFERT'])
# # # print(symbol_list)
# # # print(set(symbol_list).difference(set(l)))
# # str="DALMIABHA DBEL https://www.bloomberg.com/quote/DBEL:IN"
# # if(str[-2:]=="IN"):
# #     print(str)
# f=open("links","r")
# t=f.read().split("\n")
# for link in t:
#     if(link[-2:]!="IN"):
#         print(link)
import pickle
table=[["ABC",123], ["TEX",234]]
header=["Symbol","Price"]
df=pd.DataFrame(table,columns=header)
print(df)