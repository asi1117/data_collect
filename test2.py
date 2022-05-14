from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get('https://www.bestbuy.com/site/reviews/meta-quest-2-advanced-all-in-one-virtual-reality-headset-256gb/6473857?variant=A')
web.find_element_by_xpath("//a[@data-track='Page next']").click()