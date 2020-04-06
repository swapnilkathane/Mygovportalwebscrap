import requests
from bs4 import BeautifulSoup

site=requests.get('https://www.mygov.in/covid-19/')
soup=BeautifulSoup(site.text, 'html.parser')
a=soup.prettify()
#print(a)
title=soup.title.text
print(title)
#print(" ")
A=soup.find('div',class_='info_title')
print(A.text)
DB=soup.find_all(class_="icount")
#print(DB)
N=soup.find_all('div',class_='info_label')
res={N[i].text : DB[i].text for i in range(len(DB))}
print(res)


