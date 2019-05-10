from bs4 import BeautifulSoup
import requests
import re

r=requests.get('http://mpk.wroc.pl/kontrole-biletow').text


#print(r)

soup=BeautifulSoup(r,'html.parser')
ss=soup.select_one('span[class="date-display-single"]')
print("Możliwe dzisiaj kontrole " , str(ss.string).strip())
datetab=soup.find_all("span class","date")
routestab=soup.find_all("td", class_="views-field views-field-title")

parsed_d=[]
parsed_r=[]

for r in routestab:
    parsed_r.append((str(r.string).strip()))

for d in datetab:
    parsed_d.append((str(d.string).strip()))

for k,v in zip(parsed_d,parsed_r):
    print(k + '-'+ v)