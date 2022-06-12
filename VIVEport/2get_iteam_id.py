'''
在Steam上搜关键字VR将结果全部爬出来，VR游戏分为两类：VR Only, VR Supported
'''
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
sys.setrecursionlimit(2000)


# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
#     }
#     try:
#         r = requests.get(url, headers=headers, timeout=1000)
#         print(r)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.json()
#
#     except:
#         return ""


if __name__ == '__main__':
    cont = 1
    count1 = 0
    count2 = 0
    dataframe = pd.DataFrame()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    }
    #为防止游戏重复，我们将所有的id都放在一个数组了利用是是数组特性将其铲除
    vrOnly_list = []
    support_list = []
    pf = pd.DataFrame()
    count = 0
    while cont < 55:
        print(cont)
        #url = 'https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&sort_by=_ASC&term=vr&snr=1_7_7_151_7&infinite=1'
        #url = 'view-source:https://www.viveport.com/game.html?p='+str(cont)
        url = 'https://www.viveport.com/game.html?p='+str(cont)
        cont = cont+1
        resp = requests.get(url, headers=headers)
        #print(resp.content)
        time.sleep(2)
        html = resp.content
        page = BeautifulSoup(html, 'html.parser')
        #print(page)
        link = page.find_all(name='div', attrs={"data-container": "product-grid"})
        for i in link:
            #title = i.find(name='img', attrs={"class": 'product-image-photo'}).get('alt')
            id = i.find(name='a',attrs={'class': "product-item-link"}).get('href').split('/')[3]
            title = i.find(name='a',attrs={'class': "product-item-link"}).text
            try:
                #游戏种类
                iteam_genres = ''
                genres = i.find_all(name = 'div', attrs={"class":'product-item-genre'})
                for g in genres:
                    g.text += iteam_genres
            except:
                iteam_genres = ''
            print(id)
            #iteam_id = i.find(name='div', attrs={''})
            pf = pf.append(pd.DataFrame({
                'iteam_id': id,
                'iteam_genres': iteam_genres,
                'title': title,
                # 'title': review_author,
            },
                index=[count]))
            count += 1
            print(count)
        pf.to_csv('VIVEPort_id.csv',index=False, sep=',', encoding='utf_8_sig')
        # #print(vr_requireds)
        # for j in link:
        #     title = j.find('span', attrs={"class": "product-image-photo"}).get('src')
        #     print(title)
        # if cont >7900:
        #     print(len(vrOnly_list))
        #     set_list = set(vrOnly_list)
        #     new_vronly_list = list(set_list)
        #     print('vrlist更新后的数组', new_vronly_list)
        #     print(len(new_vronly_list))
        #     set_list2 = set(support_list)
        #     new_support_list = list(set_list2)





