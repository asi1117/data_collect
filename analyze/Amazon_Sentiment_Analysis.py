import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

def pos_neg(file1,file2):
    file = os.listdir(file1)
    for i in file:
        dta1 = pd.read_csv(file1+'/'+i).reset_index()
        #%%% review distribution
        Rating_count=dta1['review_rating'].value_counts()
        pos = 0
        neu = 0
        neg = 0
        for i in range(1, 6):
            if i >= 4:
                pos += Rating_count.get(i)
            if i == 3:
                neu += Rating_count.get(i)
            if i <= 2:
                neg += Rating_count.get(i)
        y = np.array([pos, neu, neg])
        print(Rating_count)
        print(Rating_count.get(5))
        print(type(Rating_count))
        explode = (0, 0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(y,explode=explode,labels=['positive', 'neutral','negative'], labeldistance=0.88, autopct='%1.1f%%',
                startangle=140)
        ax1.axis('equal')
        plt.tight_layout()
        plt.title('Emotion ratio chart', y=0.98)
        plt.savefig(file2 + '/' + 'rating.jpg', dpi=500)
        plt.show()

def word_sentimentAnalysis(file_path, neg_file_path, nor_file_path):
    file1 = os.listdir(file_path)
    for i in file1:
        if i == 'adj.csv':

            dta=pd.read_csv(file_path+'/'+i).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['adj']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='adi_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Positive High Frequency Adj')  # 图形标题
            plt.savefig(file_path+'/'+'adj.jpg', dpi=500)
            plt.show()
        if i == 'noun.csv':
            dta = pd.read_csv(file_path + '/' + i).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['noun']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1, 1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig2 = df0.plot.barh(x='noun_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Positive High Frequency Noun')  # 图形标题
            plt.savefig(file_path + '/' + 'noun.jpg', dpi=500)
            plt.show()
        if i == 'verb.csv':

            dta = pd.read_csv(file_path+'/'+i).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

            pos = dta1['verb']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='verb_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Positive High Frequency Verb')  # 图形标题
            plt.savefig(file_path+'/'+'verb.jpg', dpi=500)
            plt.show()
    file2 = os.listdir(neg_file_path)
    for j in file2:
        if j == 'adj.csv':

            dta=pd.read_csv(neg_file_path+'/'+j).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['adj']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='adi_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Negative High Frequency Adj')  # 图形标题
            plt.savefig(neg_file_path+'/'+'adj.jpg', dpi=500)
            plt.show()
        if j == 'noun.csv':
            dta = pd.read_csv(neg_file_path + '/' + j).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['noun']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1, 1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig2 = df0.plot.barh(x='noun_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Negative High Frequency Noun')  # 图形标题
            plt.savefig(neg_file_path + '/' + 'noun.jpg', dpi=500)
            plt.show()
        if j == 'verb.csv':

            dta = pd.read_csv(neg_file_path+'/'+j).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

            pos = dta1['verb']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='verb_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Negative High Frequency Verb')  # 图形标题
            plt.savefig(neg_file_path+'/'+'verb.jpg', dpi=500)
            plt.show()
    file3 = os.listdir(nor_file_path)
    for k in file3:

        if k == 'adj.csv':

            dta=pd.read_csv(nor_file_path+'/'+k).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['adj']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='adi_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Neutral High Frequency Adj')  # 图形标题
            plt.savefig(nor_file_path+'/'+'adj.jpg', dpi=500)
            plt.show()
        if k == 'noun.csv':
            dta = pd.read_csv(nor_file_path + '/' + k).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
            pos = dta1['noun']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1, 1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig2 = df0.plot.barh(x='noun_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Neutral High Frequency Noun')  # 图形标题
            plt.savefig(nor_file_path + '/' + 'noun.jpg', dpi=500)
            plt.show()
        if k == 'verb.csv':

            dta = pd.read_csv(nor_file_path+'/'+k).reset_index()
            dta1 = dta.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

            pos = dta1['verb']
            # pos_adj = pos.to_list()
            # print(pos_adj)
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            vectorizer = CountVectorizer(lowercase=True,
                                         ngram_range=(1,1),
                                         max_df=0.9,
                                         min_df=0.001,
                                         stop_words='english');
            X = vectorizer.fit_transform(pos.values.astype('U'))
            print(X)
            columns = vectorizer.get_feature_names()
            df = pd.DataFrame(X.toarray(), columns=columns)
            df = df.sum(axis=0)
            df = df.sort_values(ascending=False).head(15)
            print(df)
            df0 = df.sort_values(ascending=True)
            fig1 = df0.plot.barh(x='verb_freq', width=0.5)
            plt.xlabel('frequency')  # 纵坐标轴标题
            plt.title('First Type Neutral High Frequency Verb')  # 图形标题
            plt.savefig(nor_file_path+'/'+'verb.jpg', dpi=500)
            plt.show()
def paragraph_sentiment(paragraph_path,write_path):
    file = os.listdir(paragraph_path)
    stop_list =['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
                'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her',
                'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was',
                'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
                'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by',
                'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
                'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
                'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
                'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn',
                'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren',
                'won', 'wouldn','gear','samsung']
    for i in file:
        dta1 = pd.read_csv(paragraph_path+'/'+i).reset_index()
        pos = dta1['one_reviews_text'].replace('Gear',1)
        # pos_adj = pos.to_list()
        # print(pos_adj)
        fig1, ax1 = plt.subplots(figsize=(12, 8))
        vectorizer = CountVectorizer(lowercase=True,
                                     # binary=True,
                                     ngram_range=(2, 3),
                                     max_df=0.9,
                                     min_df=0.001,
                                     stop_words=stop_list);
        X = vectorizer.fit_transform(pos.values.astype('U'))
        #print(X)
        columns = vectorizer.get_feature_names()
        df = pd.DataFrame(X.toarray(), columns=columns)
        df = df.sum(axis=0)
        df = df.sort_values(ascending=False).head(20)
        print(df)
        df0 = df.sort_values(ascending=True)
        fig1 = df0.plot.barh(x='freq', width=0.5)
        plt.xlabel('frequency')  # 纵坐标轴标题
        plt.title('First Type Hot Topic')  # 图形标题
        plt.savefig(write_path + '/' + 'freq.jpg', dpi=500)
        plt.show()

if __name__ == '__main__':
    pos_file_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Positive'
    neg_file_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Negative'
    nor_file_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Neutral'
    read_file_path = 'C:/Users/ENeS/Desktop/datasets/HDMs/Totle/DRR/First'
    write_file_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First'
    pos_neg(read_file_path,write_file_path)
    # word_sentimentAnalysis(pos_file_path,neg_file_path,nor_file_path)
    # paragraph_sentiment(read_file_path, write_file_path)