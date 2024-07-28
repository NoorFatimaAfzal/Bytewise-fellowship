import streamlit as st
import pandas as pd

import preprocessing

# Load the dataset
def load_data():
    data = pd.read_csv(r'C:\Users\InfoBay\OneDrive\Desktop\task-1\Bytewise-fellowship\Task-2\nobel.csv')
    return data

data = load_data()

data = preprocessing.preprocess_data(data)

# Title of the app
st.title("Nobel Prize Data Analysis")

# Sidebar menu for selection
option = st.sidebar.radio(
    'Select Analysis',
    ('Top Gender Winner', 'Top Country Winner', 'Top Category Winner', 'Top 10 Winners', 'Top 10 Birth Countries', 'Each category winner', 'first woman nobel prize winner', 'Woman analysis through graphs')
)

#================== option 1 ==================


if option == 'Top Gender Winner':
    top_gender = data['sex'].value_counts().index[0]
    top_gender_count = data['sex'].value_counts().iloc[0]
    st.subheader("Top Gender Winner")
    st.write(f"The most commonly awarded gender is **{top_gender}** with **{top_gender_count}** awards.")
    st.subheader("Gender Distribution")
    gender_counts = data['sex'].value_counts()
    st.bar_chart(gender_counts)


#================== option 2 ==================


if option == 'Top Country Winner':
    top_country = data['birth_country'].value_counts().index[0]
    top_country_count = data['birth_country'].value_counts().iloc[0]
    st.subheader("Top Country Winner")
    st.write(f"The most commonly awarded birth country is **{top_country}** with **{top_country_count}** awards.")
    st.subheader("Top 10 Birth Countries Distribution")
    birth_country_counts = data['birth_country'].value_counts().head(10)
    st.bar_chart(birth_country_counts)


#================== option 3 ==================


if option == 'Top Category Winner':
    top_category = data['category'].value_counts().index[0]
    top_category_count = data['category'].value_counts().iloc[0]
    st.subheader("Top Category Winner")
    st.write(f"The most commonly awarded category is **{top_category}** with **{top_category_count}** awards.")
    st.subheader("Category Distribution")
    category_counts = data['category'].value_counts()
    st.bar_chart(category_counts)


#================== option 4 ==================


if option == 'Top 10 Winners':
    top_10_winners = data['full_name'].value_counts().head(10)
    st.subheader("Top 10 Winners")
    st.write(top_10_winners)
    st.subheader("Top 10 Winners Distribution")
    top_10_winners_counts = data['full_name'].value_counts().head(10)
    st.bar_chart(top_10_winners_counts)


#================== option 5 ==================


if option == 'Top 10 Birth Countries':
    top_10_birth_countries = data['birth_country'].value_counts().head(10)
    st.subheader("Top 10 Birth Countries")
    st.write(top_10_birth_countries)
    st.subheader("Top 10 Birth Countries Distribution")
    top_10_birth_countries_counts = data['birth_country'].value_counts().head(10)
    st.bar_chart(top_10_birth_countries_counts)


#================== option 6 ==================


if option == 'Each category winner':
    st.subheader("Each Category Winner")
    category = st.selectbox('Select Category', data['category'].unique())
    selected_category = data[data['category'] == category]
    st.write(selected_category['full_name'].value_counts())


#================== option 7 ==================

if option == 'first woman nobel prize winner':
    data['female_winner'] = data['sex'] == 'Female'
    nobel_women = data[data['female_winner']]
    min_row = nobel_women[nobel_women['year'] == nobel_women['year'].min()]
    first_woman_name = min_row['full_name'].values[0]
    first_woman_category = min_row['category'].values[0]
    
    st.subheader('First Woman Nobel Prize Winner')
    st.write(f"{first_woman_name} in category {first_woman_category}")


#================== option 8 ==================

if option == 'Woman analysis through graphs':
    st.subheader('Analysis of Nobel Prize Winners by Women')
    women_count_per_year = data[data['sex'] == 'Female'].groupby('year').size()
    st.line_chart(women_count_per_year)
    st.subheader('Breakdown by Category')
    category_counts = data[data['sex'] == 'Female']['category'].value_counts()
    st.bar_chart(category_counts)
    st.subheader('Breakdown by Birth Country')
    birth_country_counts = data[data['sex'] == 'Female']['birth_country'].value_counts().head(10)
    st.bar_chart(birth_country_counts)
    st.subheader('Breakdown by Birth City')
    birth_city_counts = data[data['sex'] == 'Female']['birth_city'].value_counts().head(10)
    st.bar_chart(birth_city_counts)

