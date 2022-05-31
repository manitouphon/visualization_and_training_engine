# Import pandas library
import os.path  #for checking files' and paths
import pandas as pd #pandas for dealing with CSV
import numpy as np  #Numpy for dealing with np array
import pickle as pk #Dumping Learning model as binary 
from tabulate import tabulate

import texthero as hero #text cleaning
from sklearn.feature_extraction.text import CountVectorizer #Bags of word vectorizer
from sklearn.utils import shuffle #shuffle dataset
from sklearn.naive_bayes import MultinomialNB 
from sklearn.tree import DecisionTreeClassifier 


from sklearn.model_selection import train_test_split
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

# Class

class TrainerEngine:
    def getTrainedDF(self, dataFrame = pd.DataFrame):
        df = pd.read_csv(
            'https://raw.githubusercontent.com/manitouphon/huff-post-csv-news-category-dataset/main/simplified_data.csv',
            sep=',',
            usecols=["category", "headline"],
            )
        #Testing Data
        # target_df = pd.read_csv(
        #     'https://raw.githubusercontent.com/manitouphon/FaceMine-backend/main/PPPostFBScrape.csv',
        #     sep=',',
        #     usecols=["TITLE"],
        #     )
        target_df = dataFrame
        target_df["TITLE"] = target_df["message"]
        target_df.pop("message")



        df["headline"] = hero.clean(df["headline"])
        df["headline"] = hero.clean(df["headline"])
        headlineArr = df["headline"].array
        df = shuffle(df)
        df = shuffle(df)

        x = np.array(df["headline"])
        y = np.array(df["category"])


        count_vec = CountVectorizer()
        x = count_vec.fit_transform(x)

    
        nb_model = MultinomialNB()
        nb_model.fit(x,y)
        loaded_model = nb_model
        # Dump Model to a file after training 
        # pk.dump(nb_model, open("nb_model.sav", "wb"))  
        
        target_df["CLEANED"] = hero.clean( target_df["TITLE"])  #init CLEAN column
        title = target_df["CLEANED"].tolist()
        cat = [None] * len(title)  #init list with size = len(df[title])



        trained = pd.DataFrame(columns=["title","category"])
        for x in range ( len(title) ):
            if (title[x].lower() == "none"):
                cat[x] = "NONE"
                continue
            data = count_vec.transform([title[x]]).toarray()
            cat[x] = loaded_model.predict(data)[0]
        target_df["CATEGORY"] = cat
        target_df.pop("CLEANED")
        self.__trainedDF = target_df
        return target_df

    def getDF(self):
        return self.__trainedDF
    def displayDF(self):
        print(tabulate(self.__trainedDF, headers = 'keys', tablefmt = 'psql'))
    def exportCSV(self):
        self.__trainedDF.to_csv('trained.csv', index=False)