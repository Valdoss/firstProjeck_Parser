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
            'Принтер чеков', 'Счетчик банкнот','Термотрансферний принтер','Мобільний принтер для друку етикетки та чеків', 'Принтер для друку етикеток і штрих-коду',  'Принтер мобільний',
            'Принтер пластикових карток', 'Сортировщик банкнот']
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
data = []
start_time = time.time()
for p in range(1, 5):
    # Обладнання для друку етикеток Reef 
    print(p)
    url = f"https://shop.reef.ua/ua/obladnannya-dlya-druku-etiketok/mfp/20-,%D0%9C%D0%BE%D0%B1%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9,%D0%9D%D0%B0%D1%81%D1%82%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9,%D0%9F%D1%80%D0%BE%D0%BC%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B9/manufacturers,bixolon,godex,hprt,zebra-motorola-symbol2/page-{p}/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    product_elements = soup.find_all('div', class_="product w-shipping")
    for element in product_elements:
        name_link = element.find('a', class_="product-title")
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
        price_element = element.find('p', class_= 'current')
        price = price_element.text.strip()
        s_name = "reef"
        ac_price = "-"  
        try:
            parts = remaining_name.split(" ")
            mod = parts[0]
        except:
           if remaining_name is mod:
                remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
                parts = remaining_name.split("dpi")
                # Извлечь все после dpi
                remaining_name = parts[1].strip()  # Удаление пробелов
                # Извлечь все до dpi и сам dpi
                dpi = parts[0]
        except:
            d  = remaining_name
        dpi = dpi.replace("(", "")
        index = remaining_name.find(")")
        remaining_name = remaining_name[:index] + remaining_name[index + 1:]
# Проверить первый символ
        try:
            if remaining_name[0] == ",":
                # Удалить первый символ
                remaining_name = remaining_name[1:]
        except:
            d = remaining_name
        remaining_name = remaining_name.strip()
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1, 3): #Обладнання для друку чеків Reef
    print(p)
    url = f"https://shop.reef.ua/ua/obladnannya-dlya-druku-chekiv/mfp/20-,%D0%9C%D0%BE%D0%B1%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9,%D0%9D%D0%B0%D1%81%D1%82%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9/manufacturers,bixolon,godex,hprt/page-{p}/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    product_elements = soup.find_all('div', class_="product w-shipping")
    for element in product_elements:
        name_link = element.find('a', class_="product-title")
        name = name_link.text.strip()
        for key in keywords:           
            if key.lower() in name.lower():
                kategoria = key
                break  
        else: 
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
        price_element = element.find('p', class_= 'current')
        price = price_element.text.strip()
        s_name = "reef"
        ac_price = "-"  
        try:
            parts = remaining_name.split(" ")
            mod = parts[0]
            if remaining_name == mod:
                remaining_name 
        except:
            mod = mod
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
                parts = remaining_name.split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1, 2): #Банківське обладнання Reef
    print(p)
    url = f"https://shop.reef.ua/ua/bankivske-obladnannia/mfp/manufacturers,nrj/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    product_elements = soup.find_all('div', class_="product w-shipping")
    for element in product_elements:
        name_link = element.find('a', class_="product-title")
        name = name_link.text.strip()
        if name == 'Акумуляторна батарея для детектора валют NRJ':
            break
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
        price_element = element.find('p', class_= 'current')
        price = price_element.text.strip()
        s_name = "reef"
        ac_price = "-"  
        try:
            parts = remaining_name.split(" ")
            mod = parts[0]
            if remaining_name == mod:
                remaining_name
        except:
            mod = mod
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
                parts = remaining_name.split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
        print ('-')

