# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:10:58 2023

@author: carla
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import pickle

# Load the classification model from disk and use for predictions
def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = pickle.load(open('TrainedModel/trained_vectorizer.pickle', 'rb'))

    # load the model
    loaded_model = pickle.load(open('TrainedModel/trained_model.model', 'rb'))

    # make a prediction
    print(loaded_model.predict(loaded_vectorizer.transform([utt])))
    
    
classify_utterance("URGENT! Your Mobile No. was awarded å£2000 try to contact U! Call from Landline 09064019788 BOX42WR29C, 150PPM")