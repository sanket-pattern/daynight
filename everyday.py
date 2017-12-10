
# import pandas as pd
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
with open('bloomber_list.pkl', 'rb') as f:
    l = pickle.load(f)

l=l+["ATLP","AIAE","GDPL","NJCC","PI","SBIN","STR","BIL"]

l.remove('')
l.remove('')
l.remove('')
l=sorted(set(l))
f=open("final_list","w")
for item in l:
  f.write("%s\n" % item)

