'''

'''


import datetime
import time

import requests
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sys
import  json
import csv


# def get_html(url):
#     headers = {
#         'Accept': '*/*',
#         'Accept-Language': 'en-US,en;q=0.8',
#         'Cache-Control': 'max-age=0',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',
#         'Connection': 'keep-alive'
#         # 'Referer': 'https://store.steampowered.com/'
#     }


if __name__ == '__main__':
        dataframe = pd.DataFrame()
        headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',
                    'Connection': 'keep-alive'
                    # 'Referer': 'https://store.steampowered.com/'
                }
        count = 0
        for i in range(1,18):
            url = 'https://www.amazon.co.uk/Samsung-SM-R324NZAABTU-Galaxy-Controller-Version/product-reviews/B07142L1V6/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
            print(url)
            page = requests.get(url, headers=headers)
            #print(type(page))
            html = page.content
            soup = BeautifulSoup(html, "html.parser")
            try:
                reviewCount = soup.find('div', attrs={'data-hook': 'cr-filter-info-review-rating-count'}).text.strip().split(',')[1]
            except:
                reviewCount =''
                print("没有总共的评论数")
            try:
                reviewsList = soup.find_all('div', attrs={'class': 'a-section review aok-relative'})
                print(len(reviewsList))
            except:
                print('抓取总评论数有问题')
            time.sleep(1)
            for review in reviewsList:
                try:
                    scrap_date = datetime.datetime.now()

                except:
                    scrap_date = ' '
                try:
                    reviewConment = review.find('span', attrs={'data-hook': 'review-body'}).text.strip()
                except:
                    reviewConment = " "
                    print("评论出错")
                try:
                    reviewauthor = review.find('span', attrs={'class': 'a-profile-name'}).text.strip()
                    print(reviewauthor)
                except:

                    reviewauthor = " "
                    print("作者出错")
                try:
                    reviewTitle = review.find('a', attrs={'data-hook': 'review-title'}).text.strip()
                except:
                    reviewTitle = " "
                    print('标题出错')
                try:
                    reviewRating = review.find('span', attrs={'class':'a-icon-alt'}).text.split(" ")[0]
                except:
                    reviewRating = " "
                    print("评分出错")
                try:
                    reviewHelpful = review.find('span', attrs={'data-hook': 'helpful-vote-statement'}).text.split(" ")[0]
                    if reviewHelpful == 'One':
                        reviewHelpful = '1.0'
                except:
                    reviewHelpful = "0"
                try:
                    reviewDate = review.find('span', attrs={'data-hook': 'review-date'}).text.strip()
                except:
                    reviewDate = ' '
                    print('日期出错')
                try:
                    dataframe = dataframe.append(pd.DataFrame({
                        'scrapping_date': scrap_date,
                        'review_author': reviewauthor,
                        'review_title': reviewTitle,
                        'one_reviews_text': reviewConment,
                        'review_date': reviewDate,
                        'review_rating': reviewRating,
                        'review_helpful': reviewHelpful,
                        'review_count': reviewCount
                        },
                        index=[count]))
                    count += 1
                    print(count)
                    dataframe.to_csv('Amazon_UK_GearReviews.csv', index=False, sep=',', encoding='utf_8_sig')
                except:
                    print('写评论出错')





