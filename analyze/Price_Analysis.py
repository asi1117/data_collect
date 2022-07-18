from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import os
import csv
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from numba import cuda
# print(cuda.gpus)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print('1')
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
                try:
                    blob = TextBlob(row[1])
                    courrt = blob.correct() #先进性单词检查
                    sent = courrt.sentiment
                    if sent[0] == 0:
                        neu += 1
                    if sent[0] < 0:
                        neg += 1
                    if sent[0] > 0:
                        pos += 1
                    print(pos)
                except Exception as e:
                    print("错误")
                    print(e)
                    continue
            y = np.array([pos, neu, neg])
            explode = (0, 0, 0.1)
            fig1, ax1 = plt.subplots()

            def make_autopct(y):
                def my_autopct(pct):
                    total = sum(y)
                    val = int(round(pct * total / 100.0))
                    # 同时显示数值和占比的饼图
                    return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

                return my_autopct
            ax1.pie(y, explode=explode, labels=['positive', 'neutral', 'negative'], labeldistance=0.88,
                    autopct=make_autopct(y), startangle=90)
            ax1.axis('equal')
            plt.tight_layout()
            plt.title('Second Type Cybersickness Emotion Ratio Chart', y=0.98)
            plt.savefig(file + '/' + 'Cybersickness_percentage.jpg', dpi=500)
            plt.show()
def price(file):
    text = "I am hppy today. I feel sad today."
    file_list = os.listdir(file)

    for i in file_list:
        with open(file + '/' + i, 'r', encoding='utf-8') as f:
            reader = csv.reader((line.replace('\0', '') for line in f))
            neu = 0
            pos = 0
            neg = 0
            for row in reader:
                try:
                    blob = TextBlob(row[1])
                    courrt = blob.correct() #先进性单词检查
                    sent = courrt.sentiment
                    if sent[0] == 0:
                        neu += 1
                    if sent[0] < 0:
                        neg += 1
                    if sent[0] > 0:
                        pos += 1
                    print(pos)
                except Exception as e:
                    print("错误")
                    print(e)
                    continue
            y = np.array([pos, neu, neg])
            explode = (0, 0, 0.1)
            fig1, ax1 = plt.subplots()

            def make_autopct(y):
                def my_autopct(pct):
                    total = sum(y)
                    val = int(round(pct * total / 100.0))
                    # 同时显示数值和占比的饼图
                    return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
                return my_autopct
            ax1.pie(y, explode=explode, labels=['positive', 'neutral', 'negative'], labeldistance=0.88,
                    autopct=make_autopct(y), startangle=90)
            ax1.axis('equal')
            plt.tight_layout()
            plt.title('Second Type Price Emotion Ratio Chart', y=0.98)
            plt.savefig(file + '/' + 'Price_percentage.jpg', dpi=500)
            plt.show()
def perform(file):
    text = "I am hppy today. I feel sad today."
    file_list = os.listdir(file)

    for i in file_list:
        with open(file + '/' + i, 'r', encoding='utf-8') as f:
            reader = csv.reader((line.replace('\0', '') for line in f))
            neu = 0
            pos = 0
            neg = 0
            for row in reader:
                try:
                    blob = TextBlob(row[1])
                    courrt = blob.correct() #先进性单词检查
                    sent = courrt.sentiment

                    if sent.polarity() == 0:
                        neu += 1
                    if sent.polarity() < 0:
                        neg += 1
                    if sent.polarity() > 0:
                        pos += 1
                    print(pos)
                except Exception as e:
                    print("错误")
                    print(e)
                    continue
            y = np.array([pos, neu, neg])
            explode = (0, 0, 0.1)
            fig1, ax1 = plt.subplots()

            def make_autopct(y):
                def my_autopct(pct):
                    total = sum(y)
                    val = int(round(pct * total / 100.0))
                    # 同时显示数值和占比的饼图
                    return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
                return my_autopct
            ax1.pie(y, explode=explode, labels=['positive', 'neutral', 'negative'], labeldistance=0.88,
                    autopct=make_autopct(y), startangle=90)
            ax1.axis('equal')
            plt.tight_layout()
            plt.title('Second Type Performance Emotion Ratio Chart', y=0.98)
            plt.savefig(file + '/' + 'Performance_percentage.jpg', dpi=500)
            plt.show()
if __name__ == '__main__':
    #C:\Users\ENeS\Desktop\datasets\SentimentAnalyze\DRR\First\price
    time_start = time.time()
    file_path = 'C:/Users/Admi/Desktop/test/second/price'
    file2_path = 'C:/Users/Admi/Desktop/test/second/perform'
    file3_path = 'C:/Users/Admi/Desktop/test/second/skiness'
    analysis(file3_path)
    price(file_path)
    perform(file2_path)
    time_end = time.time()
    print("用时",time_end-time_start)