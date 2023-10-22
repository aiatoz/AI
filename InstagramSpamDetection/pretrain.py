# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:42:23 2023

@author: Krishna
"""

#-------------------------------------------------------------------------------------<Libraries>---|||
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
 
ps = PorterStemmer()



#-------------------------------------------------------------------------------------<Data Cleanup>---|||

#DataSet loader, from Kaggle(5574 msgs) https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/ 
#Changed headers manually to Label, Content
df = pd.read_csv('Dataset/Kaggle/spam.csv',encoding = "ISO-8859-1")#Print here to check

encoder = LabelEncoder()
df['Label'] = encoder.fit_transform(df['Label'])

df = df.drop_duplicates(keep='first')#Removes the duplicate entries 

#Tokenizer
def getTokens(word):
    word = word.lower()
    returnList = []
    
    word = nltk.word_tokenize(word)
    for i in word:
        if i.isalnum():
            returnList.append(i)
    return returnList

#StopWords Remover
def removeStopWords(word):
    returnList = []
    for i in word:
        if i not in nltk.corpus.stopwords.words('english') and i not in string.punctuation:
            returnList.append(i)
    return returnList

#Stem words removeer, eg : walk, walked etc.
def doStem(word):
    returnList = []
    for i in word:
        returnList.append(ps.stem(i))
    return " ".join(returnList)

#Calling functions
df['tokens'] = df['Content'].apply(getTokens)
df['tokens'] = df['tokens'].apply(removeStopWords)
df['tokens'] = df['tokens'].apply(doStem)



#-------------------------------------------------------------------------------------<Data Split>---|||
from sklearn.model_selection import train_test_split
X = df['tokens']
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)



#-------------------------------------------------------------------------------------<Data Training>---|||
tfidf = TfidfVectorizer()
feature = tfidf.fit_transform(X_train)
 
tuned_parameters = {'kernel':['linear','rbf'],'gamma':[1e-3,1e-4], 'C':[1,10,100,1000]}
 
model = GridSearchCV(svm.SVC(),tuned_parameters)
model.fit(feature, y_train)



#-------------------------------------------------------------------------------------<Model Accuracy>---|||
from sklearn import metrics

y_pred = model.predict(tfidf.transform(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)



#-------------------------------------------------------------------------------------<Saving Model>---|||
import pickle
filename = 'TrainedModel/trained_model.sav'
pickle.dump(model, open(filename, 'wb'))




#-------------------------------------------------------------------------------------<Loading Model>---|||
'''spam_model = pickle.load(open("TrainedModel/trained_model.sav",'rb'))

def check_spam():
    text = "I'm good"
    is_spam = spam_model.predict(tfidf.transform([text]))
    if is_spam == 1:
        print("text is spam")
    else:
        print("text is not spam")
        
check_spam()
'''
