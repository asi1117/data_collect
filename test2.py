from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get('https://www.bestbuy.ca/en-ca/product/meta-quest-2-256gb-vr-headset-with-touch-controllers/15644387/review')
web.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/a/button').click()