for p in range(1,4): # ПРИНТЕРИ ЕТИКЕТОК  Brain
    url = f"https://brain.com.ua/ukr/category/Printeri_etiketok-c329/filter=3-21503580000,3-21515490000,3-21516930000,3-75029600000;filterbyavail=active;page={p}/"
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('div', class_="col-md-12 product-wrapper")
    ac_price = ''
    for element in n_elemnts:
        price = element.find('span', itemprop="price").text.strip()
        name = element.find('h3', class_="category-product-name").text.strip()
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
        s_name = 'brain'
        pattern = r"(?:код товару:\s+)(.*)"
        remaining_name = re.sub(pattern, "", remaining_name)
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
                # Разделить строку по "dpi"
                parts = remaining_name.lower().split("dpi")
                    # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
            # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
            # Объединить цифры в строку
        dpi = "".join(digits)
            # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):    # ДЕТЕКТОРИ ВАЛЮТ Brain
    url = f"https://brain.com.ua/ukr/category/Detektori_valyut-c1082/filter=3-21577030000;filterbyavail=active/"
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('div', class_="col-md-12 product-wrapper")
    ac_price = ''
    for element in n_elemnts:
        price = element.find('span', itemprop="price").text.strip()
        name = element.find('h3', class_="category-product-name").text.strip()
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
        s_name = 'brain'
        pattern = r"(?:код товару:\s+)(.*)"
        remaining_name = re.sub(pattern, "", remaining_name)
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
                # Разделить строку по "dpi"
                parts = remaining_name.lower().split("dpi")
                    # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
            # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
            # Объединить цифры в строку
        dpi = "".join(digits)
            # Объединить буквы в строку
        tp = "".join(letters)
        if mod is None or mod == '-':
             break
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])

for p in range(1,3): # ПРИНТЕРИ ЧЕКІВ Brain 
    url = f"https://brain.com.ua/ukr/category/Printeri_chekiv-c335/filter=3-21515490000,3-21516930000,3-75029600000;filterbyavail=active;page={p}/"
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('div', class_="col-md-12 product-wrapper")
    ac_price = ''
    for element in n_elemnts:
        price = element.find('span', itemprop="price").text.strip()
        name = element.find('h3', class_="category-product-name").text.strip()
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
        s_name = 'brain'
        pattern = r"(?:код товару:\s+)(.*)"
        remaining_name = re.sub(pattern, "", remaining_name)
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
                # Разделить строку по "dpi"
                parts = remaining_name.lower().split("dpi")
                    # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
            # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
            # Объединить цифры в строку
        dpi = "".join(digits)
            # Объединить буквы в строку
        tp = "".join(letters)
        if mod is None or mod == '-':
             break
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])

for p in range(1,2):  # Принтери етикеток Rozetka
    url = f"https://rozetka.com.ua/ua/printery-etiketok/c4625268/producer=bixolon,godex,hprt,zebra1;seller=rozetka/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
            price = element.find('div', class_='goods-tile__price--old price--gray ng-star-inserted').text.strip()
        except:
            if element.find('span', class_="goods-tile__price-value") != None:
                price = element.find('span', class_="goods-tile__price-value").text.strip()
            else :
                break
        try :
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
        except:
            ac_price = ''
        if ac_price == price:
            ac_price =''
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
        s_name = 'rozetka'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):  #Лічильники банкнот і детектори валют Rozetka
    url = f"https://rozetka.com.ua/ua/counters_and_currency_detectors/c754404/producer=nrj;seller=rozetka;state=new/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
            price = element.find('div', class_='goods-tile__price--old price--gray ng-star-inserted').text.strip()
        except:
            price = element.find('span', class_="goods-tile__price-value").text.strip()
        try :
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
        except:
            if element.find('span', class_="goods-tile__price-value") != None:
                price = element.find('span', class_="goods-tile__price-value").text.strip()
            else :
                break
        if ac_price == price:
            ac_price = ''
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
        s_name = 'rozetka'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):   # POS-принтери Rozetka
    url = f"https://rozetka.com.ua/ua/pos-printery/c4625319/producer=bixolon,hprt;seller=rozetka/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
            price = element.find('div', class_='goods-tile__price--old price--gray ng-star-inserted').text.strip()
        except:
            if element.find('span', class_="goods-tile__price-value") != None:
                price = element.find('span', class_="goods-tile__price-value").text.strip()
            else :
                break
        try :
            ac_price = element.find('span', class_="goods-tile__price-value").text.strip()
        except:
            ac_price = ''
        if ac_price == price:
            ac_price =''
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
        s_name = 'rozetka'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])


