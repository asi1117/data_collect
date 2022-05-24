#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月20日
主要爬取英國亞馬遜關於oculus——rifs的評論
@author: luyijun
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

"""
Created on 2022年5月24日

@author: luyijun
"""

# %%% relevent packages & modules


import pandas as pd
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import  traceback
# %%% relevent website

website = 'https://www.oculus.com/experiences/quest/2448060205267927'

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
count =0
while (condition_to_continue):
    try:
        WebDriverWait(driver, 10).until(
            # 爬取一頁的所有的相關數據
            EC.visibility_of_element_located((By.XPATH, '//div[@class="app-review"]')))
    except:
        print("首页有个小问题")
    reviews = driver.find_elements(by=By.XPATH, value='//div[@class="app-review"]')
    print(len(reviews))
    r = 0

    # Finding all the reviews in the website and bringing them to python
    for r in range(len(reviews)):

        try:
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
        except:
            # I got an errorr saying that element is not attached to the page document
            # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="app-review"]')))
            # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
            reviews = driver.find_elements(by=By.XPATH, value='//div[@class="app-review"]')
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")

        # scrape raw html
        try:
            scrap_date = datetime.datetime.now()

        except:
            info = traceback.format_exc()
            print(info)
        try:
            review_text = soup.find('div', attrs={'class': 'clamped-description__content'}).text
            print(review_text)
        except:
            review_text = ''
            info = traceback.format_exc()
            print(info)
            print("評論文本這裏有問題")
        try:
            review_data = soup.find('div', attrs={'class': 'app-review__date'}).text
            print(review_data)
        except:
            review_data = ''
            info = traceback.format_exc()
            print(info)
        try:
            review_title = soup.find('h1', attrs={'class': 'bxHeading bxHeading--level-5 app-review__title'}).text

            print(review_title)
        except:
            review_title = ''
            print('提取評論標題出異常')
            info = traceback.format_exc()
            print(info)
        try:
            review_rating = len(soup.find_all('i',attrs={'class': 'bxStars bxStars--white'}))
            print(review_rating)
        except:
            review_rating = ''
            print('提取評分出異常')
            info = traceback.format_exc()
            print(info)
        dataframe = dataframe.append(pd.DataFrame({
            'scrapping_date': scrap_date,
            'one_reviews_text': review_text,
            'review_date': review_data,
            'review_rating': review_rating,
            'review_title':  review_title
            },
            index=[count]))
        count += 1
        print(count)
        dataframe.to_csv("Game_BestSaber.csv", index=False, sep=',', encoding='utf_8_sig')


    driver.find_element(by=By.XPATH, value='//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[8]/div/div[3]/div[7]/button[2]/div').click()
    button_click = driver.find_element(by=By.XPATH,value='//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[8]/div/div[3]/div[7]/button[2]').get_attribute('disabled')
    if button_click:
        break
    else:
        time.sleep(10)

# %%% data cleaning


















