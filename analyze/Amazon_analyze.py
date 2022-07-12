#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:18:27 2021

@author: jialinshang
"""
#%%% relevent packages & modules
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
file_path = 'C:/Users/ENeS/Desktop/datasets/EnglishFliter/Amazon/HTCvivecosmos/English'
file_list = os.listdir(file_path)
for id in file_list:
    #%%% data preparetion
    dta = pd.read_csv(file_path+'/'+id).reset_index()

    #filter out noise information
    pd.set_option('mode.chained_assignment', None)
    dta1 = dta[['index','one_reviews_text','review_rating','review_helpful',]].copy()
    #print(dta1)

    #Cleaning the review_text
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("n't"," not")
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("I'm","I am")
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("'ll"," will")
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("It's","It is")
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("it's","It is")
    dta1['one_reviews_text'] = dta1['one_reviews_text'].str.replace("that's","that is")

    # #%%% review distribution
    # Rating_count=dta1['review_rating'].value_counts()
    # explode = (0, 0.1, 0.2, 0.2, 0.1)
    # fig1, ax1 = plt.subplots()
    # ax1.pie(Rating_count,explode=explode,labels=Rating_count.index,autopct='%1.1f%%', shadow=True,startangle=140)
    # ax1.axis('equal')
    # plt.tight_layout()
    # plt.show()

    dta1['review_rating'].value_counts()
    sns.countplot(data=dta1, x='review_rating')
    neutral = dta1[dta1['review_rating']==3]
    positive = dta1[dta1['review_rating']>=4]
    negative = dta1[dta1['review_rating']<=2]

    total_rated_review = len(neutral)+len(positive)+len(negative)
    print(total_rated_review)

    #calculate average rating of all reviews
    rating_mean = dta1['review_rating'].mean()
    print("Average rating of all reviews:",round(rating_mean,2),"/",5)

    #calculate review length and average length of low-rating reviews
    negative['review length'] = negative['one_reviews_text'].str.len()
    low_review_avg =negative['review length'].mean()
    print('The average length of low-rating reviews is',round(low_review_avg),".")

    #calculate portion of low-rating reviews
    print("Portion of low-rating reviews:", len(negative),"/",total_rated_review, "(",round((len(negative)/total_rated_review),2),")")

    #%%% Analyze Word Frequency
    #positive
    corpus_positive = positive.one_reviews_text.to_list()
    vectorizer = CountVectorizer(lowercase = True,
                                  ngram_range = (2,3),
                                  max_df = 0.9,
                                  min_df = 0.001,
                                  stop_words='english');
    X = vectorizer.fit_transform(corpus_positive)
    columns=vectorizer.get_feature_names()
    df=pd.DataFrame(X.toarray(),columns=columns)
    df=df.sum(axis=0)
    df = df.sort_values(ascending = False).head(20)
    print(df)
    df0 = df.sort_values(ascending = True)
    fig1=df0.plot.barh(x='freq', width=0.5)
    plt.show()
    corpus_positive = positive.one_reviews_text.to_list()
    vectorizer = CountVectorizer(lowercase   = True,
                                  ngram_range = (3,3),
                                  max_df      = 0.9,
                                  min_df      = 0.001,
                                  stop_words='english');
    X = vectorizer.fit_transform(corpus_positive)
    columns=vectorizer.get_feature_names()
    df2=pd.DataFrame(X.toarray(),columns=columns)
    df2=df2.sum(axis=0)
    df2 = df2.sort_values(ascending = False).head(15)
    print(df2)
    df0 = df2.sort_values(ascending = True)
    fig1=df0.plot.barh(x='freq', width=0.5)
    plt.show()


    # corpus_positive = positive.one_reviews_text.to_list()
    # vectorizer = CountVectorizer(lowercase   = True,
    #                               ngram_range = (4,5),
    #                               max_df      = 0.9,
    #                               min_df      = 0.001,
    #                               stop_words='english');
    # X = vectorizer.fit_transform(corpus_positive)
    # columns=vectorizer.get_feature_names()
    # df2=pd.DataFrame(X.toarray(),columns=columns)
    # df2=df2.sum(axis=0)
    # df2 = df2.sort_values(ascending = False).head(15)
    # print(df2)
    # df0 = df2.sort_values(ascending = True)
    # fig1=df0.plot.barh(x='freq', width=0.5)
    #
    # negative
    corpus_negative = negative.one_reviews_text.to_list()
    vectorizer = CountVectorizer(lowercase=True,
                                 ngram_range=(2, 3),
                                 max_df=0.9,
                                 min_df=0.001,
                                 stop_words='english');
    X = vectorizer.fit_transform(corpus_negative)
    columns = vectorizer.get_feature_names()
    df3 = pd.DataFrame(X.toarray(), columns=columns)
    df3 = df3.sum(axis=0)
    df3 = df3.sort_values(ascending=False).head(15)
    print(df3)
    df0 = df3.sort_values(ascending=True)
    fig3 = df0.plot.barh(x='freq', width=0.5)

    #negative
    corpus_negative     = negative.one_reviews_text.to_list()
    vectorizer  = CountVectorizer(lowercase = True,
                                  ngram_range = (3,3),
                                  max_df = 0.9,
                                  min_df = 0.001,
                                  stop_words='english');
    X  = vectorizer.fit_transform(corpus_negative)
    columns=vectorizer.get_feature_names()
    df3=pd.DataFrame(X.toarray(),columns=columns)
    df3=df3.sum(axis=0)
    df3 = df3.sort_values(ascending = False).head(15)
    print(df3)
    df0 = df3.sort_values(ascending = True)
    fig3=df0.plot.barh(x='freq', width=0.5)
    # plt.show()