for p in range(1,3) :   #  Принтери етикеток Epicentr
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
        name = element.find('div', class_="card__name").text.strip()
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
for p in range(1,2):    #   Принтери чеків Epicentr
    url =  f'https://epicentrk.ua/ua/shop/printery-chekov/filter/seller-is-epicentr/brand-is-17b16564dba245d6b361e1ff72b6e57f-or-63e4571d0d6a4ec68ae73fe2c464d150/apply/'
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts =soup.findAll('div', class_="card__info")
    for element in n_elemnts:
        try:
            price = element.find('span',class_="card__price-sum").text.strip()
        except:
            break
        name = element.find('div', class_="card__name").text.strip()
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
for p in range(1,2):    # Детектори валют Epicentr
    url = f'https://epicentrk.ua/ua/shop/detektory-valyut/filter/seller-is-epicentr/brand-is-253bd6381334407c9b875c3783d38a0c/apply/'
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts =soup.findAll('div', class_="card__info")
    for element in n_elemnts:
        try:
            price = element.find('span',class_="card__price-sum").text.strip()
        except:
            break
        name = element.find('div', class_="card__name").text.strip()
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
# Товари Megapos
megapos = [
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-ez-g500',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-g500-usbrs232ethernet',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-g530-usb',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-ez-dt2-plus',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-ez-dt4-plus',
    'https://megapos.com.ua/uk/mobilnyj-printer-godex-mx30i-wifi',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-rt730i',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-rt863i',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-ez-2250i',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-ez6250i',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-gx4200i',
    'https://megapos.com.ua/uk/mobilnyj-printer-godex-mx30',
    'https://megapos.com.ua/uk/mobilnyj-printer-godex-mx30i',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-rt-200',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-zx-1200i',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-zx-420i',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-zebra-tlp2824',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-zebra-tlp2824',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-zebra-zd220-dt',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-zebra-zd220-tt',
    'https://megapos.com.ua/uk/zebra-zd230-dt',
    'https://megapos.com.ua/uk/zebra-zd411t',
    'https://megapos.com.ua/uk/zebra-zd421t-zd4a042-30ee00ez',
    'https://megapos.com.ua/uk/zebra-zd421t-zd4a042-30ee00ez',
    'https://megapos.com.ua/uk/zebra-zd421t-zd4a042-30em00ez',
    'https://megapos.com.ua/uk/zebra-zd421-zd42042-t0ee00ez',
    'https://megapos.com.ua/uk/zebra-zd421d',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-zebra-zt411',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-rt730i',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-bp520',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-ez120',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-godex-ez130',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-godex-zx-430i',
    'https://megapos.com.ua/uk/zebra-zd410-zd41022-d0ew02ez',
    'https://megapos.com.ua/uk/zebra-zd420d-zd42043-d0ee00ez',
    'https://megapos.com.ua/uk/printer-etiketok-dlja-markirovki-meditsinskoj-tary-godex-gtl-100',
    'https://megapos.com.ua/uk/mobilnyj-printer-godex-mx20',
    'https://megapos.com.ua/uk/mobilnyj-printer-hprt-mt800',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-bixolon-slp-dl410cg',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-l3000-usbbluetooth',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-l3000',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-s300los',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-bixolon-xd3-40dek-usbrs-232ethernet',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-bixolon-xd3-40dk',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-bixolon-xq-840',
    'https://megapos.com.ua/uk/promyshlennyj-printer-etiketok-bixolon-xt5-43d9s-s-otdelitelem-i-smotchikom',
    'https://megapos.com.ua/uk/mobilnyj-printer-hprt-hm-z3',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-hprt-ht100',
    'https://megapos.com.ua/uk/nastolnyj-printer-etiketok-hprt-ht330',
    'https://megapos.com.ua/uk/printer-chekov-hprt-lpq58',
    'https://megapos.com.ua/uk/printer-chekov-hprt-lpq80',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-xm7-20',
    'https://megapos.com.ua/uk/printer-chekov-hprt-lpq58',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r200iii-wkl',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r310bk',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r310-wkl-wifi',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r310-wk',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-350iii',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-380-ii-cosk-usbrs-232',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-e300-esk',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-q200',
    'https://megapos.com.ua/uk/printer-chekov-hprt-ppt2-a',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp585-usb',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp585-usbbluetooth',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp808',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp809',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp80k',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp80k-l',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r200iii',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r310-wk',
    'https://megapos.com.ua/uk/mobilnyj-printer-bixolon-spp-r310bk',
    'https://megapos.com.ua/uk/printer-chekov-bixolon-srp-380-ii-coek-usbrs-232',
    'https://megapos.com.ua/uk/printer-chekov-hprt-ppt2-a',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp805l',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp806-usbwi-fi',
    'https://megapos.com.ua/uk/printer-chekov-hprt-tp809',
    'https://megapos.com.ua/uk/schetchik-banknot-nrj-al-955-uv-mg-ir'
]
for url in megapos:
    price =''
    ac_price =''
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue  
    soup = BeautifulSoup(response.text, 'lxml')
    try: 
        if soup.find('span', class_="price-old") is None:
            price_element = soup.find('div', class_="price")
            price = price_element.text.strip()
        else:
            price_element = soup.find('span', class_="price-old")
            price = price_element.text.strip()
            ac_price = soup.find('span',class_="price-new")
            ac_price = ac_price.text.strip()
    except AttributeError:
        price
    try:
        price = re.findall(r"Ціна:\s*(.*?)\s*грн", price)[0]
    except:
        price
    name_link = soup.find('h1', style="margin-top:0px;margin-bottom:8px;")
    name = name_link.text.strip()  
    for key in keywords:
            if key.lower() in name.lower():
                kategoria = key
                break  
    else: 
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
    s_name = 'megapos'
    pattern = r"(?:код товару:\s+)(.*)"
    remaining_name = re.sub(pattern, "", remaining_name)
    parts = remaining_name.split(" ")
    mod = parts[0]
    if remaining_name == mod:
        remaining_name 
    l1 = remaining_name.split()
    remaining_name = " ".join(l1[1:])
    dpi = ""
    try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
    price = "".join(numbers)
    if ac_price != None:
        numbers = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers)
        # Найти все цифры
    digits = re.findall(r"\d+", dpi)
        # Найти все буквы
    letters = re.findall(r"[a-zA-Z]", dpi)
    dpi = "".join(digits)
    tp = "".join(letters) 
    data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
