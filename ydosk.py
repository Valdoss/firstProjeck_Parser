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
            'Принтер пластикових карток', 'Сортировщик банкнот','Термопринтер мобильный принтер чеков','Настольный принтер чеков/этикеток']
firm = ["Godex","Zebra", "NRJ", "HPRT", 'BIXOLON']
USB_K = ['USB','u']
USBHOST_K = ['USB-HOST', 'USB HOST','USB-HOST']
Bt_K = ['BT', 'BLUETOOTH']
ETHERNET_K = ['ETHERNET', 'E']
data = []
serial_K = ['SERIAL', 'RS232', 'US']
wifi_K = ['WIFI', 'WI-FI', 'WI FI']
c=0
DT2X = ['/ DT2X']
Vuniat = ['CG', 'COG', 'COSK', 'ESK', 'COEK']
start_time = time.time()
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
        dpi = " ".join(digits)
            # Объединить буквы в строку
        tp = "0"
        if len(remaining_name) > 0 and (remaining_name[0] == '(' or remaining_name[0] == ')'):
            remaining_name = remaining_name[1:]
        if len(remaining_name) > 0 and (remaining_name[-1] == '(' or remaining_name[-1] == ')'):
            remaining_name = remaining_name[:-1]
            
        cyrillic_text = ""
        remaining_name = remaining_name.replace('+',',')
        found_cyrillic = False
        for char in remaining_name:
            if ord(char) >= 1040 and ord(char) <= 1103:
                found_cyrillic = True
                cyrillic_text += char
            elif found_cyrillic:
                cyrillic_text += char
        if cyrillic_text:
            print(cyrillic_text)  # Выводит текст после первого символа кириллицы
        else:
            print("Кириллица не найдена.")
        for item in remaining_name:
            if(item == ',' or item == ' '):
                pass
            elif item in cyrillic_text:
                remaining_name = remaining_name.replace(item, '')
        remaining_name = remaining_name.replace('+',',')
        if mod == '':
            break
        reefCode = ''
        par = cyrillic_text.split('(')
        p =''
        tp = ''
        try:
            reefCode = par[1]
            cyrillic_text = par[0]
        except:
            pass
        try:
            if remaining_name[0].isdigit():
                reefCode = remaining_name
                remaining_name = '' 
        except:
            pass
        foundCode = False
        for ch in remaining_name:
            if(ch == '('):
                foundCode = True
                reefCode += ch
            elif foundCode:
                if ch.isdigit():
                    p = remaining_name.split('(')
                    reefCode += ch
                else :
                    foundCode = False
        try:
            reefCode = p[1]
            remaining_name = p[0]
        except:
            pass
        
        remaining_name = remaining_name.upper()
        ZebraCod = ''
        for byk in remaining_name:
            if byk == 'Z':
                Zeb = remaining_name.split('Z')
                remaining_name = Zeb[0]
                try:   
                  ZebraCod ='Z'+ Zeb[1]
                except:
                    pass
        USB = ''
        USBHOST = ''
        BT = ''
        ETHERNET = ''
        serial = ''
        wifi = ''
        # for key in USB_K:
        #     if key.upper() in remaining_name.upper():
        #         USB = 'USB'
        #         break  
        # for key in USBHOST_K:
        #     if key.upper() in remaining_name.upper():
        #         USBHOST = 'USB-HOST'
        #         break  
        remaining_name = remaining_name.upper()
        words = re.split(r"[ ,]", remaining_name)
        for word in words:
            if word.startswith('U'):
                for key in USB_K:
                    if key.upper() in remaining_name.upper():
                        USB = 'USB'
                        break  
        for word in words:
            if word.startswith('U') or word.upper() == 'UES' or word.upper() == 'USB' :
                for key in USBHOST_K:
                    if key.upper() in remaining_name.upper():
                        USBHOST = 'USB-HOST'
                        break 
        for word in words:
            if word.startswith('B'):
                for key in Bt_K:
                    if key.upper() in remaining_name.upper():
                        BT = 'BLUETOOTH'
                        break  
        for word in words:
            if word.startswith('E') or word.upper() == 'UES' :
                for key in ETHERNET_K:
                    if key.upper() in remaining_name.upper():
                        ETHERNET = 'ETHERNET'
                        break
        for word in words:
            if word.startswith('S') or word.startswith('R'):
                for key in serial_K:
                    if key.upper() in remaining_name.upper():
                        serial = 'SERIAL'
                        break
            elif word.upper() == 'UES' or word.upper() == 'ERIAL':
                serial = 'SERIAL'
                break  
        for word in words:
            if word.startswith('W'):
                for key in wifi_K:
                    if key.upper() in remaining_name.upper():
                        wifi = 'Wi-Fi'
                        break
        Liner = ''
        for word in words:
            if word.upper() == 'PLUS':
                mod = mod + " " + 'PLUS'
        for word in words:
            if word.upper() == 'LINER' or word.upper() == 'LINERLESS' or word.upper() == 'LINER LES' or word.upper() == 'LINER-LESS':
                Liner = 'LINER LESS'
                break
        for word in words:
            if word.startswith('DT2X') :
                mod = mod + '/DT2X'
                break
        lpt = ''
        for word in words:
            if word == 'LPT':
                lpt = 'LPT'
                break
        rtc = ''
        for word in words:
            if word == 'RTC':
                lpt = 'RTC'
                break   
            
        wordssssss = re.split(r"[ ,/ \]", remaining_name)

        data.append([kategoria,  # Use empty string if kategoria is None
        marka,
        mod,
        dpi or 0,
        remaining_name or 0,
        cyrillic_text,  reefCode, ZebraCod, USB, USBHOST, BT, ETHERNET,serial, wifi, Liner, lpt, rtc,
        price or 0,
        ac_price or 0,
        s_name or 0 ])
header = ['Kategoria','marka','model',"dpi", 'name','cyrillic_text','reefCode','ZebraCod', 'USB','USBHOST','BLUETOOTH','ETHERNET','serial', 'Wi-Fi', 'LINER LESS' ,'lpt', 'rtc' ,'price', 'sale', 'firm'] 
df = pd.DataFrame(data, columns=header)
workbook = openpyxl.Workbook()                      
worksheet = workbook.active
worksheet.append(header)
for row in data:
    worksheet.append(row)
workbook.save(r'14.11.xlsx')

    