# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:10:58 2023

@author: Krishna
"""

import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import nltk
import string
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


#-------------------------------------------------------------------------------------<Loading Model>---|||
tfidf = TfidfVectorizer()

spam_model = pickle.load(open("TrainedModel/trained_model.sav",'rb'))

def check_spam():
    text = "I'm good"
    is_spam = spam_model.predict(tfidf.transform([text]))
    if is_spam == 1:
        print("text is spam")
    else:
        print("text is not spam")
        
check_spam()