# Товари technologic
technologic = [
    'https://technologic.ua/cat/nastolnye-printery-etiketok/filter-brands-is-godex-taiwan-or-hprt/',
    'https://technologic.ua/cat/promyshlennye-printery-etiketok/filter-brands-is-godex-taiwan/',
    'https://technologic.ua/cat/stacionarnye-printery-chekov/filter-brands-is-hprt/',
    'https://technologic.ua/cat/schetchiki-banknot/filter-brands-is-nrj/'
]
for url in technologic:

    for p in range(1,2):  # Настольные принтеры этикеток technologic
    
        r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(r.text, 'lxml')
        ac_price = ''
        n_elemnts = soup.findAll('div', class_="product-card")
        for element in n_elemnts:
            try:
                name = element.find('h3', class_="product-card--name").text.strip()
            except:
                name='-'
            try:
                price = element.find('div', class_="product-card--price-actual").text.strip()
            except:
                price = '-'
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
            s_name = 'technologic'
            parts = remaining_name.split(" ")
            mod = parts[0]
            if remaining_name == mod:
                remaining_name 
            l1 = remaining_name.split()
            remaining_name = " ".join(l1[1:])
            dpi = ""
            try:
                # Разделить строку по "dpi"
                parts = remaining_name.lower().split("dpi")
                    # Извлечь все после dpi
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
            price = "".join(numbers)
            numbers1 = re.findall(r"\d+", ac_price)
            ac_price = "".join(numbers1)
                # Найти все цифры
            digits = re.findall(r"\d+", dpi)
            # Найти все буквы
            letters = re.findall(r"[a-zA-Z]", dpi)
            # Объединить цифры в строку
            dpi = "".join(digits)
            # Объединить буквы в строку
            tp = "".join(letters)
            data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
        
    #   Товари fornit
