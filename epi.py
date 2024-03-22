import openpyxl
from time import sleep
from re import findall, split
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

keywords = ["Принтер етикеток і чеків", "Принтер етикеток","Детектор валют", "Принтер linerless етикеток","Принтер браслетів","Принтер-аплікатор","Детектор валют","Детектор валюти","Лічильник банкнот","Сортувальник банкнот",
            'Принтер чеків', 'Термопринтер','Портативний принтер','POS-принтер','POS-прінтер', 'Настольный принтер этикеток','Промышленный принтер этикеток','Мобильный принтер', 'Мобильный принтер','Принтер этикеток','Принтер чеков и этикеток',
            'Принтер чеков', 'Счетчик банкнот','Термотрансферний принтер','Мобільний принтер для друку етикетки та чеків', 'Принтер для друку етикеток і штрих-коду']
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
data = []
url = f"https://gipercenter.kiev.ua/ua/g97469047-nastolnye?bss0=25916&bss0=202701&presence_available=true"
r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(r.text, 'lxml')
n_elemnts = soup.find('div', class_="row row-products")
'''price = soup.find('span', class_="card__price-sum")
Z = soup.find('div', class_="card__info")
price = Z.find('span',class_="card__price-sum").text.strip()
name = Z.find('h2', class_="font-weight-700 nc").text.strip()'''
V = soup.findAll('li', class_="ProductList__item--d3K92 js-rtb-partner js-productad")
OZ =  soup.find('div', class_="Block__ui_margin-top_xs--JYF_i Block__ui_margin-right_xs--zwvwn Block__ui_margin-bottom_xs--JVahY Block__ui_margin-left_xs--S129n").find('span', class_="Text__ui_text_size_xl--hiLG7")
Old = soup.find('p', class_="Text__ui_text_size_xs--GXoZP Text__ui_text_decoration_line-through--lN0mm")
Z =  soup.findAll('div', class_="Block__ui_margin-top_xs--JYF_i Block__ui_margin-right_xs--zwvwn Block__ui_margin-bottom_xs--JVahY Block__ui_margin-left_xs--S129n")
New = soup.findAll('span', class_="Text__ui_text_size_xl--hiLG7")
#print(New)
#print (Z)
name = soup.findAll('p', class_="Item__title--g7_es")
#print(name)
#print(price)
n_elemnts = soup.findAll('div', class_="cs-product-gallery__image-wrap")
print(soup)
header = ['Kategoria','marka','model','TP',"dpi", 'name', 'price', 'sale', 'firm'] 
df = pd.DataFrame(data, columns=header)
workbook = openpyxl.Workbook()                      
worksheet = workbook.active
worksheet.append(header)
for row in data:
    worksheet.append(row)
workbook.save(r'14.7.xlsx')
