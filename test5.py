#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月16日

@author: luyijun
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月16日

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
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
urls = 'https://www.bestbuy.ca/api/reviews/v2/products/15644387/reviews?source=all&lang=en-CA&pageSize=10&page=1&sortBy=relevancy'

# %%% initialize chrome
# path = 'C:\python\chromedriver.exe'

# open website
driver = Chrome()
driver.get(url=urls)
driver.maximize_window()

time_star = time.time()
# %%% collect all reviews
reviews_one_store = []
condition_to_continue = True
while (condition_to_continue):
    WebDriverWait(driver, 10).until(
        # 爬取一頁的所有的相關數據
        EC.visibility_of_element_located((By.XPATH, "//li[@class='review_36yjK']")))
    # //*[@id="reviews-accordion"]/section/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/span
    reviews = driver.find_elements(by=By.XPATH, value="//li[@class='review_36yjK']")
    print(len(reviews))
    r = 0
    for count_click in range(1, 684):
        print(count_click)

        before = driver.page_source
        # //*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/a/button
        driver.find_element(by=By.XPATH,
                            value='//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/a/button').click()
        after = driver.page_source
        if before == after:
            break
        else:
            time.sleep(6)
    print(len(reviews))
    # Finding all the reviews in the website and bringing them to python
    if(int(len(reviews)>=6835)):
        for r in range(len(reviews)):
            print(r)
            one_review = {}
            one_review['scrapping_date'] = datetime.datetime.now()
            one_review['url'] = driver.current_url
            try:
                soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
            except:
                # I got an errorr saying that element is not attached to the page document
                # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
                WebDriverWait(driver, 6000).until(
                    EC.visibility_of_element_located((By.XPATH, "//li[@class='review_36yjK']")))
                # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
                reviews = driver.find_elements(by=By.XPATH, value="//li[@class='review_36yjK']")
                soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")

            # scrape raw htm
            try:
                one_review_raw = reviews[r].get_attribute('innerHTML')
            except:
                one_review_raw = ""
            #one_review['review_raw'] = one_review_raw
            # print(one_review_raw)
            # scrape review text
            try:
                one_review_text = soup.find('div', attrs={'class': 'reviewContent_XCspv'}).p.span.text
            except:
                one_review_text = ""
            one_review['one_review_text'] = one_review_text
            #print(one_review_text)
            # scrape review date
            try:
                one_review_date = soup.find('span', attrs={'class': 'locationAndTime_3MA78'}).text
            except:
                one_review_date = ""
            one_review['review_date'] = one_review_date
            print(one_review_date)
            # scrape review stars
            cont = 0
            try:
                # one_review_stars = soup.find_all('div', attrs={'class': 'ratableStar_3ea3F'}).find_all('svg',attrs={'class':'icon_q2ZYd fullStar_365cI'}).get_attribute_list('aria-hidden')
                one_review_stars = soup.find('div', attrs={'class': 'feedbackStarContainer_2eC1W'}).find_all('svg', attrs={
                    'class': 'icon_q2ZYd fullStar_365cI'})

                for i in one_review_stars:
                    cont += 1
                print(cont)

            except:
                one_review_stars = ""
            str1 = 'Rated ' + str(cont) + ' out of 5 stars'
            print(str1)
            one_review['one_review_stars'] = str1
            reviews_one_store.append(one_review)
            one_review['Rating'] = cont
        # print(one_review_stars)
    # before = driver.page_source
    # # //*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/a/button
    # driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/a/button').click()
    # after = driver.page_source
    # if before == after:
    #     break
    # else:
    #     time.sleep(6)

# check the total number of reviews
len(reviews_one_store)

# %%% data cleaning
Oculus_reviews = pd.DataFrame.from_dict(reviews_one_store)
Oculus_reviews_backup = pd.DataFrame.from_dict(reviews_one_store)
Oculus_reviews['review_raw'].map(lambda Oculus_reviews: BeautifulSoup(Oculus_reviews, "html.parser").text)
# %%% export to excel
file_name = 'Canda_Oculus_reviews256G.xlsx'
Oculus_reviews.to_excel(file_name)
time_end = time.time()
print('縂耗時', time_end - time_star, 's')

















