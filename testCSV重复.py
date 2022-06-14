import csv
import pandas as pd
import shutil
pf = pd.read_csv('1968697563211639.csv',engine='python')
new = pf.drop_duplicates(subset=['review_author','one_reviews_text','review_title','review_date'], keep='first')
new.to_csv('new2.csv', encoding='utf-8')


