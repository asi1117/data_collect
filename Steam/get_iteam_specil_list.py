'''
爬取每个游戏的详细信息，包括：售价（美元）
All Reviews, Release date, developer, publisher, support headsets, input, play area, support language
ganer, system requirements
'''
import time
from webbrowser import Chrome

import requests
import row as row
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sys
import os
import csv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    driver = Chrome()
    # with open('2VR_Only_titles.csv', 'rt',encoding='utf-8_sig') as f:
    #     reader = csv.DictReader(f)
    #     game_list = [row['id'] for row in reader]
    id_list = ['250820', '630980', '613920', '743060', '1056890', '1056880', '790870', '1056910', '1056900', '857630', '924110', '815980', '828360', '633140', '750970', '897920', '632280', '627320', '633210', '556230', '1635700', '525350', '738790', '1056940', '451450', '668180', '737480', '922120', '630530', '727230', '769620', '1059450', '515740']
    print(len(id_list))
    gameCount = 0
    df = pd.DataFrame()
    for d in id_list:
        url = 'https://store.steampowered.com/app/' + d + '/'
        print(url)
        driver.get(url)
        driver.maximize_window()
        try:
            driver.find_element(by=By.XPATH,value='//a[@id="view_product_page_btn"]').click()
            time.sleep(5)
        except:
            print("有没点击成功")
            time.sleep(5)
        page = driver.find_element(by=By.XPATH,value='/html/body')
        resp = BeautifulSoup(page.get_attribute('innerHTML'), "html.parser")
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
            try:
                genre = ''
                print("Game Genre:************************************")
                details_block = resp.find("div", {"id": "genresAndManufacturer"})
                generHref = details_block.find('span').find_all('a')
                for a in generHref:
                    genre = genre + ';' + a.text.strip()
                    # genre.append(a.text.strip())
                    print(a.text.strip())
            except:
                genre =''
                #游戏价格
            print("Game price:************************************")
            try:
                price = resp.find("div", {"class": "game_purchase_price price"}).text
            except:
                price = ''
            #爬取metacritic score
            print("Game metacritic score:************************************")
            try:

                score = resp.find("div", {"class": "score high"}).text
            except:
                score = ''
            #爬取支持的语言
            try:
                language = ''
                table = resp.find("table", {"class": "game_language_options"})
                lang = table.find_all("td", {"class": "ellipsis"})
                for l in lang:
                    language = language + ';' + l.text.strip()
                print("Support Language:************************************")
                print(language)
            except:
                language = ''
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
    df.to_csv("3VR_Support_Game_Inf.csv", index=False, sep=',', mode='w+', encoding='utf_8_sig')
    print("Game count: ", len(game_id))




