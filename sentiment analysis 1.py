#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:45:45 2021

@author: jialinshang
"""

#%%% relevent packages & modules
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn                         import linear_model
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model            import LogisticRegression
from sklearn.neighbors               import KNeighborsClassifier
from sklearn.metrics                 import confusion_matrix
from sklearn.metrics                 import accuracy_score
from sklearn.metrics                 import classification_report
from sklearn.metrics                 import plot_confusion_matrix

#%%% data preparetion
dta = pd.read_excel('/Users/jialinshang/Desktop/marketing/final project/BestBuy_US_Oculus_Quest2_reviews256.xlsx').reset_index()

#filter out noise information
dta1 = dta[['index','scrapping_date','one_review_text','review_date','one_review_stars','Rating']].copy()
print(dta1)

#Cleaning the review_text
dta1['one_review_text'] = dta1['one_review_text'].str.replace("n't"," not")
dta1['one_review_text'] = dta1['one_review_text'].str.replace("I'm","I am")
dta1['one_review_text'] = dta1['one_review_text'].str.replace("'ll"," will")

dta1['one_review_text'] = dta1['one_review_text'].str.replace("It's","It is")
dta1['one_review_text'] = dta1['one_review_text'].str.replace("it's","It is")
dta1['one_review_text'] = dta1['one_review_text'].str.replace("that's","that is")

#%%% data splitting
np.random.seed(1)
dta1['ML_group']   = np.random.randint(100, size = dta1.shape[0])

#80% for trainning; 10% for validating; 10% for testing
inx_train          = dta1.ML_group  <  80                                
inx_valid          = (dta1.ML_group >= 80) & (dta1.ML_group<90)          
inx_test           = (dta1.ML_group >= 90)

#%%% text vectorization
corpus      = dta1.one_review_text.to_list()
vectorizer  = CountVectorizer(lowercase   = True,
                              ngram_range = (1,1),
                              max_df      = 0.85,
                              min_df      = 0.01);
X           = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
vc_mtx=vectorizer.transform(corpus)

vc_mtx.toarray()

#%%% TVT Split
y_train   = dta1.Rating[inx_train].to_numpy()
y_valid   = dta1.Rating[inx_valid].to_numpy()
y_test    = dta1.Rating[inx_test ].to_numpy()

X_train   = X[np.where(inx_train)[0],:]
X_valid   = X[np.where(inx_valid)[0],:]
X_test    = X[np.where(inx_test) [0],:]

# check wheher all reviews are assigned to groups
X_train.shape[0]+X_valid.shape[0]+X_test.shape[0] == 5054

#%%% KNN classification
test_error_rates = []
k_max            = 20
for k in range(1,k_max+1):
    knn_model   = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train,y_train)
    y_hat_valid = knn_model.predict(X_valid)
    test_error  = 1-accuracy_score(y_valid, y_hat_valid)
    test_error_rates.append(test_error)

# minimum the test error
k =np.argmin(test_error_rates)
min(test_error_rates)
best_k=test_error_rates.index(min(test_error_rates))+1

plt.plot(range(1,k_max+1),test_error_rates)
plt.ylabel('Error Rates')
plt.xlabel('K neighbors')

confusion_matrix(y_valid, y_hat_valid)
plot_confusion_matrix(knn_model, X_valid, y_valid)
print(classification_report(y_valid, y_hat_valid))

#predict results
results_list_knn_actual = []
knn                     = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)

results_list_knn_actual.append(
        np.concatenate([knn.predict(X_train),
                 knn.predict(X_valid),
                 knn.predict(X_test )]))

results_list_knn_actual = pd.DataFrame(results_list_knn_actual).transpose()
dta2=dta1
dta2['Predicted_star']  = results_list_knn_actual[0]
#dta2 = dta2.sort_values(by='index')
#dta2.to_excel('BestBuy_US_Oculus_Quest2_reviews256.xlsx', index = False)
print(dta2)

#%%% logistic regression
categories         = pd.DataFrame(np.sort(np.unique(y_train))).reset_index() #contians that all the possible values of y
categories.columns = ['index','label']   
#
ccp_train_list = []
ccp_valid_list = []
ccp_test_list  = []

for cat in categories['label'].to_list(): #the conditional probability for each x
    y_train_c = 1*(y_train==cat) #dummy variable
    clf       = linear_model.LogisticRegression(tol          = 0.0001,
                                                max_iter     = 10000,
                                                random_state = None).fit(X_train, y_train_c)
    ccp_train_list.append(  clf.predict_proba(X_train)[:,1]) # predict the probabilities
    ccp_valid_list.append(  clf.predict_proba(X_valid)[:,1])
    ccp_test_list.append (  clf.predict_proba(X_test) [:,1])

' . Topic probability matrix'
ccp_train = pd.DataFrame(ccp_train_list).transpose()
ccp_valid = pd.DataFrame(ccp_valid_list).transpose()
ccp_test  = pd.DataFrame(ccp_test_list).transpose()
#bias estimated: the sum is not equal to one 
' . Choosing your predictive category for the y'
ccp_train['index_hat'] =  ccp_train.idxmax(axis=1) #
ccp_valid['index_hat'] =  ccp_valid.idxmax(axis=1)
ccp_test ['index_hat'] =  ccp_test.idxmax(axis=1)
ccp_train              =  ccp_train.merge(categories, 
                                         left_on  = 'index_hat' ,
                                         right_on = 'index'     , 
                                         how      = 'left').rename(columns={'label':'label_hat'}).drop(['index','index_hat'],axis=1)
ccp_valid              =  ccp_valid.merge(categories,
                                         left_on  = 'index_hat',
                                         right_on = 'index', 
                                         how      = 'left').rename(columns={'label':'label_hat'}).drop(['index','index_hat'],axis=1)
ccp_test               =  ccp_test.merge(categories,
                                         left_on  = 'index_hat' ,
                                         right_on = 'index' ,
                                         how      = 'left').rename(columns={'label':'label_hat'}).drop(['index','index_hat'],axis=1)

ccp_train['y_train']   = y_train
ccp_valid['y_valid']   = y_valid
ccp_test ['y_test']    = y_test

print({'ccp_train'  : ccp_train,'ccp_valid'  : ccp_valid,'ccp_test'   : ccp_test})


confusion_matrix(y_test, ccp_test['label_hat'])
print(classification_report(y_test, ccp_test['label_hat']))

































