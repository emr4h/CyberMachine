import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer


def machineLearnSpam(message):

    dataSet = pd.read_csv('../CyberMachine/spam.csv')
    dataSet.Category = dataSet.Category.apply(lambda x: 1 if x == 'spam' else 0)
    features = dataSet.iloc[:,1] 
    ifSpam = dataSet.iloc[:,0] 
    cv = CountVectorizer()
    features = cv.fit_transform(features)
    userInput = cv.transform([message])
    print("The model is training using a total of 5572 data...\n")

    print("Prediction using Decision Trees ...")

    dtModel = tree.DecisionTreeClassifier() 
    dtModel.fit(features, ifSpam)
    dtPredict = dtModel.predict(userInput)
    print(dtPredict) 
    print("\n")

    print("Prediction using Random Forest ...")

    rfModel = RandomForestClassifier() 
    rfModel.fit(features, ifSpam) 
    rfPredict = rfModel.predict(userInput)
    print(rfPredict)
    print("\n")


    print("Prediction using Support Vector Machine ...")

    svcModel = svm.SVC()
    svcModel.fit(features, ifSpam)
    svcPredict = svcModel.predict(userInput)
    print(svcPredict)
    print("\n")

    predict = int(svcPredict + dtPredict + rfPredict)
    return predict

