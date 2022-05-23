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
Created on 2022年5月19日

@author: 盧一鈞
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

website = 'https://www.amazon.com/-/zh/product-reviews/B07VPRVBFF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

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
            EC.visibility_of_element_located((By.XPATH, "//div[@class='a-section review aok-relative']")))
    except:
        print("首页有个小问题")
    reviews = driver.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")

    r = 0

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
            print(review_title)
        try:
            review_rating = soup.find('i', attrs={'data-hook': 'review-star-rating'}).text.split('.')[0]
            print(review_rating)
        except:
            review_rating = soup.find('i', attrs={'data-hook': 'cmps-review-star-rating'}).text.split('.')[0]
            print(review_rating)
        try:
            size = soup.find('a', attrs={'class': 'a-size-mini a-link-normal a-color-secondary'}).text.split(':')[1]
            print(size)
        except:
            size = ''
            print('size抓取失敗')
        dataframe = dataframe.append(pd.DataFrame({
            'scrapping_date': scrap_date,
            'one_reviews_text': review_text,
            'review_date': review_data,
            'review_rating': review_rating,
            'size': size,
            'review_title':  review_title
            },
            index=[count]))
        count += 1
        print(count)
        dataframe.to_csv("Amazon_US_Valve_Index_reviews.csv", index=False, sep=',', encoding='utf_8_sig')

    before = driver.page_source
    driver.find_element(by=By.XPATH, value='//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
    after = driver.page_source
    if before == after:
        time_end = time.time()
        print('縂耗時', time_end - time_star, 's')
        break
    else:
        time.sleep(10)

# %%% data cleaning


















