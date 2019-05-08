from bs4 import BeautifulSoup
import requests

r=requests.get('http://mpk.wroc.pl/kontrole-biletow').text


#print(r)

soup=BeautifulSoup(r,'html.parser')

for date in soup.find_all(class=):
    print(date.get(''))
