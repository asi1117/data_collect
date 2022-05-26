#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
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
# %%% relevent website

website = 'https://www.oculus.com/experiences/quest/section/391914765228253/'

# %%% initialize chrome
# open website
driver = Chrome()
driver.get(website)
driver.maximize_window()
time_star = time.time()
# %%% collect all reviews
reviews_one_store = []
condition_to_continue = True
dataframe = pd.DataFrame()
count = 0
page = driver.find_element(by=By.XPATH,value='//*[@id="footer-ssr"]/div/div[1]')
#因为quest里是有387个游戏，用滚动条的方式将锁定到关键字上，等待一秒等页面刷新获取值
for i in range(38):
    driver.execute_script("arguments[0].scrollIntoView()", page)
    time.sleep(1)
    print('i',i)
n = 0
k = 0
#得到商品的所有共同标签，将标签内容传到soup中
while(condition_to_continue):
    iteam_list = driver.find_elements(by=By.XPATH, value='//div[@class="section__items-cell"]')

    #循环打开游戏的页面，获取上面的信息
    while(n<len(iteam_list)+1) :
        soup1 = BeautifulSoup(iteam_list[n].get_attribute('innerHTML'), "html.parser")
        id1 = soup1.find('a', attrs={'class': 'store-section-item-tile'}).get('data-testid')
        print(id1)
        # 得到商品id，通过访问url将商品信息输进去
        url = 'https://www.oculus.com/experiences/quest/' + str(id1)
        driver.get(url)
        driver.maximize_window()
        windows = driver.window_handles  # 获得多个窗口句柄
        print(windows)
        #node_handle = driver.current_window_handle
        driver.switch_to.window(windows[-1])
        #print(node_handle)
        #driver.switch_to.window(windows[0]) #切换窗口
        time.sleep(2)
        try:
            page = driver.find_element(by=By.XPATH, value='//*[@id="mount"]/div/div[2]/div/div/div[2]')
            #print(page)
            soup2 =BeautifulSoup(page.get_attribute('innerHTML'),"html.parser")
        except:
            print('第二页跳转失败')
        try:
            app_details = soup2.find_all('div', attrs={'class': 'app-details-row__right'})
            print(app_details)
        except:
            print("取游戏细节出错")
        try:
            iteam_name = soup2.find('div', attrs={'class': 'app-description__title'}).text
            print(iteam_name)
        except:
            iteam_name = ''
            print('获取商品名字错误')
        try:
            iteam_description = soup2.find('div', attrs={'class': 'clamped-description__content'}).text
            print(iteam_description)
        except:
            iteam_description = ''
            print('获取商品简介')
        try:
            iteam_price = soup2.find('span', attrs={'class': 'app-purchase-price'}).text
        except:
            iteam_price = ''
            print('价格失败')
        try:
            print(len(app_details))
            print(app_details[0].text)
            print(app_details[1].text)
            print(app_details[2].text)
            print(app_details[3].text)
            print(app_details[4].text)
            print(app_details[5].text)
            print(app_details[6].text)
            print(app_details[7].text)
            print(app_details[8].text)
            print(app_details[9].text)
            print(app_details[10].text)
            print(app_details[11].text)
            print(app_details[12].text)
            print(app_details[13].text)
            try:
                if(app_details[14] in app_details):
                    app_details[13] = app_details[14]
                    print(app_details[13])
            except:
                print('列表没有14')
            dataframe = dataframe.append(pd.DataFrame({
                'Game_Id': id1,
                'Game_Name': iteam_name,
                'Game_price': iteam_price,
                'Game_description': iteam_description,
                'Game_Modes': app_details[0].text,
                'Game_PlayerModes': app_details[1].text,
                'Game_Controllers': app_details[2].text,
                'Game_Platforms': app_details[3].text,
                'Category': app_details[4].text,
                'Game_Genres': app_details[5].text,
                'Game_Languages': app_details[6].text,
                'Game_Version': app_details[7].text,
                'Game_Developer': app_details[8].text,
                'Game_Publisher': app_details[9].text,
                'Game_Website': app_details[10].text,
                'Game_ReleaseDate': app_details[11].text,
                'Game_Policy': app_details[12].text,
                'Game_Space': app_details[13].text,
            },
                index=[count]))
            count += 1
            print(count)
            print(id1+'.csv')
            n = n + 1
            time.sleep(1)
            driver.get(website)
            driver.maximize_window()
            time.sleep(2)
            try:  # 获取id后每次取玩页面信息之后还要把所有页面都拉出来才能继续
                page = driver.find_element(by=By.XPATH, value='//*[@id="footer-ssr"]/div/div[1]')
                while (k < 38):
                    k = k+1
                    driver.execute_script("arguments[0].scrollIntoView()", page)
                    print('k=', k)
                    time.sleep(1)

            except:
                print('第二次拉页面拉错了')
            k = 0
            dataframe.to_csv("3gameMessage.csv", index=False, sep=',', encoding='utf_8_sig')
            break
        except:
            print("写文件出错")


    # try:
    #     game_Modes = soup2.find('div',attrs={'class':'app-details-row__right'})
    # except:
    #     game_playWays = soup2.find('')
    #
    #
















