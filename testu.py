import openpyxl
from time import sleep
from re import findall, split
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
url = "https://brain.com.ua/ukr/category/Marshrutyzatory-c1333-143/"
keywords = ["Принтер етикеток і чеків", "Принтер етикеток","Детектор валют", "Принтер linerless етикеток","Принтер браслетів","Принтер-аплікатор","Детектор валют","Детектор валюти","Лічильник банкнот","Сортувальник банкнот",
            'Принтер чеків', 'Термопринтер','Портативний принтер','POS-принтер','POS-прінтер', 'Настольный принтер этикеток','Промышленный принтер этикеток','Мобильный принтер', 'Мобильный принтер','Принтер этикеток','Принтер чеков и этикеток',
            'Принтер чеков', 'Счетчик банкнот','Термотрансферний принтер','Мобільний принтер для друку етикетки та чеків', 'Принтер для друку етикеток і штрих-коду']
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
data = []
start_time = time.time()



z ='''for url in epicentr:
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        name_link = soup.find('div', class_="_tpM6 _DRP-")
        name = name_link.text.strip()
        for key in keywords:
            if key.lower() in name.lower():
                kategoria = key
                break  # Exit the loop after finding a match
        else:  # No match found, set category to empty
            kategoria = ""
        split_name = split(r"(?:{})".format("|".join(keywords)), name, flags=re.IGNORECASE)
        if len(split_name) > 1:
            remaining_name = split_name[1].strip()
        else:
            remaining_name = name
        markat = split(r"(?:{})".format("|".join(firm)), remaining_name, flags=re.IGNORECASE)
        if len(markat) > 1:
            remaining_name = markat[1].strip()
        else:      
            marka = remaining_name
        for key in firm:
            if key.lower() in name.lower():
                marka = key
                break  # Exit the loop after finding a match
            else:  # No match found, set category to empty
                marka = ""
        try:
            price = soup.find('p', class_="product-price__small ng-star-inserted").text.strip()
        except:
            ac_price = "-"
        try:
            price_element = soup.find('div', class_='_YkdM _J5fD')
            price = price_element.text.strip()
        except:
            price_element = soup.find('p', class_="product-price__big")
            if price_element:
                ac_priceprice = price_element.text.strip()
            else:
                price
        s_name = 'epicentr'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            parts = remaining_name.lower().split("dpi")
            remaining_name = parts[1].strip()  # Удаление пробелов
                # Извлечь все до dpi и сам dpi
            dpi = parts[0] 
        except:
            d  = remaining_name
        dpi = dpi.replace("(", "")
        index = remaining_name.find(")")
        remaining_name = remaining_name[:index] + remaining_name[index + 1:]
        try:
                if remaining_name[0] == ",":
                # Удалить первый символ
                    remaining_name = remaining_name[1:]
        except:
            d = remaining_name
        remaining_name = remaining_name.strip()
        numbers = re.findall(r"\d+", price)
        def remove_all_except_digits_and_dots(price):
            return re.sub(r"[^\d.]", "", price)
        price = remove_all_except_digits_and_dots(price)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        letters = re.findall(r"[a-zA-Z]", dpi)
        dpi = "".join(digits)
        tp = "".join(letters)
        price = price.strip(".")
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue'''

for p in range(1,3) :
    print(p)
    url = f"https://epicentrk.ua/ua/shop/printery-etiketok/filter/seller-is-epicentr/brand-is-17b16564dba245d6b361e1ff72b6e57f-or-63e4571d0d6a4ec68ae73fe2c464d150-or-8b58f2bf69114d89aaf6862361cd5a4e/apply/?PAGEN_1={p}"
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts =soup.findAll('div', class_="card__info")
    for element in n_elemnts:
        try:
            price = element.find('span',class_="card__price-sum").text.strip()
        except:
            break
        name = element.find('h2', class_="font-weight-700 nc").text.strip()
        data.append([name , price])
for p in range(1,2):
    url =  f'https://epicentrk.ua/ua/shop/printery-chekov/filter/seller-is-epicentr/brand-is-17b16564dba245d6b361e1ff72b6e57f-or-63e4571d0d6a4ec68ae73fe2c464d150/apply/'
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts =soup.findAll('div', class_="card__info")
    for element in n_elemnts:
        try:
            price = element.find('span',class_="card__price-sum").text.strip()
        except:
            break
        name = element.find('h2', class_="font-weight-700 nc").text.strip()
        data.append([name , price])
for p in range(1,2):    
    url = f'https://epicentrk.ua/ua/shop/detektory-valyut/filter/seller-is-epicentr/brand-is-253bd6381334407c9b875c3783d38a0c/apply/'
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts =soup.findAll('div', class_="card__info")
    for element in n_elemnts:
        try:
            price = element.find('span',class_="card__price-sum").text.strip()
        except:
            break
        name = element.find('h2', class_="font-weight-700 nc").text.strip()
        data.append([name , price])

header = ['Kategoria', 'price'] 
df = pd.DataFrame(data, columns=header)
workbook = openpyxl.Workbook()                      
worksheet = workbook.active
worksheet.append(header)
for row in data:
    worksheet.append(row)
workbook.save(r'14.5.xlsx')
'https://epicentrk.ua/ua/shop/printery-etiketok/filter/seller-is-epicentr/brand-is-17b16564dba245d6b361e1ff72b6e57f-or-63e4571d0d6a4ec68ae73fe2c464d150-or-8b58f2bf69114d89aaf6862361cd5a4e/apply/?PAGEN_1=2'
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")
