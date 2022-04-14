import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier


def machineLearnUrl(userInput):

    url = pd.read_csv('../CyberMachine/url_spam_classification.csv')

    url['is_spam'] = url.is_spam.apply(str)
    url['is_spam'] = url['is_spam'].apply(lambda x : 1 if x == "True" in x else 0)

    urls = url.iloc[:,0]
    ifSpam = url.iloc[:,1]

    def extractUrl(data):
        url = str(data)
        extractSlash = url.split('/')
        result = []
        
        for i in extractSlash:
            extractDash = str(i).split('-')
            dotExtract = []
            
            for j in range(0,len(extractDash)):
                extractDot = str(extractDash[j]).split('.')
                dotExtract += extractDot
                
            result += extractDash + dotExtract
        result = list(set(result))

        return result

    cv = CountVectorizer(tokenizer=extractUrl)

    print("The model is training using a total of 148303 url data ...\n")

    features = cv.fit_transform(urls)
    features_test = cv.transform([userInput])

    print("Prediction using Stochastic Gradient Descent ...")

    sgdcModel = SGDClassifier()
    sgdcModel.fit(features, ifSpam)
    sgdcPredict = sgdcModel.predict(features_test)
    print(sgdcPredict) 
    print("\n")

    print("Prediction using Decision Trees ...")

    nbModel = MultinomialNB()
    nbModel.fit(features, ifSpam)
    nbPredict = nbModel.predict(features_test)
    print(nbPredict) 
    print("\n")

    print("Prediction using Linear Support Vector Machine ...")

    lsvcModel = LinearSVC()
    lsvcModel.fit(features, ifSpam)
    lsvcPredict = lsvcModel.predict(features_test)
    print(lsvcPredict) 
    print("\n")

    predict = int(lsvcPredict + nbPredict + sgdcPredict)
    return predict

