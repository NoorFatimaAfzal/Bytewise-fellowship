import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_data(data):
    # imputing missing values in 'Year' column with the most frequent value
    imputer = SimpleImputer(strategy='most_frequent')
    data['Year'] = imputer.fit_transform(data[['Year']]).ravel()

    # imputing missing values in 'Population' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Population'] = imputer.fit_transform(data[['Population']]).ravel()

    # imputing missing values in 'Murder' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Murder'] = imputer.fit_transform(data[['Murder']]).ravel()

    # imputing missing values in 'Rape' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Rape'] = imputer.fit_transform(data[['Rape']]).ravel()

    # imputing missing values in 'Robbery' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Robbery'] = imputer.fit_transform(data[['Robbery']]).ravel()    

    # imputing missing values in 'Assault' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Assault'] = imputer.fit_transform(data[['Assault']]).ravel()

    # imputing missing values in 'Burglary' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['Burglary'] = imputer.fit_transform(data[['Burglary']]).ravel()

    # imputing missing values in 'CarTheft' column with the mean value
    imputer = SimpleImputer(strategy='mean')
    data['CarTheft'] = imputer.fit_transform(data[['CarTheft']]).ravel()

    return data