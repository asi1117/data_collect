#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import warnings

import requests as requests

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import traceback

# %%% initialize chrome
# open website
time_star = time.time()
# %%% collect all reviews

count = 0
dataframe = pd.DataFrame()
with open('VIVEPort_id.csv', 'rt', encoding='utf-8_sig') as f:
    reader = csv.DictReader(f)
    game_list = [row['iteam_id'] for row in reader]
id_list = game_list
n = 0
k = 0
worry_list = []
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    }
#得到商品的所有共同标签，将标签内容传到soup中
#循环打开游戏的页面，获取上面的信息

for id in id_list:
    # 得到商品id，通过访问url将商品信息输进去
    url = 'https://www.viveport.com/' + str(id)
    resp = requests.get(url, headers=headers)
    html = resp.content
    soup1 = BeautifulSoup(html, 'html.parser')
    url2 = soup1.find('option', attrs={'class': 'view-jp_v_enus'}).get('href')
    resp2 = requests.get(url2, headers=headers)
    html2 = resp2.content
    soup2 = BeautifulSoup(html2, 'html.parser')
    try:
        app_details = soup2.find_all('div', attrs={'class': 'meta-block'})
        #print(app_details)
    except:
        print("取游戏细节出错")
    try:
        iteam_name = soup2.find('div', attrs={'class': 'page-title-wrapper product'}).text.strip()
        print(iteam_name)
    except:
        iteam_name = ''
        print('获取商品名字错误')
    try:
        iteam_description = soup2.find_all('div', attrs={'class': 'description-block'})[0].text.strip()
        print(iteam_description)
    except:
        iteam_description = ''
        print('获取商品简介')
    try:
        iteam_price = soup2.find_all('span', attrs={'class': 'price'})[0].text.strip()
    except:
        iteam_price = ''
        print('价格失败')
    try:
        iteam_language = soup2.find('table', attrs={'class': 'lang-supported-table'}).text.replace('Interface', '').replace('Audio', '').replace('Subtitles', '').strip()
    except:
        iteam_language = ''
        print('语言失败')

    try:
        print(len(app_details))
        print(id+'.csv')
        # print('日期',app_details[5].find_all('p')[1].get('data-date'))  # .get('data-date'))
        dataframe = dataframe.append(pd.DataFrame({
            'Game_Id': id,
            'Game_Name': iteam_name,
            'Game_price': iteam_price,
            'Game_description': iteam_description,
            'Game_platform': app_details[0].find('div').text.strip(),
            'Game_genre':app_details[1].find('div').text.strip(),
            'Game_playArea':app_details[2].find('div').text.strip(),
            'Game_Controllers':app_details[3].find('div').text.strip(),
            'Game_rating':app_details[4].find_all('p')[1].text.strip(),
            'Game_releaseDate': app_details[5].find_all('p')[1].get('data-date'), #.get('data-date'),
            'Game_latestDate': app_details[6].find_all('p')[1].get('data-date'),
            'Game_version':app_details[7].find_all('p')[1].text.strip(),
            'Game_type': app_details[8].find_all('p')[1].text.strip(),
            'Game_modes':app_details[9].find('div').text.strip(),
            'Game_languages':iteam_language.strip(),
        },
            index=[count]))
        count += 1
        print(count)
        dataframe.to_csv("iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
        time.sleep(2)
    except:
        print(id ,"写文件出错")
        worry_list.append(id)
        print('worry_list',worry_list)
        continue


# 'Game_Id': id,
#             'Game_Name': iteam_name,
#             'Game_price': iteam_price,
#             'Game_description': iteam_description,
#             'Game_platform': app_details[0].text.strip(),
#             'Game_genre':app_details[1].div.text.strip(),
#             'Game_playArea':app_details[2].div.text.strip(),
#             'Game_Controllers':app_details[3].text.strip(),
#             'Game_rating':app_details[4].text.strip(),
#             'Game_releaseDate':app_details[5].p[1].get('data-date'),
#             'Game_version':app_details[7].p[1].text.strip(),
#             'Game_type': app_details[8].p[1].text.strip(),
#             'Game_modes':app_details[9].div.text.strip(),
#             'Game_languages':iteam_language.strip(),













