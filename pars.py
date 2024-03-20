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
            'Принтер чеков', 'Счетчик банкнот','Термотрансферний принтер','Мобільний принтер для друку етикетки та чеків', 'Принтер для друку етикеток і штрих-коду',  'Принтер мобільний']
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
data = []
start_time = time.time()
for p in range(1, 5):
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
for p in range(1, 3):
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
for p in range(1, 2):
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

for p in range(1,4):
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
for p in range(1,2):
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

for p in range(1,3):
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
rozetka = [
    'https://rozetka.com.ua/ua/godex_18367/p226643395/',
    'https://rozetka.com.ua/ua/godex_14924/p44827600/',
    'https://rozetka.com.ua/ua/nrj-24331/p385385157/',
    'https://rozetka.com.ua/ua/godex_dt2x/p6809789/',
    'https://rozetka.com.ua/ua/godex_14923/p53194920/',
    'https://rozetka.com.ua/ua/godex_dt4x/p6809859/',
    'https://rozetka.com.ua/ua/godex_14642/p117200521/',
    'https://rozetka.com.ua/ua/godex_6090/p12539431/',
    'https://rozetka.com.ua/ua/godex_12245/p116428681/',
    'https://rozetka.com.ua/ua/godex_16098/p116321767/',
    'https://rozetka.com.ua/ua/godex_rt200/p6811084/',
    'https://rozetka.com.ua/ua/godex_9212/p12549287/',
    'https://rozetka.com.ua/ua/godex_10894/p12549742/',
    'https://rozetka.com.ua/ua/godex_7945/p12549826/',
    'https://rozetka.com.ua/ua/godex_14114/p26540521/',
    'https://rozetka.com.ua/ua/zebra_tlp2824/p6809499/',
    'https://rozetka.com.ua/ua/zebra_zd22042_d0eg00ez/p244402465/',
    'https://rozetka.com.ua/ua/zebra_zd22042_t0eg00ez/p244403095/',
    'https://rozetka.com.ua/ua/zebra-zd23042-d0ec00ez/p362019348/',
    'https://rozetka.com.ua/ua/zebra-902-zd4a022-d0ee00ez/p369070428/',
    'https://rozetka.com.ua/ua/zebra-zd4a022-d0em00ez/p381365148/',
    'https://rozetka.com.ua/ua/zebra-903-zd4a022-t0ee00ez/p369072771/',
    'https://rozetka.com.ua/ua/zebra-24987-/p404878533/',
    'https://rozetka.com.ua/ua/zebra_zd4a042-30em00ez/p362675073/',
    'https://rozetka.com.ua/ua/zebra-zd4a042-d0ee00ez/p419118792/',
    'https://rozetka.com.ua/ua/zebra-zd4a042-d0em00ez/p362019090/',
    'https://rozetka.com.ua/ua/zebra_zt41142_t0e0000z/p244396057/',
    'https://rozetka.com.ua/ua/godex_13598/p26557001/',
    'https://rozetka.com.ua/ua/zebra_zd41022_d0ew02ez/p147567547/',
    'https://rozetka.com.ua/ua/nrj-24475reef/p386195829/',
    'https://rozetka.com.ua/ua/nrj-22474/p398469600/',
    'https://rozetka.com.ua/ua/nrj-24473/p398468697/',
    'https://rozetka.com.ua/ua/nrj-23330/p385382175/',
    'https://rozetka.com.ua/ua/nrj-24331/p385385157/',
    'https://rozetka.com.ua/ua/nrj-25056/p414586275/',
    'https://rozetka.com.ua/ua/nrj-24903/p398649612/',
    'https://rozetka.com.ua/ua/nrj-24439reef/p385388274/',
    'https://rozetka.com.ua/ua/nrj-24332/p385386756/',
    'https://rozetka.com.ua/ua/hprt-18929/p366607512/',
    'https://rozetka.com.ua/ua/bixolon_12449/p26560265/',
    'https://rozetka.com.ua/ua/bixolon_17248/p117200563/',
    'https://rozetka.com.ua/ua/bixolon-17581reef/p363915249/',
    'https://rozetka.com.ua/ua/334038937/p334038937/',
    'https://rozetka.com.ua/ua/200272429/p200272429/',
    'https://rozetka.com.ua/ua/267861281/p267861281/',
    'https://rozetka.com.ua/ua/bixolon_17965/p194169452/',
    'https://rozetka.com.ua/ua/bixolon_17680/p194160996/',
    'https://rozetka.com.ua/ua/bixolon-19331/p363661329/',
    'https://rozetka.com.ua/ua/bixolon-21361/p363948714/',
    'https://rozetka.com.ua/ua/bixolon-21361/p363948714/',
    'https://rozetka.com.ua/ua/bixolon-21363reef/p363872115/',
    'https://rozetka.com.ua/ua/bixolon-21360/p363872118/',
    'https://rozetka.com.ua/ua/351595134/p351595134/',
    'https://rozetka.com.ua/ua/202004695/p202004695/',
    'https://rozetka.com.ua/ua/hprt_14250/p102080274/',
    'https://rozetka.com.ua/ua/hprt_13221_hprt/p106853703/',
    'https://rozetka.com.ua/ua/hprt-13222reef/p366606186/',
    'https://rozetka.com.ua/ua/hprt_10897/p13292589/',
    'https://rozetka.com.ua/ua/hprt_17086_lpq80/p107489526/',
    'https://rozetka.com.ua/ua/bixolon-21362reef/p363872124/',
    'https://rozetka.com.ua/ua/bixolon-21359/p363872121/',
    'https://rozetka.com.ua/ua/351596367/p351596367/',
    'https://rozetka.com.ua/ua/hprt_10897/p13292589/',
    'https://rozetka.com.ua/ua/bixolon_16424/p117183967/',
    'https://rozetka.com.ua/ua/bixolon_spp_r310bk_bluetooth_usb/p9349778/',
    'https://rozetka.com.ua/ua/bixolon_srp_350iiicog/p57445089/',
    'https://rozetka.com.ua/ua/bixolon_16458/p71657439/',
    'https://rozetka.com.ua/ua/bixolon-19315/p397260105/',
    'https://rozetka.com.ua/ua/bixolon-19324/p363773451/',
    'https://rozetka.com.ua/ua/hprt_14657/p231957523/',
    'https://rozetka.com.ua/ua/hprt_14656/p231960895/',
    'https://rozetka.com.ua/ua/348766902/p348766902/',
    'https://rozetka.com.ua/ua/hprt-22593reef/p365672016/',
    'https://rozetka.com.ua/ua/hprt-23403/p365666754/',
    'https://rozetka.com.ua/ua/hprt_8931/p11245630/',
    'https://rozetka.com.ua/ua/hprt_9540/p11245644/',
    'https://rozetka.com.ua/ua/hprt_14317/p53193648/',
    'https://rozetka.com.ua/ua/202012831/p202012831/',
    'https://rozetka.com.ua/ua/hprt_14316/p53193822/',
    'https://rozetka.com.ua/ua/hprt-24586-/p391069539/',
    'https://rozetka.com.ua/ua/hprt-22950/p365671056/',
    'https://rozetka.com.ua/ua/bixolon_sppr200iiibk_bluetooth_usb/p9343982/',
    'https://rozetka.com.ua/ua/hprt_9554/p11245658/',
    'https://rozetka.com.ua/ua/252787381/p252787381/'
]
for p in range(1,2):
    url = f"https://rozetka.com.ua/ua/printery-etiketok/c4625268/producer=bixolon,godex,hprt,zebra1;seller=rozetka/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        '''name =  element.find('span', class_="goods-tile__title").find('span').text.strip()'''
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_="goods-tile__price-value").text.strip()
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
        try:
            price = soup.find('p', class_="product-price__small ng-star-inserted").text.strip()
        except:
            ac_price = "-"
        
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
        
