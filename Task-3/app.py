import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns

import preprocessing

data = pd.read_csv(r'C:\Users\InfoBay\OneDrive\Desktop\Data_science\Bytewise-fellowship\Task-3\data\crime.csv')

data = preprocessing.preprocess_data(data)

# Sidebar options
st.sidebar.title('Crime Analysis')
user_option = st.sidebar.radio('Select an Option', ('Data Analysis', 'Data Visualization', 'Exploratory data analysis', 'Top Crime each year'))

#==================== option 1 =====================


if user_option == 'Data Analysis':
    st.title('Data Analysis')
    st.subheader('Data Preview')
    st.write(data.head())
    st.subheader('Data Description')    
    st.write(data.describe())

    st.subheader('Data Information')
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.subheader('Data Shape')
    st.write(data.shape)
    st.subheader('Data Columns')
    st.write(data.columns)
    st.subheader('Data Types')
    st.write(data.dtypes)
    st.subheader('Missing Values')
    st.write(data.isnull().sum())
    st.subheader('Unique Values')
    st.write(data.nunique())


#==================== option 2 =====================

if user_option == 'Data Visualization':
    st.title('Data Visualization')
    st.subheader('Crimes Trend Analysis Per Year')
    
    # Multiple Crime Trends
    selected_crimes = st.multiselect('Select Crimes', data.columns[2:], default=['Murder'])
    fig, ax = plt.subplots(figsize=(14, 8))
    for crime in selected_crimes:
        ax.plot(data['Year'], data[crime], marker='o', label=crime)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Crimes')
    ax.set_title('Crime Trends Over the Years')
    ax.set_xticks(data['Year'])
    ax.set_xticklabels(data['Year'], rotation=45)
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Crime Distribution for a Specific Year
    st.subheader('Crime Distribution in a Specific Year')
    selected_year = st.selectbox('Select a Year', data['Year'].unique())
    crime_data_year = data[data['Year'] == selected_year].iloc[:, 2:].sum()
    fig, ax = plt.subplots()
    ax.bar(crime_data_year.index, crime_data_year.values)
    ax.set_xlabel('Crime Type')
    ax.set_ylabel('Number of Crimes')
    ax.set_title(f'Crime Distribution in {selected_year}')
    st.pyplot(fig)
    
    # Heatmap of Crime Rates
    st.subheader('Heatmap of Crime Rates')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(data.iloc[:, 2:].transpose(), cmap="YlGnBu", ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Crime Type')
    ax.set_title('Heatmap of Crime Rates Over the Years')
    ax.set_xticks(range(len(data['Year'])))
    ax.set_xticklabels(data['Year'], rotation=45)
    st.pyplot(fig)

    # Box Plot for Crime Distributions
    st.subheader('Box Plot for Crime Distributions')
    selected_crime_box = st.selectbox('Select Crime for Box Plot', data.columns[2:])
    fig, ax = plt.subplots()
    sns.boxplot(x=data[selected_crime_box], ax=ax)
    ax.set_xlabel('Number of Crimes')
    ax.set_title(f'Box Plot of {selected_crime_box}')
    st.pyplot(fig)

    # distribution of crimes
    st.subheader('Distribution of Crimes')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.kdeplot(data[selected_crime_box], ax=ax, fill=True)
    ax.set_xlabel('Number of Crimes')
    ax.set_ylabel('Density')
    ax.set_title(f'Distribution of {selected_crime_box}')
    st.pyplot(fig)


#==================== option 3 =====================

if user_option == 'Exploratory data analysis':
    st.title('Exploratory Data Analysis')
    st.subheader('Correlation Analysis')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(data.iloc[:, 2:].corr(), cmap="YlGnBu", ax=ax, annot=True)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    st.subheader('Pairplot')
    fig = sns.pairplot(data.iloc[:, 2:])
    st.pyplot(fig)

    st.subheader('Distribution of Crimes')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.kdeplot(data.iloc[:, 2:], ax=ax, fill=True)
    ax.set_xlabel('Number of Crimes')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of Crimes')
    st.pyplot(fig)

    st.subheader('Violin Plot')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.violinplot(data=data.iloc[:, 2:], ax=ax)
    ax.set_xlabel('Crime Type')
    ax.set_ylabel('Number of Crimes')
    ax.set_title('Violin Plot of Crimes')
    st.pyplot(fig)

    st.subheader('Box Plot')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=data.iloc[:, 2:], ax=ax)
    ax.set_xlabel('Crime Type')
    ax.set_ylabel('Number of Crimes')
    ax.set_title('Box Plot of Crimes')
    st.pyplot(fig)

    st.subheader('Histogram')
    fig, ax = plt.subplots(figsize=(12, 6))
    data.iloc[:, 2:].hist(ax=ax)
    ax.set_xlabel('Number of Crimes')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Crimes')
    st.pyplot(fig)
    

#==================== option 4 =====================

if user_option == 'Top Crime each year':
    st.title('Top Crime each year')
    top_crime = data.iloc[:, 2:].idxmax(axis=1)
    data['Top Crime'] = top_crime
    st.write(data[['Year', 'Top Crime']])