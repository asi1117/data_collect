import csv
import os
import time
from functools import reduce

import pandas as pd
import glob


def hebing():
    csv_list = glob.glob('C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex/*.csv')
    print(u'共发现%s个CSV文件' % len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i, 'rb').read()
        with open('C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex/Amazon_All_ValveIndexReviews.csv',
                  'ab') as f:
            f.write(fr)
    print(u'合并完毕！')


def quchong(file):
    df = pd.read_csv(file, header=0)
    datalist = df.drop_duplicates(subset=['review_author', 'one_reviews_text'], keep='first')
    datalist.to_csv(file)


def count(file):
    count=[]
    try:
        first = 0
        with open(file, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    first += 1
            count.append(first - 1)
            print('这个', '有', first - 1)
    except:
        print('这个id没有评论' )

if __name__ == '__main__':
    hebing()
    quchong("C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex/Amazon_All_ValveIndexReviews.csv")
    time.sleep(2)
    count("C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex/Amazon_All_ValveIndexReviews.csv")
