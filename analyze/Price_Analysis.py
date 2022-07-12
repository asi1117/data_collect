from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import os
import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analysis(file):
    text = "I am hppy today. I feel sad today."
    file_list = os.listdir(file)
    for i in file_list:
        with open(file + '/' + i, 'r', encoding='utf-8') as f:
            reader = csv.reader((line.replace('\0', '') for line in f))
            neu = 0
            pos = 0
            neg = 0
            for row in reader:
                blob = TextBlob(row[1])
                courrt = blob.correct() #先进性单词检查
                sent = courrt.sentiment
                if sent[0] == 0:
                    neu += 1
                if sent[0] <= 0:
                    neu += 1
                if sent[0] >=0:
                    pos += 1
                # neu = 0
                # pos = 0
                # neg = 0
                # for y in sent:
                #     if y[0] == 0:
                #         neu += 1
                #     if y[0] <= 0:
                #         neg += 1
                #     if y[0] >= 0:
                #         pos += 1

            y = np.array([pos, neu, neg])
            explode = (0, 0, 0.1)
            fig1, ax1 = plt.subplots()
            ax1.pie(y, explode=explode, labels=['positive', 'neutral', 'negative'], labeldistance=0.88,
                    autopct='%1.1f%%', startangle=140)
            ax1.axis('equal')
            plt.tight_layout()
            plt.title('Price Emotion Ratio Chart', y=0.98)
            plt.savefig(file + '/' + 'price_percentage.jpg', dpi=500)
            plt.show()

        # all = blob.sentiment
        # print(all)
        # print(all[0])
        # neu =0
        # pos =0
        # neg =0
        # for i in all:
        #     if i[0] == 0:
        #         neu += 1
        #     if i[0] <= 0:
        #         neg += 1
        #     if i[0] >= 0:
        #         pos += 1
        # print()


if __name__ == '__main__':
    #C:\Users\ENeS\Desktop\datasets\SentimentAnalyze\DRR\First\price
    file_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/price'

    analysis(file_path)