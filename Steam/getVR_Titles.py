'''
在Steam上搜关键字VR将结果全部爬出来，VR游戏分为两类：VR Only, VR Supported
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

sys.setrecursionlimit(2000)


def get_html(url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'https://store.steampowered.com/'
    }
    try:
        r = requests.get(url, headers=headers, timeout=2000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()

    except:
        return ""


if __name__ == '__main__':
    cont = 1
    while cont <8000:
        #url = 'https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&sort_by=_ASC&term=vr&snr=1_7_7_151_7&infinite=1'
        url = 'https://store.steampowered.com/search/results/?query&start='+str(cont)+'&count=100&dynamic_data=&sort_by=_ASC&term=vr&snr=1_7_7_151_7&infinite=1'
        cont = cont+100
        json_game = get_html(url)
        html = json_game.get('results_html')
        page = BeautifulSoup(html, 'html.parser')
        # print(page)
        link = page.find_all(name='a', attrs={"class": "search_result_row ds_collapse_flag"})
        dataframe = pd.DataFrame()
        count = 0
        for j in link:
            print(j["href"].split('?')[0])
            title = j.find('span', attrs={"class": "title"})
            print("game title: ", title.string)
            game_id = j["href"].split('/')[4]
            print(game_id)

            vr_required = j.find('span', attrs={"class": "vr_required"})
            if vr_required == None:
                vr_required = j.find('span', attrs={"class": "vr_supported"})
                if vr_required == None:
                    vr_required = "Not mentioned"
                else:
                    vr_required = vr_required.string
            else:
                vr_required = vr_required.string
            print("vr_required: ", vr_required)
            if vr_required != "Not mentioned":
                dataframe = dataframe.append(pd.DataFrame({
                    'title': title,
                    'id': game_id,
                    'href': j["href"].split('?')[0],
                    'VR required': vr_required},
                    index=[count]))
                count += 1
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv("VR_titles.csv", index=False, sep=',', encoding='utf_8_sig')
        print(count)


        # date = j.find(name='div', attrs={"class": "col search_released responsive_secondrow"})
        # print("release date: ", date.string)
        # price = j.find('div', attrs={"class": "col search_price responsive_secondrow"})
        # if price == None:
        #     price = j.find('div', attrs={"class": "col search_price discounted responsive_secondrow"})
        # print("price: ", price)
        # review_summary = j.find('span', attrs={"class": "search_review_summary positive"})
        # if review_summary == None:
        #     review_summary = j.find('span', attrs={"class": "search_review_summary negative"})
        #     if review_summary == None:
        #         review_summary = j.find('span', attrs={"class": "search_review_summary mixed"})
        #
        # print(review_summary)
        # print(type(review_summary))






