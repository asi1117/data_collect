from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get("http://lagou.com")
#找到某个元素
#find_element(by=By.XPATH, value=xpath)
el = web.find_element(by=By.XPATH,value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)#让浏览器缓一会
#找到对话框，输入python -输入回车、点击搜索按钮
web.find_element(by=By.XPATH,value='//*[@id="search_input"]').send_keys('python',Keys.ENTER)

#查找数据存在的位置，进行数据提取
#找到页面存放数据的所有div
div_list = web.find_elements(by=By.XPATH,value='//*[@id="jobList"]/div[1]/div')
for div in div_list:
    #find_element(by=By.TAG_NAME, value=name)
    job_name = div.find_element(by=By.TAG_NAME, value="a").text
    job_time = div.find_element(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/span').text
    job_price = div.find_element(by=By.XPATH,value='//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[2]/span').text
    print(job_name)
    print(job_time)
    print(job_price)