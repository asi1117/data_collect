#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月14日

@author: luyijun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月14日

@author: 盧一鈞
"""

#%%% relevent packages & modules

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

#%%% relevent website

#website='https://www.bestbuy.com/site/reviews/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255?variant=A'
website='https://www.bestbuy.com/site/reviews/oculus-quest-2-advanced-all-in-one-virtual-reality-headset-256gb/6473857?variant=A'

#%%% initialize chrome
#path = 'C:\python\chromedriver.exe'

#open website
driver = Chrome()
driver.get(website)
driver.maximize_window()

time_star = time.time()
#%%% collect all reviews
reviews_one_store = []
condition_to_continue = True
while(condition_to_continue):
    WebDriverWait(driver, 10).until(
        #爬取一頁的所有的相關數據
        EC.visibility_of_element_located((By.XPATH, "//li[@class='review-item']")))
    #//*[@id="reviews-accordion"]/section/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/span
    reviews = driver.find_elements(by=By.XPATH, value="//li[@class='review-item']")
    
    r = 0

    # Finding all the reviews in the website and bringing them to python
    for r in range(len(reviews)):
        one_review ={}
        one_review['scrapping_date'] = datetime.datetime.now()
        one_review['url'] = driver.current_url
        try:                
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'),"html.parser")
        except:
            # I got an errorr saying that element is not attached to the page document
            #To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//li[@class='review-item']")))
            #reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
            reviews = driver.find_elements(by=By.XPATH,value="//li[@class='review-item']")
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
            
        # scrape raw html
        try:
            one_review_raw = reviews[r].get_attribute('innerHTML')
        except:
            one_review_raw = ""
        one_review['review_raw'] = one_review_raw
        #print(one_review_raw)
        # scrape review text
        try:
            one_review_text = soup.find('p', attrs={'class':'pre-white-space'}).text
        except:
            one_review_text = ""
        one_review['one_review_text'] = one_review_text
        print(one_review_text)
        # scrape review date
        try:
            one_review_date = soup.find('div', attrs={'class':'disclaimer v-m-right-xxs'}).text
        except:
            one_review_date = ""
        one_review['review_date'] = one_review_date
        print(one_review_date)
        # scrape review stars
        try:
            one_review_stars=soup.find('div', attrs={'class':'review-rating'}).text
        except:
            one_review_stars = ""
        one_review['one_review_stars'] = one_review_stars
        reviews_one_store.append(one_review)
        print(one_review_stars)
    before = driver.page_source
    driver.find_element(by=By.XPATH,value="//a[@data-track='Page next']").click()
    after = driver.page_source
    if before == after:
        break
    else: 
        time.sleep(6)

# check the total number of reviews       
len(reviews_one_store)

#%%% data cleaning
Oculus_reviews = pd.DataFrame.from_dict(reviews_one_store)
Oculus_reviews_backup = pd.DataFrame.from_dict(reviews_one_store)
Oculus_reviews['review_raw'].map(lambda Oculus_reviews: BeautifulSoup(Oculus_reviews, "html.parser").text)
Oculus_reviews['Rating'] = Oculus_reviews.one_review_stars.str.extract("(\d)")[[0]]

#%%% export to excel
file_name = 'BestBuy_US_Oculus_Quest2_reviews256.xlsx'
Oculus_reviews.to_excel(file_name)
time_end = time.time()
print('縂耗時', time_end - time_star, 's')

















