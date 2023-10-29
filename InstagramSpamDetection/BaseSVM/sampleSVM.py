# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:52:53 2023

@author: Krishna
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import pickle


# Train the classification model
def train_model():
    df = pd.read_json('intent_data.json')

    X_train, X_test, y_train, y_test = train_test_split(df['Utterance'], df['Intent'], random_state=0)

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    model = LinearSVC().fit(X_train_tfidf, y_train)

    # Save the vectorizer
    vec_file = 'vectorizer.pickle'
    pickle.dump(count_vect, open(vec_file, 'wb'))

    # Save the model
    mod_file = 'classification.model'
    pickle.dump(model, open(mod_file, 'wb'))


# Load the classification model from disk and use for predictions
def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

    # load the model
    loaded_model = pickle.load(open('classification.model', 'rb'))

    # make a prediction
    print(loaded_model.predict(loaded_vectorizer.transform([utt])))