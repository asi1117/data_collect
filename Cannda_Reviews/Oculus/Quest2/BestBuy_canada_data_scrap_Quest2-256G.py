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


def get_html(url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'Connection': 'keep-alive'
        # 'Referer': 'https://store.steampowered.com/'
    }
    try:
        r = requests.get(url, headers=headers, timeout=2000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return BeautifulSoup(r.text, "html.parser")

    except:
        return ""


if __name__ == '__main__':
    #url = 'https://www.bestbuy.ca/api/reviews/v2/products/15644387/reviews?source=all&lang=en-CA&pageSize=10&page=1&sortBy=relevancy'
    #page = get_html(url)
    # lables =['scrapping_date','one_reviews_text','review_date','one_review_stars','Rating']
    # with open('BestBuy_Canada_Oculus_Quest2_reviews256G.csv','w',encoding='utf-8_sig') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(lables)
        dataframe = pd.DataFrame()
        for i in range(1, 684):

            url = 'https://www.bestbuy.ca/api/reviews/v2/products/15644387/reviews?source=all&lang=en-CA&pageSize=10&page=' + str(i) + '&sortBy=relevancy'
            print(url)
            page = get_html(url)
            print(type(page))
            str_text = page.text
            #print(type(str_text))
            json_text = json.loads(str_text)
            reviews_list = json_text.get('reviews')

            count = 0
            for i in reviews_list:
                dict_reviews = dict(i)
                dict_scrap_data = datetime.datetime.now()
                dict_review_text = dict_reviews.get('comment')
                dict_review_data = dict_reviews.get('submissionTime')
                dict_review_stars = dict_reviews.get('rating')
                dict_review_rating = dict_reviews.get('rating')
                print(dict_review_text)
                print(dict_review_data)
                dataframe=dataframe.append(pd.DataFrame({
                    'scrapping_date': dict_scrap_data,
                    'one_reviews_text': dict_review_text,
                    'review_date': dict_scrap_data,
                    'one_review_stars': dict_review_stars,
                    'Rating':dict_review_rating},
                    index=[count]))
                count += 1
                dataframe.to_csv("BestBuy_Canada_Oculus_Quest2_reviews256G.csv", index=False, sep=',', encoding='utf_8_sig')
                print(count)
                # writer.writerows(wdata)