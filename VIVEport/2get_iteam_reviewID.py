'''
在Steam上搜关键字VR将结果全部爬出来，VR游戏分为两类：VR Only, VR Supported
'''
import csv
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time


if __name__ == '__main__':
    cont = 1
    count1 = 0
    count2 = 0
    dataframe = pd.DataFrame()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    }
    #读csv文件的id一列
    with open('C:/Users/Admi/PycharmProjects/data_collect/VIVEport/VIVEPort_id.csv', 'rt',encoding='utf-8_sig') as f:
        reader = csv.DictReader(f)
        game_list = [row['iteam_id'] for row in reader]
    id_list =game_list
    pf = pd.DataFrame()
    count = 0
    for game_id in id_list:
        print(cont)
        #url = 'https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&sort_by=_ASC&term=vr&snr=1_7_7_151_7&infinite=1'
        #url = 'view-source:https://www.viveport.com/game.html?p='+str(cont)
        url = 'https://www.viveport.com/'+str(game_id)
        cont = cont+1
        resp = requests.get(url, headers=headers)
        #print(resp.content)
        html = resp.content
        page = BeautifulSoup(html, 'html.parser')
        #print(page)
        #获取评论id
        revieid = page.find_all(name='input', attrs={'name': 'item'})[0].get('value')
        pf = pf.append(pd.DataFrame({
            'iteam_id': game_id,
            'review_id': revieid,
            # 'title': review_author,
        },
            index=[count]))
        count += 1
        print(count)
        pf.to_csv('VIVEPort_reviewId.csv',index=False, sep=',', encoding='utf_8_sig')






