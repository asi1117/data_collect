import csv
import pandas as pd
import shutil
pf = pd.read_csv('2124523024270629.csv',engine='python')
new = pf.drop_duplicates(subset=['review_author','one_reviews_text','review_title','review_date','review_rating','review_helpful'], keep='first')
new.to_csv('21245230242706291.csv', encoding='utf-8')