for p in range(1,2):
    url = f"https://rozetka.com.ua/ua/counters_and_currency_detectors/c754404/producer=nrj;seller=rozetka;state=new/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        '''name =  element.find('span', class_="goods-tile__title").find('span').text.strip()'''
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_="goods-tile__price-value").text.strip()
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
        try:
            price = soup.find('p', class_="product-price__small ng-star-inserted").text.strip()
        except:
            ac_price = "-"
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
for p in range(1,2):
    url = f"https://rozetka.com.ua/ua/pos-printery/c4625319/producer=hprt;seller=rozetka/"
    r = requests.get(url, timeout=20, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'lxml')
    n_elemnts = soup.findAll('li',class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for element in n_elemnts:
        '''name =  element.find('span', class_="goods-tile__title").find('span').text.strip()'''
        try:
            name = element.find('span', class_="goods-tile__title").text.strip()
        except:
            name='-'
        try:
            price = element.find('span', class_="goods-tile__price-value").text.strip()
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
        try:
            price = soup.find('p', class_="product-price__small ng-star-inserted").text.strip()
        except:
            ac_price = "-"
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

start_time = time.time()
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
technologic = [
    'https://technologic.com.ua/products/printer-etiketok-godex-g500/',
    'https://technologic.com.ua/products/printer-etiketok-godex-g530/',
    'https://technologic.com.ua/products/printer-etiketok-godex-dt2x/',
    'https://technologic.com.ua/products/printer-etiketok-godex-rt200i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-rt863i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-rt200/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx1200i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx1300i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx1600i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx420i/',
    'https://technologic.com.ua/products/printer-etiketok-zebra-zd220tt/',
    'https://technologic.com.ua/products/printer-etiketok-zebra-zd220tt/',
    'https://technologic.com.ua/products/printer-etiketok-zebra-zd220dt/',
    'https://technologic.com.ua/products/printer-etiketok-zebra-tlp2824-plus/',
    'https://technologic.com.ua/products/printer-etiketok-godex-rt730i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-ez120/',
    'https://technologic.com.ua/products/printer-etiketok-godex-ez130/',
    'https://technologic.com.ua/products/printer-etiketok-godex-ez6300-plus/',
    'https://technologic.com.ua/products/printer-etiketok-godex-hd830i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx1200i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx1300i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-zx430i/',
    'https://technologic.com.ua/products/printer-etiketok-godex-gtl100/',
    'https://technologic.com.ua/products/licilnik-banknot-nrj-al-5100-uv/',
    'https://technologic.com.ua/products/licilnik-banknot-nrj-al-185-uv-mg-ir/',
    'https://technologic.com.ua/products/licilnik-banknot-nrj-al-6600-uvmg/',
    'https://technologic.ua/products/mobilnii-printer-cekiv-bixolon-spp-r200iiibk/',
    'https://technologic.ua/products/printer-etiketok-hprt-ht300/',
    'https://technologic.ua/products/printer-cekiv-i-etiketok-hprt-lpq58/',
    'https://technologic.ua/products/printer-cekiv-i-etiketok-hprt-lpq80/',
    'https://technologic.ua/products/printer-cekiv-hprt-mpt2/',
    'https://technologic.ua/products/printer-cekiv-hprt-ppt2-a/',
    'https://technologic.ua/products/printer-cekiv-hprt-mpt3/',
    'https://technologic.ua/products/printer-cekiv-hprt-ppt2-a/',
    'https://technologic.ua/products/printer-cekiv-hprt-tp805l/'
]
for url in technologic:
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
        price_element = soup.find('div', class_="product-main-price")
        price = price_element.text.strip()
    except AttributeError:
        price
    try:
        price = re.findall(r"Ціна:\s*(.*?)\s*грн", price)[0]
    except:
        price
    name_link = soup.find('h1', class_="product-hero-title")
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
    s_name = 'technologic'
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
            parts = remaining_name.lower().split("dpi")
            remaining_name = parts[1].strip()  # Удаление пробелов
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
    digits = re.findall(r"\d+", dpi)
    letters = re.findall(r"[a-zA-Z]", dpi)
    dpi = "".join(digits)
    tp = "".join(letters)
    data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
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
for url in fornit:
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
        if soup.find('span', class_="product-price__item") is None:
            price_element = soup.find('div', class_="product-price__old-price")
            price = price_element.text.strip()
            ac_price = soup.find('div', class_="product-price__item product-price__item--new")
            ac_price = ac_price.text.strip()
    except AttributeError:
        price_element = soup.find('div', class_="product-price__item")
        price = price_element.text.strip()
    try:
        price = re.findall(r"Ціна:\s*(.*?)\s*грн", price)[0]
    except:
        price
    name_link = soup.find('h1', class_="product-title")
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
    s_name = 'fornit'
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
posttorg = [
    'https://posttorg.com.ua/product/printer_etiketok_godex_g500/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-g530/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_ez-dt2_plus/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_dt2x/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_ez-dt4_plus/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-dt4x/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-etiketok-godex-mx30i/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_rt-200i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-rt863i/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_ez-6300_plus/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-ez2350i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-ez6250i/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-etiketok-godex-mx30/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-etiketok-godex-mx30i/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_rt-200/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx-1200i/',
    'https://posttorg.com.ua/product/printer_etiketok_godex_zx-1300i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx1600i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx420i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-rt730iw/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-ez130/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-ez6300-plus/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-hd830i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx1200xi/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx1300xi/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-zx430i/',
    'https://posttorg.com.ua/product/printer-etiketok-godex-gtl-100/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-etiketok-godex-mx20/',
    'https://posttorg.com.ua/product/printer-etiketok-hprt-elite/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-hprt-mt800/',
    'https://posttorg.com.ua/product/printer-etiketok-bixolon-samsung-slp-dx420/',
    'https://posttorg.com.ua/product/mobilnyj-printer-etiketok-bixolon-spp-l3000/',
    'https://posttorg.com.ua/product/printer-etiketok-bixolon-xq-840/',
    'https://posttorg.com.ua/product/printer-etiketok-hprt-ht100/',
    'https://posttorg.com.ua/product/printer-etiketok-hprt-ht300/',
    'https://posttorg.com.ua/product/printer-etiketok-hprt-ht330/',
    'https://posttorg.com.ua/product/printer-chekov-etiketok-hprt-lpq58/',
    'https://posttorg.com.ua/product/printer-chekov-etiketok-hprt-lpq80/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-etiketok-bixolon-xm7-40/',
    'https://posttorg.com.ua/product/printer_chekov_bixolon_srp-350iii/',
    'https://posttorg.com.ua/product/printer-chekov-bixolon-srp-e300/',
    'https://posttorg.com.ua/product/printer-chekov-bixolon-srp-q200/',
    'https://posttorg.com.ua/product/mobilnyj-printer-etiketok-chekov-hprt-hm-e200/',
    'https://posttorg.com.ua/product/mobilnyj-printer-chekov-hprt-mpt-ii/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-ppt2-a/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp585/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp806/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp808/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp809/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp80k/',
    'https://posttorg.com.ua/product/printer-chekov-bixolon-srp-380/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-ppt2-a/',
    'https://posttorg.com.ua/product/printer-chekov-hprt-tp805l/'
]
print('m')
for url in posttorg:
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue  
    soup = BeautifulSoup(response.text, 'lxml')
    product_container = soup.find('div', class_="br-body br-body-product")
    try:
        price = soup.find('span', class_="price nowrap").text.strip()   
    except:
        ac_price = "-"  
    name_link = soup.find('div', class_="product-title-block")
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
    s_name = 'postorg'
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
    price = re.findall(r"^\d+\.?", price)[0]
    digits = re.findall(r"\d+", dpi)
    letters = re.findall(r"[a-zA-Z]", dpi)
    dpi = "".join(digits)
    tp = "".join(letters)
    ac_price = ''
    data.append([kategoria,marka,mod,tp,dpi, remaining_name, price, ac_price, s_name])
dpi_600 = [
    'https://600dpi.com.ua/printer-etiketok-godex-g500',
    'https://600dpi.com.ua/printer-etiketok-godex-g530',
    'https://600dpi.com.ua/printer-etiketok-godex-dt2x',
    'https://600dpi.com.ua/printer-etiketok-godex-dt4x',
    'https://600dpi.com.ua/printer-etiketok-godex-rt200i',
    'https://600dpi.com.ua/printer-etiketok-godex-rt863i',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-etiketok-godex-mx30i',
    'https://600dpi.com.ua/printer-etiketok-godex-rt200',
    'https://600dpi.com.ua/printer-etiketok-godex-zx1200i',
    'https://600dpi.com.ua/printer-etiketok-godex-zx1300i',
    'https://600dpi.com.ua/shop/search?text=GoDEX+ZX1600i',
    'https://600dpi.com.ua/printer-etiketok-godex-zx420i',
    'https://600dpi.com.ua/printer-etiketok-godex-rt730i',
    'https://600dpi.com.ua/printer-etiketok-godex-bp520l',
    'https://600dpi.com.ua/printer-etiketok-godex-ez120',
    'https://600dpi.com.ua/printer-etiketok-godex-ez130',
    'https://600dpi.com.ua/printer-etiketok-godex-ez-6300-plus',
    'https://600dpi.com.ua/printer-etiketok-godex-hd830i',
    'https://600dpi.com.ua/printer-etiketok-godex-zx1200xi',
    'https://600dpi.com.ua/printer-etiketok-godex-zx430i',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-etiketok-godex-mx20',
    'https://600dpi.com.ua/sortirovshchik-banknot-nrj-al-955-uv-mg-ir',
    'https://600dpi.com.ua/printer-etiketok-bixolon-slp-dl410c',
    'https://600dpi.com.ua/printer-chekov-etiketok-bixolon-srp-s300l',
    'https://600dpi.com.ua/printer-etiketok-hprt-ht100',
    'https://600dpi.com.ua/printer-etiketok-hprt-ht300',
    'https://600dpi.com.ua/printer-chekov-etiketok-hprt-lpq58',
    'https://600dpi.com.ua/printer-chekov-etiketok-hprt-lpq80',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-bixolon-spp-r310',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-bixolon-spp-r410',
    'https://600dpi.com.ua/printer-chekov-bixolon-srp-350iii',
    'https://600dpi.com.ua/printer-chekov-bixolon-srp-380',
    'https://600dpi.com.ua/printer-chekov-bixolon-srp-e300',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-hprt-hm-e300',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-hprt-hm-e200',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-hprt-mpt2',
    'https://600dpi.com.ua/printer-chekov-hprt-ppt2-a',
    'https://600dpi.com.ua/printer-chekov-hprt-tp806',
    'https://600dpi.com.ua/printer-chekov-hprt-tp808',
    'https://600dpi.com.ua/printer-chekov-hprt-tp809',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-bixolon-spp-r200iii',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-bixolon-spp-r310',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-bixolon-spp-r410',
    'https://600dpi.com.ua/printer-chekov-bixolon-srp-380',
    'https://600dpi.com.ua/mobilnyi-printer-chekov-hprt-mpt3',
    'https://600dpi.com.ua/printer-chekov-hprt-tp805l',
]
for url in dpi_600:
    try:
        response = requests.get(url, timeout=20, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        continue  
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        price = soup.find('span', class_="product-price__main-value").text.strip()   
    except:
        ac_price = "-"  
    try:
        name_link = soup.find('div', class_="product-intro__row")
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
    s_name = '600 dpi'
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
    'https://gipercenter.kiev.ua/ua/p1414283733-printer-etiketok-godex.html',
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
    try:
        price = soup.find('span', class_="Text__ui_text_size_x7l--cgh_a Text__ui_text_font-weight_bold--qRTru").text.strip()   
        ac_price = ''
    except:
        price =  soup.find('span', class_="Text__ui_text_size_xs--GXoZP Text__ui_text_decoration_line-through--lN0mm").text.strip()   
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