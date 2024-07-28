import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import preprocessing

netflix_movies = pd.read_csv(r'C:\Users\InfoBay\OneDrive\Desktop\task-1\netflix_data.csv')

netflix_movies = preprocessing.preprocess_data(netflix_movies)

# Sidebar options
st.sidebar.title('Netflix Movies Analysis')
user_option = st.sidebar.radio('Select an Option', ('Movies less than 60 minutes', 'Movie Duration Scatter Plot', 'Genre Analysis', 'Country Analysis', 'Type of Movies'))

# ====================== 1st option ======================

# Option 1: Movies less than 60 minutes
if user_option == 'Movies less than 60 minutes':
    st.header('Movies less than 60 minutes')
    short_movies = netflix_movies[netflix_movies['duration'] < 60]
    st.dataframe(short_movies)

# ====================== 2nd option ======================

# Option 2: Movie Duration Scatter Plot
if user_option == 'Movie Duration Scatter Plot':
    st.header('Movie Duration by Year of Release')

    # Create a list to hold the colors
    colors = []

    # Define the genre groups and their corresponding colors
    genre_colors = {
        "Children": "blue",
        "Documentaries": "green",
        "Stand-Up": "red"
    }

    # Iterate through the rows of netflix_movies and assign colors based on genre
    for genre in netflix_movies['genre']:
        if "Children" in genre:
            colors.append(genre_colors["Children"])
        elif "Documentaries" in genre:
            colors.append(genre_colors["Documentaries"])
        elif "Stand-Up" in genre:
            colors.append(genre_colors["Stand-Up"])
        else:
            colors.append("yellow")  # Assign yellow for 'Other' genres

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
    ax.set_xlabel("Release year")
    ax.set_ylabel("Duration (min)")
    ax.set_title("Movie Duration by Year of Release")

    st.pyplot(fig)


# ====================== 3rd option ======================

# Option 3: Genre Analysis
if user_option == 'Genre Analysis':
    st.header('Movies by Genre')
    
    # Get unique genres
    genres = netflix_movies['genre'].dropna().unique().tolist()
    genres.sort()
    genres.insert(0, 'All')  # Option to show all genres
    
    selected_genre = st.selectbox('Select Genre', genres)
    
    if selected_genre == 'All':
        # Show all movies
        st.write(netflix_movies[['title', 'genre', 'description']])
    else:
        # Filter by selected genre
        filtered_movies = netflix_movies[netflix_movies['genre'] == selected_genre]
        st.write(filtered_movies[['title', 'description']])



# ====================== 4th option ======================

# Option 4: Country Analysis
if user_option == 'Country Analysis':
    st.header('Movies by Country')
    
    # Get unique countries
    countries = netflix_movies['country'].dropna().unique().tolist()
    countries.sort()
    countries.insert(0, 'All')  # Option to show all countries
    
    selected_country = st.selectbox('Select Country', countries)
    
    if selected_country == 'All':
        # Show all movies
        st.write(netflix_movies[['title', 'country', 'description']])
    else:
        # Filter by selected country
        filtered_movies = netflix_movies[netflix_movies['country'] == selected_country]
        st.write(filtered_movies[['title', 'description']])


# ====================== 5th option ======================

# Option 5: Type of Movies
if user_option == 'Type of Movies':
    st.header('Type of Movies')
    
    # Get unique types
    types = netflix_movies['type'].dropna().unique().tolist()
    types.sort()
    types.insert(0, 'All')  # Option to show all types

    selected_type = st.selectbox('Select Type', types)

    if selected_type == 'All':
        # Show all movies
        st.write(netflix_movies[['title', 'type', 'description']])
    else:
        # Filter by selected type
        filtered_movies = netflix_movies[netflix_movies['type'] == selected_type]
        st.write(filtered_movies[['title', 'description']])

        