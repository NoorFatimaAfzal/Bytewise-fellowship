import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_data(data):
    #================== Data Cleaning ==================

    # Impute missing values in 'motivation' column with the most frequent value
    imputer1 = SimpleImputer(strategy='most_frequent')
    data['motivation'] = imputer1.fit_transform(data[['motivation']]).ravel()

    # Impute missing values in 'birth_date' column with the most frequent value
    imputer2 = SimpleImputer(strategy='most_frequent')
    data['birth_date'] = imputer2.fit_transform(data[['birth_date']]).ravel()

    # Impute missing values in 'birth_city' column with the most frequent value
    imputer3 = SimpleImputer(strategy='most_frequent')
    data['birth_city'] = imputer3.fit_transform(data[['birth_city']]).ravel()

    # Impute missing values in 'birth_country' column with the most frequent value
    imputer4 = SimpleImputer(strategy='most_frequent')
    data['birth_country'] = imputer4.fit_transform(data[['birth_country']]).ravel()

    # Impute missing values in 'sex' column with the most frequent value
    imputer5 = SimpleImputer(strategy='most_frequent')
    data['sex'] = imputer5.fit_transform(data[['sex']]).ravel()

    # Impute missing values in 'organization_name' column with the most frequent value
    imputer6 = SimpleImputer(strategy='most_frequent')
    data['organization_name'] = imputer6.fit_transform(data[['organization_name']]).ravel()

    # Impute missing values in 'organization_city' column with the most frequent value
    imputer7 = SimpleImputer(strategy='most_frequent')
    data['organization_city'] = imputer7.fit_transform(data[['organization_city']]).ravel()

    # Impute missing values in 'organization_country' column with the most frequent value
    imputer8 = SimpleImputer(strategy='most_frequent')
    data['organization_country'] = imputer8.fit_transform(data[['organization_country']]).ravel()

    # Impute missing values in 'death_date' column with the most frequent value
    imputer9 = SimpleImputer(strategy='most_frequent')
    data['death_date'] = imputer9.fit_transform(data[['death_date']]).ravel()

    # Impute missing values in 'death_city' column with the most frequent value
    imputer10 = SimpleImputer(strategy='most_frequent')
    data['death_city'] = imputer10.fit_transform(data[['death_city']]).ravel()

    # Impute missing values in 'death_country' column with the most frequent value
    imputer11 = SimpleImputer(strategy='most_frequent')
    data['death_country'] = imputer11.fit_transform(data[['death_country']]).ravel()

    return data