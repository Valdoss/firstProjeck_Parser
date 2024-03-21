import openpyxl
from time import sleep
from re import findall, split
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
start_time = time.time()
keywords = ["Принтер етикеток і чеків", "Принтер етикеток","Детектор валют", "Принтер linerless етикеток","Принтер браслетів","Принтер-аплікатор","Детектор валют","Детектор валюти","Лічильник банкнот","Сортувальник банкнот",
            'Принтер чеків', 'Термопринтер','Портативний принтер','POS-принтер','POS-прінтер', 'Настольный принтер этикеток','Промышленный принтер этикеток','Мобильный принтер', 'Мобильный принтер','Принтер этикеток','Принтер чеков и этикеток',
            'Принтер чеков', 'Счетчик банкнот','Термотрансферний принтер','Мобільний принтер для друку етикетки та чеків', 'Принтер для друку етикеток і штрих-коду', 'Принтер мобільний',
            'Принтер пластикових карток', 'Лічильник купюр'
           ]
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
data = []
start_time = time.time()
url = f"https://rozetka.com.ua/ua/printery-etiketok/c4625268/producer=bixolon,godex,hprt,zebra1;seller=rozetka/"

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
for p in range(1,2):  # Промышленный принтер этикеток technologic
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
for p in range(1,2):  # Промышленный принтер этикеток technologic
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
for p in range(1,2):  # Промышленный принтер этикеток technologic
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
for p in range(1,2):  # Промышленный принтер этикеток technologic
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
header = ['kategoria','marka','mod','tp','dpi', 'remaining_name', 'price', 'ac_price', 's_name'] 
df = pd.DataFrame(data, columns=header)
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(header)
for row in data:
    worksheet.append(row)
workbook.save(r'14.7.xlsx')