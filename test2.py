from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get('https://www.amazon.com/-/zh/product-reviews/B07PTMKYS7/ref=cm_cr_arp_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews')
reviews = web.find_elements(by=By.XPATH, value="//div[@class='a-section review aok-relative']")
print(len(reviews))
r =0
for r in range(len(reviews)):
    soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
    review = soup.find('span',attrs = {'data-hook' : 'review-body'}).text
    print(review)