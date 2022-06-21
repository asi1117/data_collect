
import csv
import pandas as pd
import os
from lingua import Language, LanguageDetectorBuilder
languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
filepath = 'C:/Users/ENeS/Desktop/datasets/EnglishFliter/Amazon/HTCvivecosmos'
id_list = os.listdir(filepath)
df = pd.read_csv('C:/Users/ENeS/Desktop/datasets/EnglishFliter/Amazon/HTCvivepro/Amazon_All_vivepro.csv',encoding='utf_8_sig')
reviews = df['one_reviews_text'] #pandas 根据键取值的
df_key = reviews.keys().values#keys()返回的是他的键的总和
df2 = pd.DataFrame()
for k in df_key: #根据键遍历值就
    result = detector.detect_language_of(reviews.get(k))
    if result == Language.ENGLISH:
        print('这是英文',k)

        df2 = df.iloc[k]#通过索引获取行

        print(df2)
    df2.to_csv('C:/Users/ENeS/Desktop/datasets/EnglishFliter/Amazon/HTCvivepro/Amazon_English_vivepro.csv', sep=',', encoding='utf-8_sig')
    #print(result,k)

