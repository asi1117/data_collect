# 导包
import csv
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import textblob
import nltk
nltk.download('punkt')
nltk.download('stopwords')




# 文档读取
def read_file(file_path):
    file = os.listdir(file_path)
    for i in file:
        file_name = file_path+'/'+i
        return file_name
#利用textblob 构建模型
def text_blb(filename,write1_path,write2_path,write3_path):
    pf1 = pd.DataFrame()
    pf2 = pd.DataFrame()
    pf3 = pd.DataFrame()
    pf4 = pd.DataFrame()
    pf5 = pd.DataFrame()
    pf6 = pd.DataFrame()
    pf7 = pd.DataFrame()
    pf8 = pd.DataFrame()
    pf9 = pd.DataFrame()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader((line.replace('\0','') for line in f))
        # total_tags =[]
        head = next(reader)
        for row in reader:
            #积极的情况
            if int(row[6]) >= 4:
                if row[4]:
                    pd.set_option('mode.chained_assignment', None)
                    blob1 = textblob.TextBlob(row[4])
                    tags = blob1.tags
                    print(tags)
                    toal_adj_word = ''
                    toal_noun_word = ''
                    toal_verb_word = ''
                    for y in tags:
                        if y[1] == 'JJ' or y[1] == 'JJR' or y[1] == 'JJS':
                            #print(y[0])
                            toal_adj_word += y[0] + ' '
                        if y[1] == 'NN' or y[1] == 'NNS':
                            toal_noun_word += y[0]+' '
                        if y[1] == 'VB' or y[1] == 'VBG' or y[1] == 'VBD' or y[1] == 'VBN' or y[1] == 'VBP':
                            toal_verb_word = y[0] + ' '
                    #存adj
                    pf1 = pf1.append(pd.DataFrame({
                        'author': row[2],
                        'adj': toal_adj_word,
                        'helpful': row[7],
                    },
                        index=[count1]))
                    count1 += 1
                    print(count1)
                    #存noun
                    pf2 = pf2.append(pd.DataFrame({
                        'author': row[2],
                        'noun': toal_noun_word,
                        'helpful': row[7],
                    },
                        index=[count2]))
                    count2 += 1
                    print(count2)
                    #存verb
                    pf3 = pf3.append(pd.DataFrame({
                        'author': row[2],
                        'verb': toal_verb_word,
                        'helpful': row[7],
                    },
                        index=[count3]))
                    count3 += 1
                    print(count3)
                pf1.to_csv(write1_path + "adj.csv", index=False, sep=',', encoding='utf_8_sig')
                pf2.to_csv(write1_path + "noun.csv", index=False, sep=',', encoding='utf_8_sig')
                pf3.to_csv(write1_path + "verb.csv", index=False, sep=',', encoding='utf_8_sig')
            if int(row[6]) == 3:
                if row[4]:
                    pd.set_option('mode.chained_assignment', None)
                    blob1 = textblob.TextBlob(row[4])
                    tags = blob1.tags
                    print(tags)
                    toal_adj_word = ''
                    toal_noun_word = ''
                    toal_verb_word = ''
                    for y in tags:
                        if y[1] == 'JJ' or y[1] == 'JJR' or y[1] == 'JJS':
                            #print(y[0])
                            toal_adj_word += y[0] + ' '
                        if y[1] == 'NN' or y[1] == 'NNS':
                            toal_noun_word += y[0]+' '
                        if y[1] == 'VB' or y[1] == 'VBG' or y[1] == 'VBD' or y[1] == 'VBN' or y[1] == 'VBP':
                            toal_verb_word = y[0] + ' '
                    #存adj
                    pf4 = pf4.append(pd.DataFrame({
                        'author': row[2],
                        'adj': toal_adj_word,
                        'helpful': row[7],
                    },
                        index=[count4]))
                    count4 += 1
                    print(count4)
                    #存noun
                    pf5 = pf5.append(pd.DataFrame({
                        'author': row[2],
                        'noun': toal_noun_word,
                        'helpful': row[7],
                    },
                        index=[count5]))
                    count5 += 1
                    print(count5)
                    #存verb
                    pf6 = pf6.append(pd.DataFrame({
                        'author': row[2],
                        'verb': toal_verb_word,
                        'helpful': row[7],
                    },
                        index=[count6]))
                    count6 += 1
                    print(count6)
                pf4.to_csv(write2_path + "adj.csv", index=False, sep=',', encoding='utf_8_sig')
                pf5.to_csv(write2_path + "noun.csv", index=False, sep=',', encoding='utf_8_sig')
                pf6.to_csv(write2_path + "verb.csv", index=False, sep=',', encoding='utf_8_sig')
            if int(row[6]) <= 2:
                if row[4]:
                    pd.set_option('mode.chained_assignment', None)
                    blob1 = textblob.TextBlob(row[4])
                    tags = blob1.tags
                    print(tags)
                    toal_adj_word = ''
                    toal_noun_word = ''
                    toal_verb_word = ''
                    for y in tags:
                        if y[1] == 'JJ' or y[1] == 'JJR' or y[1] == 'JJS':
                            #print(y[0])
                            toal_adj_word += y[0] + ' '
                        if y[1] == 'NN' or y[1] == 'NNS':
                            toal_noun_word += y[0]+' '
                        if y[1] == 'VB' or y[1] == 'VBG' or y[1] == 'VBD' or y[1] == 'VBN' or y[1] == 'VBP':
                            toal_verb_word = y[0] + ' '
                    #存adj
                    pf7 = pf7.append(pd.DataFrame({
                        'author': row[2],
                        'adj': toal_adj_word,
                        'helpful': row[7],
                    },
                        index=[count7]))
                    count7 += 1
                    print(count7)
                    #存noun
                    pf8 = pf8.append(pd.DataFrame({
                        'author': row[2],
                        'noun': toal_noun_word,
                        'helpful': row[7],
                    },
                        index=[count8]))
                    count8 += 1
                    print(count8)
                    #存verb
                    pf9 = pf9.append(pd.DataFrame({
                        'author': row[2],
                        'verb': toal_verb_word,
                        'helpful': row[7],
                    },
                        index=[count9]))
                    count9 += 1
                    print(count9)
                pf7.to_csv(write3_path + "adj.csv", index=False, sep=',', encoding='utf_8_sig')
                pf8.to_csv(write3_path + "noun.csv", index=False, sep=',', encoding='utf_8_sig')
                pf9.to_csv(write3_path + "verb.csv", index=False, sep=',', encoding='utf_8_sig')

if __name__ == '__main__':
    file_path = 'C:/Users/ENeS/Desktop/datasets/HDMs/Totle/DRR/First'
    write1_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Positive/'
    write2_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Neutral/'
    write3_path = 'C:/Users/ENeS/Desktop/datasets/SentimentAnalyze/DRR/First/Negative/'
    filename = read_file(file_path)
    text_blb(filename, write1_path, write2_path, write3_path)