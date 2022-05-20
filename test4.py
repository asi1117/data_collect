from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get('https://www.bestbuy.ca/en-ca/product/meta-quest-2-256gb-vr-headset-with-touch-controllers/15644387/review')
reviews = web.find_elements(by=By.XPATH, value="//li[@class='review_36yjK']")
print(len(reviews))
r =0
for r in range(len(reviews)):
    soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
    review = soup.find('div', attrs={'class': 'review-rating'}).text
    print(review)