fornit = [
    'https://fornit.com.ua/printer-godex-g500-bez-setevoy-karty/',
    'https://fornit.com.ua/termotransfernyi-prynter-godex-g500-usbrs232-ethernet/',
    'https://fornit.com.ua/printer-godex-g530-usb/',
    'https://fornit.com.ua/termotransfernyi-prynter-godex-g530-ethernet/',
    'https://fornit.com.ua/termoprynter-etyketok-godex-dt2x-usbrs232ethernet/',
    'https://fornit.com.ua/termotransfernyy-printer-godex-rt700i/',
    'https://fornit.com.ua/termotransfernyy-printer-godex-rt863i/',
    'https://fornit.com.ua/printer-godex-ez2350i/',
    'https://fornit.com.ua/termotransfernyy-printer-etiketok-godex-rt200/',
    'https://fornit.com.ua/termotransfernyy-printer-zebra-tpl-2824-plus/',
    'https://fornit.com.ua/prynter-zebra-zd220/',
    'https://fornit.com.ua/prynter-etyketok-zebra-zd230-203-dpi-zd23042-d0ec00ez-usb-ethernet/',
    'https://fornit.com.ua/termoprinter-zebra-zd41022-bluetooth/',
    'https://fornit.com.ua/prynter-etyketok-zebra-zd421-zd4a042-30ee00ez-termotransfernyi-usbethernetbt/',
    'https://fornit.com.ua/termotransfernyi-prynter-godex-ez120/',
    'https://fornit.com.ua/termotransfernyy-printer-godex-ez130/',
    'https://fornit.com.ua/shirokiy-termotransfernyy-printer-pechati-a4-formata-godex-hd830i/',
    'https://fornit.com.ua/lichylnyk-banknot-nrj-al-5100-uv/',
    'https://fornit.com.ua/profesiinyi-lichylnyk-banknot-iz-funktsiieiu-sortuvannia-nrj-al-955-uv/',
    'https://fornit.com.ua/printer-dlya-pechati-etiketok-slp-dl410/',
    'https://fornit.com.ua/prynter-etyketok-bixolon-xd3-40dk-usb/',
    'https://fornit.com.ua/termotransfernyi-prynter-bixolon-xd3-40tek/',
    'https://fornit.com.ua/prynter-etyketok-bixolon-xm7-20iwk-bluetooth-wi-fi/',
    'https://fornit.com.ua/mobilnyi-prynter-dlia-druku-etyketky-ta-chekiv-hprt-hm-z3-bluetoothusbrs232/',
    'https://fornit.com.ua/termotransfernyy-printer-hprt-ht100/',
    'https://fornit.com.ua/termotransfernyy-printer-hprt-ht300/',
    'https://fornit.com.ua/termotransfernyi-prynter-hprt-ht330/',
    'https://fornit.com.ua/termoprynter-etyketok-hprt-lpq58/',
    'https://fornit.com.ua/prynter-etyketok-bixolon-xm7-20iwk-bluetooth-wi-fi/',
    'https://fornit.com.ua/promyshlennyy-etiketochnyy-printer-bixolon-xt5-40s/',
    'https://fornit.com.ua/termoprynter-etyketok-hprt-lpq58/',
    'https://fornit.com.ua/printer-chekov-bixolon-srp-350iii-s-funktsiey-avtomaticheskogo-masshtabirovaniya-cheka-ot-100-do-75/',
    'https://fornit.com.ua/prynter-chekiv/',
    'https://fornit.com.ua/mobilnyy-printer-pechati-chekov-hprt-mpt2/',
    'https://fornit.com.ua/prynter-chekiv-hprt-ppt2-a/',
    'https://fornit.com.ua/prynter-chekiv-hprt-tp80k/'
]
for p in range(1,4):    #   Товари fornit
    
    url = f"https://fornit.com.ua/katalog/filter/brand=95,96,99,160;page={p};price=1150-445000/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('li', class_="catalog-grid__item")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="catalogCard-title").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="catalogCard-oldPrice").text.strip()
        except:
            price = element.find('div', class_="catalogCard-price").text.strip()
        try:
            ac_price = element.find('div', class_="catalogCard-price").text.strip()
        except:
            ac_price =''
        if ac_price == price:
            ac_price =''
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
        s_name = 'fornit'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
