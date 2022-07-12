import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
#提取含有指定字符的行


def price(filepath,writepath):
    id_list = os.listdir(filepath)
    for i in id_list:
        df2 = pd.DataFrame()
        print(df2)
        df = pd.read_csv(filepath+'/'+i, sep=',', encoding='utf-8')
        #bargain|Premium|sixpenny|cut-price|low-cost|sale|appreciation|
        #|value|$|expensive|cost|dear|cheap|money|worth|pay|afford
        df2 = df[df['one_reviews_text'].str.contains(pat='price|value|/$|expensive|cost|dear|cheap|money|worth|pay|afford|bargain|Premium|sixpenny|cut-price|low-cost|sale|appreciation', regex=True,
                                                     case=False)]
        author = df2['review_author']
        review = df2['one_reviews_text']
        rating = df2['review_rating']
        helpful = df2['review_helpful']
        print(author)
        #df2.to_csv(writepath + i, sep=',', index=False, encoding='utf-8')
        df3 = pd.DataFrame({
            'author': author,
            'review': review,
            'rating': rating,
            'helpful': helpful
        })
        print(df3)
        df3.to_csv(writepath + i, sep=',', index=False, encoding='utf-8')

def comfort(filepath,writepath):
    id_list = os.listdir(filepath)
    for i in id_list:
        df2 = pd.DataFrame()
        print(df2)
        df = pd.read_csv(filepath + '/' + i, sep=',', encoding='utf-8')
        # bargain|Premium|sixpenny|cut-price|low-cost|sale|appreciation|
        # |value|$|expensive|cost|dear|cheap|money|worth|pay|afford
        df2 = df[df['one_reviews_text'].str.contains(
            pat='comfort|fell',
            regex=True,
            case=False)]
        author = df2['review_author']
        review = df2['one_reviews_text']
        rating = df2['review_rating']
        helpful = df2['review_helpful']
        print(author)
        # df2.to_csv(writepath + i, sep=',', index=False, encoding='utf-8')
        df3 = pd.DataFrame({
            'author': author,
            'review': review,
            'rating': rating,
            'helpful': helpful
        })
        print(df3)
        df3.to_csv(writepath + i, sep=',', index=False, encoding='utf-8')
if __name__ == '__main__':
    filepath = 'C:/Users/ENeS/Desktop/datasets/HDMs/Totle/DRR/First'
    writepath = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/price/'

    price(filepath, writepath)