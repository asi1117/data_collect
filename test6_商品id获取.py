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

website = 'https://www.oculus.com/experiences/rift/section/1736210353282450/'

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
js = driver.find_element(by=By.XPATH,value='//*[@id="footer-ssr"]/div/div[1]')
for i in range(200):
    driver.execute_script("arguments[0].scrollIntoView()",js)
    time.sleep(3)
    print(i)
iteam_list = driver.find_elements(by=By.XPATH, value='//div[@class="section__items-cell"]')
print(len(iteam_list))
id_list = []
for n in range(len(iteam_list)):
    soup = BeautifulSoup(iteam_list[n].get_attribute('innerHTML'), "html.parser")
    id1 = soup.find('a',attrs={'class': 'store-section-item-tile'}).get('data-testid')
    id_list.append(id1)
    print(id1)
print(id_list)
print(len(id_list))
    # id = driver.find_element(by=By.XPATH, value='//a[@class="store-section-item-tile"]').get_attribute('data-testid')
    # print(id)
# while (condition_to_continue):
#     try:
#         WebDriverWait(driver, 10).until(
#             # 爬取一頁的所有的相關數據
#             EC.visibility_of_element_located((By.XPATH, "//div[@class='a-section review aok-relative']")))
#     except:
#         print("首页有个小问题")
#     reviews = driver.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")
#
#     r = 0
#
#     # Finding all the reviews in the website and bringing them to python
#     for r in range(len(reviews)):
#
#         try:
#             soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
#         except:
#             # I got an errorr saying that element is not attached to the page document
#             # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
#             WebDriverWait(driver, 10).until(
#                 EC.visibility_of_element_located((By.XPATH, "//div[@class='a-section review aok-relative']")))
#             # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
#             reviews = driver.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")
#             soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
#
#         # scrape raw html
#         try:
#             scrap_date = datetime.datetime.now()
#
#         except:
#             info = traceback.format_exc()
#             print(info)
#


















