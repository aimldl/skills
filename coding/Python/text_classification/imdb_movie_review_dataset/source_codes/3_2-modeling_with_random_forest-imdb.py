#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6-modeling_with_random_forest-imdb_movie_review_dataset.py

Previously,
pnlp-4_english-4_modeling_with_random_forest-refactored.py
pnlp-4_text_classification-english_sentiment_analysis-...

This is a refactorized version.
There're some minor changes in the variable names and so on.

Source: Python Natural Language Processing
Advanced machine learning and deep learning techniques for natural language processing
Jalaj Thanaki

파이썬 자연어 처리의 이론과 실제
효율적인 자연어 처리를 위한 머신 러닝과 딥러닝 구현하기
04. 텍스트분류 > 01. 영어 텍스트 분류
pp.146~212

* Dataset
IMDB Movie Review

Bag of Words Meets Bags of Popcorn
https://www.kaggle.com/c/word2vec-nlp-tutorial
"""
import os

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#%%##################
# Directory & Files #
#####################
dir_data_in = '../data/input/'
dir_data_out = '../data/output/'

if not os.path.exists( dir_data_out ):
    os.makerdirs( dir_data_out )

file_train_clean_data = 'train_clean.csv'
file_test_clean_data  = 'test_clean.csv'
file_result_output    = 'imdb_movie_review-bag_of_words-random_forest-result.csv'

#%%##############
# Load the data #
#################
# The preprocessed data was saved to a csv file
file = dir_data_out + file_train_clean_data
train_data = pd.read_csv( file )
print(f'Read {file}...')

file = dir_data_out + file_test_clean_data
print(f'Reading in {file}...')
test_data  = pd.read_csv( file )

reviews    = list( train_data['review'] )
sentiments = list( train_data['sentiment'] )

y = np.array( sentiments )

random_seed      = 42
test_split_ratio = 0.2

#%%#################################
# Vectorizing with CountVectorizer #
####################################
vectorizer          = CountVectorizer( analyzer = 'word', max_features=5000 )
train_data_features = vectorizer.fit_transform( reviews )  # x = train_data_features

#%%###################
# Training the Model #
######################
# Split training and testing data
train_input, test_input, train_label, test_label = train_test_split( train_data_features, y, test_size=test_split_ratio, random_state=random_seed )
# x_train, x_eval, y_train, y_eval = train_input, eval_input, train_label, eval_label
# train_input, eval_input, train_label, eval_label = train_input, test_input, train_label, test_label

# Modeling with Random Forest
forest = RandomForestClassifier( n_estimators=100 )
forest.fit( train_input, train_label )

#predicted = lgs.predict( x_eval )
accuracy  = forest.score( test_input, test_label )

print(f'accuracy = {accuracy}')
# accuracy = 0.8596

#%%##################
# Testing the Model #
#####################
test_reviews = test_data['review']  # Better to do list( test_data['review'] )?
ids          = test_data['id']  # Better to do list( test_data['id'] )?

test_data_feature_vect = vectorizer.transform( test_reviews )
predictions            = forest.predict( test_data_feature_vect )
print( predictions )

ids = test_data['id']  # Better to do list( test_data['id'] )?

#%%##################
# Saving the Result #
#####################

# From dictionary to dataframe
# TODO: Do I actually need list()?
result    = {'id': list(ids), 'sentiment': list(predictions) }
result_df = pd.DataFrame( result )

file = dir_data_out + file_result_output
result_df.to_csv( file , index=False, quoting=3)
print(f'Saved to {file}...')
# Saved to ../data/output/imdb_movie_review-bag_of_words-random_forest-result.csv...