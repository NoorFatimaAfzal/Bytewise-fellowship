import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_data(data):

    #================== Data Cleaning ==================

    ## Ravel() function convert the 2D array to 1D array 

    # Impute missing values in 'country' column
    imputer1 = SimpleImputer(strategy='most_frequent')
    data['country'] = imputer1.fit_transform(data[['country']]).ravel()

    # Impute missing values in 'director' column
    imputer2 = SimpleImputer(strategy='most_frequent')
    data['director'] = imputer2.fit_transform(data[['director']]).ravel()

    # Impute missing values in 'cast' column
    imputer3 = SimpleImputer(strategy='most_frequent')
    data['cast'] = imputer3.fit_transform(data[['cast']]).ravel()

    return data