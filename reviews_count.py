import csv
import os
import time
from functools import reduce

import pandas as pd
import glob


filepath = 'C:/Users/ENeS/Desktop/datasets/HTCprot/iteam_review'
id_list = os.listdir(filepath)
worry_list = []
for id in id_list:
    try:
        first = 0
        path = 'C:/Users/ENeS/Desktop/datasets/HTCprot/iteam_review/'+id
        with open(path, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                review_count = row[7].replace('review(s)','')
                if row:
                    first += 1
            print('这个', '有', first - 1)
            if int(review_count) >(first-1) & (int(review_count) - first) > 5:
                print(path.split('/')[8])
                worr_id = path.split('/')[8].split('.')[0]
                worry_list.append(worr_id)
                print(worry_list,"错误的")
                print(len(worry_list))
            else:
                print('这个文件没问题')
    except:
        print('这个id没有评论' )
