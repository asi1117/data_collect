'''
爬取每个游戏的详细信息，包括：售价（美元）
All Reviews, Release date, developer, publisher, support headsets, input, play area, support language
ganer, system requirements
'''
import requests
import row as row
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sys
import os
import csv
sys.setrecursionlimit(2000)


def get_html(url):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Connection': 'keep-alive',
        'Origin': 'https://store.steampowered.com',
        'Referer': 'https://store.steampowered.com/'
    }
    try:
        r = requests.get(url, headers=headers, timeout=2000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return BeautifulSoup(r.text, "html.parser")

    except:
        return ""


if __name__ == '__main__':
    worry_list = []
    game_id = []
    with open('2VR_Support_titles.csv', 'rt',encoding='utf-8_sig') as f:
        reader = csv.DictReader(f)
        game_list = [row['id'] for row in reader]

    id_list =game_list
    print(id_list)
    gameCount = 0
    df = pd.DataFrame()
    for d in id_list:
        url = 'https://store.steampowered.com/app/' + d + '/'
        print(url)
        resp = get_html(url)
        #爬取游戏名字，开发商，发行商，发布日期
        # 游戏名字
        try:
            print("Game name:************************************")
            gameName = resp.find("div", {"class": "apphub_AppName"}).text.strip()
            print(gameName, "\n")
            #开发商
            print("Developer:************************************")
            dlp = resp.find("div", {"id": "developers_list"})
            if dlp is None:
                developer = ''
                print('No developer\n')
            else:
                developer = dlp.find("a").text.strip()
                print(developer, "\n")

            #发行商
            print("Publisher:************************************")
            dev_row = resp.find_all("div", {"class": "dev_row"})
            if len(dev_row) < 2:
                print("No publisher\n")
            else:
                pub = dev_row[1].find("div", {"class": "summary column"})
                if pub is None:
                    publisher = ''
                    print("No publisher\n")
                else:
                    publisher = pub.find("a").text.strip()
                    print(publisher, "\n")

            #发行日期
            print("Release date:************************************")
            release_date = resp.find("div", {"class": "date"})
            if release_date is None:
                release_date = ''
                print("No Release Date\n")
            else:
                release_date = release_date.text.strip()
                print(release_date, "\n")

            # 爬取 Headsets, Input, Play Area的信息
            headSets = ''
            inputD = ''
            playArea = ''

            details_left = resp.findAll("div", {"class": "block responsive_apppage_details_left"})
            details_left_up = details_left[0]
            details_left_down = details_left[1]
            ahref = details_left_down.find_all("a")
            for a in ahref:
                img = a.find("div", {"class": "icon"})
                src = img.find("img").get("src")
                str = src.split('ico_')[1].split('.')[0]
                if "headset" in str:
                    st = str.split("_")[2:]
                    headSets = headSets + ';' + ''.join(st)
                elif "area" in str:
                    area = str.split("_")[2:]
                    playArea = playArea + ';' + ''.join(area)
                else:
                    inputD = inputD + ';' + str

            print("Headsets:************************************")
            print(headSets, "\n")
            print("Input:************************************")
            print(inputD, "\n")
            print("Play area:************************************")
            print(playArea, "\n")

            # 爬取游戏类型 GENRE
            genre = ''
            print("Game Genre:************************************")
            details_block = resp.find("div", {"id": "genresAndManufacturer"})
            generHref = details_block.find('span').find_all('a')
            for a in generHref:
                genre = genre + ';' + a.text.strip()
                # genre.append(a.text.strip())
                print(a.text.strip())

            #游戏价格
            print("Game price:************************************")
            pri = resp.find("div", {"class": "game_purchase_price price"})
            if pri is None:
                print("no price\n")
                price = ''
            else:
                price = pri.text.strip()
                print(price, "\n")

            #爬取metacritic score
            print("Game metacritic score:************************************")
            sco = resp.find("div", {"class": "score high"})
            if sco is None:
                print("No score\n")
                score = ''
            else:
                print(sco.text.strip(), "\n")
                score = sco.text.strip()

            #爬取支持的语言
            language = ''
            table = resp.find("table", {"class": "game_language_options"})
            lang = table.find_all("td", {"class": "ellipsis"})
            for l in lang:
                language = language + ';' + l.text.strip()
            print("Support Language:************************************")
            print(language)

            df = df.append(pd.DataFrame({
                'Game_id': d,
                'Game_name': gameName,
                'Developer': developer,
                'Publisher': publisher,
                'Release Date': release_date,
                'Price': price,
                'Metacritic Score': score,
                'Headsets': headSets,
                'Input': inputD,
                'Play Area': playArea,
                'Genre': genre,
                'Support Language': language},
                index=[gameCount]))
            gameCount += 1
        except:
            print("这个id有问题",d)
            worry_list.append(d)
            print(worry_list)
            print(len(worry_list))
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    df.to_csv("VR_Support_Game_Inf.csv", index=False, sep=',', mode='w+', encoding='utf_8_sig')
    print("Game count: ", len(game_id))




