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

website = 'https://www.viveport.com/stores/store/redirect/___store/jp_v_enus/___from_store/jp_v_enus/uenc/aHR0cHM6Ly93d3cudml2ZXBvcnQuY29tL2dhbWUuaHRtbD9fX19zdG9yZT1qcF92X2VudXM%2C/'

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
count = 1
id_list = []
driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/button[1]').click()
while condition_to_continue:
    driver.find_element(by=By.XPATH,value='//ol[@class="js-product-list products list items product-items"]')

    iteam_list =driver.find_elements(by=By.XPATH, value='//li[@class="item product product-item product-item--release"]')
    for i in range(len(iteam_list)):
        soup = BeautifulSoup(iteam_list[i].get_attribute('innerHTML'), "html.parser")
        id = soup.find('a', attrs={'class': 'product-item-link'}).get('href').split('/')[3]
        id_list.append(id)
    print('页数：',count)
    if count ==54:
        print(id_list)
        print(len(id_list))
    count = count+1
    before = driver.page_source
    driver.find_elements(by=By.XPATH,value='//li[@class="item pages-item-next"]')[1].click()

    after = driver.page_source
    if before == after:
        print(id_list)
        print(len(id_list))
        break
    else:
        time.sleep(4)
# js = driver.find_element(by=By.XPATH,value='//*[@id="footer-ssr"]/div/div[1]')
# for i in range():
#     driver.execute_script("arguments[0].scrollIntoView()",js)
#     time.sleep(3)
#     print(i)
# iteam_list = driver.find_elements(by=By.XPATH, value='//div[@class="section__items-cell"]')
# print(len(iteam_list))
# id_list = []
# for n in range(len(iteam_list)):
#     soup = BeautifulSoup(iteam_list[n].get_attribute('innerHTML'), "html.parser")
#     id1 = soup.find('a',attrs={'class': 'store-section-item-tile'}).get('data-testid')
#     id_list.append(id1)
#     print(id1)
# print(id_list)
# print(len(id_list))
    # id = driver.find