print('m')
for p in range(1,2):  # Настольные принтеры этикеток postorg
    url = f"https://postorg.com.ua/category/nastolnye/?proizvoditel%5B%5D=233&proizvoditel%5B%5D=268&proizvoditel%5B%5D=275"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-lg-12 flexdiscount-product-wrap 3")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="line-product-name").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="price").text.strip()
        except:
            price = '-'
        
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
        s_name = 'postorg'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        # price = price.split(".")
        price = price[:price.find(".")]
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):  #  Принтер Чеків-етикеток этикеток postorg
    url = f"https://postorg.com.ua/category/chekov-etiketok/?proizvoditel%5B%5D=275"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-lg-12 flexdiscount-product-wrap 3")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="line-product-name").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="price").text.strip()
        except:
            price = '-'
        
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
        s_name = 'postorg'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        # price = price.split(".")
        price = price[:price.find(".")]
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):  # Промышленный принтер этикеток postorg
    url = f"https://postorg.com.ua/category/promyshlennye/?proizvoditel%5B%5D=233&proizvoditel%5B%5D=268"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-lg-12 flexdiscount-product-wrap 3")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="line-product-name").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="price").text.strip()
        except:
            price = '-'
        
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
        s_name = 'postorg'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        # price = price.split(".")
        price = price[:price.find(".")]
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):  # Настільні принтери чеків postorg 
    url = f"https://postorg.com.ua/category/nastolnye-printery-chekov/?proizvoditel%5B%5D=233&proizvoditel%5B%5D=275"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-lg-12 flexdiscount-product-wrap 3")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="line-product-name").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="price").text.strip()
        except:
            price = '-'
        
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
        s_name = 'postorg'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        # price = price.split(".")
        price = price[:price.find(".")]
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2):  # Мобільні принтери чеків postorg
    url = f"https://postorg.com.ua/category/mobilnye-printery-chekov/?proizvoditel%5B%5D=233&proizvoditel%5B%5D=275"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-lg-12 flexdiscount-product-wrap 3")
    for element in n_elemnts:
        try:
            name = element.find('div', class_="line-product-name").text.strip()
        except:
            name='-'
        try:
            price = element.find('div', class_="price").text.strip()
        except:
            price = '-'
        
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
        s_name = 'postorg'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        # price = price.split(".")
        price = price[:price.find(".")]
        numbers = re.findall(r"\d+", price)
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2): # Принтеры чеков 600dpi  
    url = f"https://600dpi.com.ua/printery-chekov/brand-bixolon-or-godex-or-hprt-or-zebra"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-xs-6 col-sm-6 col-md-4 col-lg-3")
    for element in n_elemnts:
        try :
            Z = element.find('div', class_="unavailable hidden").text.strip()
        except:
            Z = None
        if Z == None:
            break
        try:
            name = element.find('div', class_="product-cut__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_= "product-price__old-value").text.strip()
        except:
            price = element.find('span', class_="product-price__main-value").text.strip()
        try:
            ac_price = element.find('span', class_="product-price__main-value").text.strip()
        except:
            ac_price = ''
        if ac_price == price :
            ac_price = ''
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
        s_name = '600dpi'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
        
for p in range(1,2):  # Принтеры этикеток 600dpi
    url = f"https://600dpi.com.ua/printery-etiketok/brand-bixolon-or-godex-or-hprt"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-xs-6 col-sm-6 col-md-4 col-lg-3")
    for element in n_elemnts:
        try :
            Z = element.find('div', class_="unavailable hidden").text.strip()
        except:
            Z = None
        if Z == None:
            break
        '''name =  element.find('span', class_="goods-tile__title").find('span').text.strip()'''
        try:
            name = element.find('div', class_="product-cut__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_= "product-price__old-value").text.strip()
        except:
            price = element.find('span', class_="product-price__main-value").text.strip()
        try:
            ac_price = element.find('span', class_="product-price__main-value").text.strip()
        except:
            ac_price = ''
        if ac_price == price :
            ac_price = ''
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
        s_name = '600dpi'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
for p in range(1,2): # Счетчики банкнот 600dpi 
    url = f"https://600dpi.com.ua/schetchiki-banknot/brand-nrj"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    ac_price = ''
    n_elemnts = soup.findAll('div', class_="col-xs-6 col-sm-6 col-md-4 col-lg-3")
    for element in n_elemnts:
        try :
            Z = element.find('div', class_="unavailable hidden").text.strip()
        except:
            Z = None
        if Z == None:
            break
        try:
            name = element.find('div', class_="product-cut__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_= "product-price__old-value").text.strip()
        except:
            price = element.find('span', class_="product-price__main-value").text.strip()
        try:
            ac_price = element.find('span', class_="product-price__main-value").text.strip()
        except:
            ac_price = ''
        if ac_price == price :
            ac_price = ''
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
        s_name = '600dpi'
        parts = remaining_name.split(" ")
        mod = parts[0]
        if remaining_name == mod:
            remaining_name 
        l1 = remaining_name.split()
        remaining_name = " ".join(l1[1:])
        dpi = ""
        try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
        price = "".join(numbers)
        numbers1 = re.findall(r"\d+", ac_price)
        ac_price = "".join(numbers1)
            # Найти все цифры
        digits = re.findall(r"\d+", dpi)
        # Найти все буквы
        letters = re.findall(r"[a-zA-Z]", dpi)
        # Объединить цифры в строку
        dpi = "".join(digits)
        # Объединить буквы в строку
        tp = "".join(letters)
        data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
    
    # Товари torgsoft
torgsoft = [
    'https://store.torgsoft.ua/printer-etiketok-godex-godex-dt-2/',
    'https://store.torgsoft.ua/printer-unversalniy-hprt-lpq58/',
    'https://store.torgsoft.ua/hprt-tp80c/',
    'https://store.torgsoft.ua/printer-chekov-bixolon-srp-e300/',
    'https://store.torgsoft.ua/printer-chekov-bixolon-srp-330ii/' 
]
for url in torgsoft:
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue  
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        price = soup.find('span', class_="full_card_new_price p_price").text.strip()   
    except:
        ac_price = "-"  
    try:
        name_link = soup.find('div', class_="m_tovar_info_head_left").find('h1')
        name = name_link.text.strip()  
    except:
        name
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
    s_name = 'torgsoft'
    pattern = r"(?:код товару:\s+)(.*)"
    remaining_name = re.sub(pattern, "", remaining_name)
    parts = remaining_name.split(" ")
    mod = parts[0]
    if remaining_name == mod:
        remaining_name 
    l1 = remaining_name.split()
    remaining_name = " ".join(l1[1:])
    dpi = ""
    try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
    parts = price.split(",")
    price = parts[0]
    def remove_all_except_digits_and_dots(price):
            return re.sub(r"[^\d.]", "", price)
    price = remove_all_except_digits_and_dots(price)
    remaining_name = remaining_name.strip()
    numbers = re.findall(r"\d+", price)
    price = "".join(numbers)
    digits = re.findall(r"\d+", dpi)
    letters = re.findall(r"[a-zA-Z]", dpi)
    dpi = "".join(digits)
    tp = "".join(letters)
    ac_price = ''
    data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
    # Товари Гиперцентр
gipercentrKIEV = [
    'https://gipercenter.kiev.ua/ua/p1414283734-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283732-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285798-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285800-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283749-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285794-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285792-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285875-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285816-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283674-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285804-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285812-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285815-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285813-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285753-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285799-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414285809-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283690-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414285849-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283514-printer-etiketok-chekov.html',
    'https://gipercenter.kiev.ua/ua/p1414283517-printer-etiketok-chekov.html',
    'https://gipercenter.kiev.ua/ua/p1414283736-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283694-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1425897934-printer-dlya-pechati.html',
    'https://gipercenter.kiev.ua/ua/p1414283689-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1425897913-godex-zx420i.html',
    'https://gipercenter.kiev.ua/ua/p1414285814-printer-etiketok-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283692-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1414283695-printer-etiketok-godex.html',
    'https://gipercenter.kiev.ua/ua/p1239670289-printer-etiketok-dlya.html',
    'https://gipercenter.kiev.ua/ua/p1414283672-printer-etiketok-chekov.html',
    'https://gipercenter.kiev.ua/ua/p1414283561-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283548-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283560-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283546-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283563-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283549-printer-chekov-hprt.html',
    'https://gipercenter.kiev.ua/ua/p1414283521-printer-chekov-bixolon.html',
    'https://gipercenter.kiev.ua/ua/p1414283562-printer-chekov-hprt.html']
for url in gipercentrKIEV:
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue  
    soup = BeautifulSoup(response.text, 'lxml')
    price =''
    try:
        price = soup.find('span', class_="Text__ui_text_size_x7l--cgh_a Text__ui_text_font-weight_bold--qRTru").text.strip()   
        ac_price = ''
    except:
        if price != None:
            try:
                price =  soup.find('span', class_="Text__ui_text_size_xs--GXoZP Text__ui_text_decoration_line-through--lN0mm").text.strip()   
            except:
                 break
        ac_price = soup.find('span',class_="Text__ui_text_size_x7l--cgh_a").text.strip()
      
    name_link = soup.find('h1',class_="Text__ui_text_size_xl--hiLG7 Text__ui_text_line-height_m--I9dbv Text__ui_text_font-weight_bold--qRTru")
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
    s_name = 'gipercentr'
    pattern = r"(?:код товару:\s+)(.*)"
    remaining_name = re.sub(pattern, "", remaining_name)
    parts = remaining_name.split(" ")
    mod = parts[0]
    if remaining_name == mod:
        remaining_name 
    l1 = remaining_name.split()
    remaining_name = " ".join(l1[1:])
    dpi = ""
    try:
            # Разделить строку по "dpi"
            parts = remaining_name.lower().split("dpi")
                # Извлечь все после dpi
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
    parts = price.split(",")  # Розделение по коме
    price = parts[0]
    def remove_all_except_digits_and_dots(price):
            return re.sub(r"[^\d.]", "", price)
    price = remove_all_except_digits_and_dots(price)
    remaining_name = remaining_name.strip()
    numbers = re.findall(r"\d+", price)
    price = "".join(numbers)
    digits = re.findall(r"\d+", dpi)
    letters = re.findall(r"[a-zA-Z]", dpi)
    dpi = "".join(digits)
    tp = "".join(letters)
    data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
header = ['Kategoria','marka','model','TP',"dpi", 'name', 'price', 'sale', 'firm'] 
df = pd.DataFrame(data, columns=header)
workbook = openpyxl.Workbook()                      
worksheet = workbook.active
worksheet.append(header)
for row in data:
    worksheet.append(row)
workbook.save(r'14.5.xlsx')
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")