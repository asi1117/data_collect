'''

'''


import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import  json
import csv
sys.setrecursionlimit(2000)


# def get_html(url):
#     headers = {
#         'Accept': '*/*',
#         'Accept-Language': 'en-US,en;q=0.8',
#         'Cache-Control': 'max-age=0',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#         'Connection': 'keep-alive'
#         # 'Referer': 'https://store.steampowered.com/'
#     }
#     try:
#         r = requests.get(url, headers=headers, timeout=2000)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return BeautifulSoup(r.text, "html.parser")
#
#     except:
#         return ""


if __name__ == '__main__':
        dataframe = pd.DataFrame()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        }
        for i in range(1, 684):

            url = 'view-source:https://www.amazon.co.uk/Samsung-5&sr=8-5#customerReviews'
            page = requests.get(url, headers=headers)
            print(type(page))
            html = page.content
            soup = BeautifulSoup(html, "html.parser'")
            reviewsList =soup.find_all('div',attrs={'data-hook': 'review' })
            for review in reviewsList:
                try:
                    scrap_date = datetime.datetime.now()

                except:
                    scrap_date =' '
                try:
                    reviewConment =review.find('',attrs={})
                except:
                    reviewConment = " "
                    print("")
                try:
                    reviewauthor =review.find('',attrs={})
                except:
                    reviewauthor = " "
                try:
                    reviewTitle =review.find('',attrs={})
                except:
                    reviewTitle = " "
                try:
                    reviewRating = review.find('',attrs={})
                except:
                    reviewRating =" "
                    print("评分出错")
                try:
                    reviewHelpful = review.find('',attrs={})
                except:
                    reviewHelpful ="0"
                try:
                    reviewDate = review.find(' ', attrs={})
                except:
                    reviewDate =''
                    print('日期出错')
                try:
                    dataframe =dataframe.append(pd.DataFrame({

                    }))
                except:
                    print()





