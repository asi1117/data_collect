#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月19日
爬取了亞馬遜上在美國的評論
@author: luyijun
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import traceback

"""
Created on 2022年5月19日

@author: 盧一鈞
"""

# %%% relevent packages & modules

import gc
import os
import pandas as pd
import numpy as np
import re
import shelve
import time
import datetime
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# %%% relevent website

# website='https://www.bestbuy.com/site/reviews/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255?variant=A'
website = 'https://www.amazon.com/-/zh/product-reviews/B07PTMKYS7/ref=cm_cr_arp_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews'

# %%% initialize chrome
# path = 'C:\python\chromedriver.exe'

# open website
driver = Chrome()
driver.get(website)
driver.maximize_window()

time_star = time.time()
# %%% collect all reviews
reviews_one_store = []
condition_to_continue = True
# lables = ['scrapping_date', 'one_reviews_text', 'review_date', 'one_review_stars', 'title']
# with open('Amazon_US_Oculus_rifs.csv', 'w', encoding='utf-8_sig',
#               newline='') as f:  # 注意要這個裏面的屬性 newline是刪除空行
#     writer = csv.writer(f)
#     writer.writerow(lables)
dataframe = pd.DataFrame()
while (condition_to_continue):
    WebDriverWait(driver, 10).until(
        # 爬取一頁的所有的相關數據
        EC.visibility_of_element_located((By.XPATH, "//div[@class='a-section review aok-relative']")))
    # //*[@id="reviews-accordion"]/section/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/span
    reviews = driver.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")

    r = 0
    count =0
    # Finding all the reviews in the website and bringing them to python
    for r in range(len(reviews)):

        try:
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
        except:
            # I got an errorr saying that element is not attached to the page document
            # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='a-section review aok-relative']")))
            # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
            reviews = driver.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")

            # scrape raw html
            try:
                scrap_date = datetime.datetime.now()

            except:
                info = traceback.format_exc()
                print(info)
            try:
                review_text = soup.find('span', attrs={'data-hook': 'review-body'}).text
                print(review_text)
            except:
                review_text = ''
                info = traceback.format_exc()
                print(info)
                print("評論文本這裏有問題")
            try:
                review_data = soup.find('span', attrs={'data-hook': 'review-date'}).text
                print(review_data)
            except:
                review_data = ''
                info = traceback.format_exc()
                print(info)
            try:
                review_title = soup.find('a', attrs={'data-hook': 'review-title'}).text

                print(review_title)
            except:
                review_title = soup.find('span', attrs={'data-hook': 'review-title'}).text
                print('提取評論標題出異常')
                info = traceback.format_exc()
                print(info)
            try:
                review_rating = soup.find('i', attrs={'data-hook': 'review-star-rating'}).text.split('.')[0]
                print(review_rating)
            except:
                review_rating = soup.find('i', attrs={'data-hook': 'cmps-review-star-rating'}).text.split('.')[0]
                print('提取評分出異常')
                info = traceback.format_exc()
                print(info)
            dataframe = dataframe.append(pd.DataFrame({
                'scrapping_date': scrap_date,
                'one_reviews_text': review_text,
                'review_date': review_data,
                'review_rating': review_rating,
                'review_title': review_title},
                index=[count]))
            count += 1
            dataframe.to_csv("Amazon_UK_Oculus_rifs_reviews.csv", index=False, sep=',', encoding='utf_8_sig')

# check the total number of reviews

# %%% data cleaning

time_end = time.time()
print('縂耗時', time_end - time_star, 's')

















