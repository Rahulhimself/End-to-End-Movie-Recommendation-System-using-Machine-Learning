

import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np # Import numpy for potential NaN handling

# GLOBAL VARIABLE TO HOLD POSTER DATA
poster_df = pd.DataFrame()

def fetch_poster(movie_title):
    """
    Fetches the movie poster URL from the local poster_df DataFrame 
    using the movie title.
    """
    global poster_df
    
    # Check if the DataFrame is loaded and not empty
    if poster_df.empty:
        # Fallback if data isn't loaded
        return "https://placehold.co/500x750/CC0000/FFFFFF?text=Data+Error"
    
    # Find the row corresponding to the movie title
    poster_row = poster_df.query('title == @movie_title')
    
    if not poster_row.empty:
        # Get the poster URL from the found row
        poster_url = poster_row['poster_url'].iloc[0]
        # Return the URL if it's a valid string
        if isinstance(poster_url, str) and poster_url:
            return poster_url
    
    # Return a placeholder if the movie or poster URL is not found
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"


def recommend(movie):
    """
    Retrieves the top 5 recommended movies along with their posters, years, and ratings.
    """
    # 1. Get the index of the input movie
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return [], [], [], []

    # 2. Get the similarity scores and sort them
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_years = []
    recommended_movie_ratings = []
    
    # 3. Iterate through the top 5 recommended movies (skipping the first one, which is the input movie itself)
    for i in distances[1:6]:
        # Get the DataFrame index of the recommended movie
        movie_df_index = i[0]
        
        # Retrieve the title
        movie_title = movies.iloc[movie_df_index]['title']
        recommended_movie_names.append(movie_title)
        
        # Retrieve the poster (using the new local function)
        recommended_movie_posters.append(fetch_poster(movie_title))
        
        # 🌟 Retrieve the year (Assumes a 'year' column exists)
        # We use .get() for safety, defaulting to None if the column is missing
        movie_year = movies.iloc[movie_df_index].get('year', np.nan) 
        # Convert pandas Series object to a single value if necessary
        recommended_movie_years.append(movie_year if not isinstance(movie_year, pd.Series) else movie_year.iloc[0]) 
        
        # 🌟 Retrieve the rating (Assumes a 'vote_average' or 'rating' column exists)
        movie_rating = movies.iloc[movie_df_index].get('vote_average', np.nan) # Change 'vote_average' if your column name is different
        # Convert pandas Series object to a single value if necessary
        recommended_movie_ratings.append(movie_rating if not isinstance(movie_rating, pd.Series) else movie_rating.iloc[0])

    return recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings


st.set_page_config(layout="wide")
st.header('Movie Recommender System Using Machine Learning')

# Load the data files
try:
    movies_dict = pickle.load(open('artifacts/movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    
    # NEW: Load the local poster data and assign to the global variable
    try:
        poster_df = pd.read_csv('artifacts/poster.csv')
    except FileNotFoundError:
        st.warning("Local poster data file 'artifacts/poster.csv' not found. Poster images will fail.")
        # Continue execution, but posters will show 'No Poster'
        
except FileNotFoundError:
    st.error("Model files not found. Please run the data processing notebook first.")
    st.stop()


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Finding recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings = recommend(selected_movie)
    
    if recommended_movie_names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            if i < len(recommended_movie_names): # Safety check
                with col:
                    st.text(recommended_movie_names[i])
                    st.image(recommended_movie_posters[i])
                    
                    # Ensure year is an integer before displaying
                    year = recommended_movie_years[i]
                    if pd.notna(year):
                        # Ensure year is displayable, assuming it's an integer year
                        st.caption(f"Year: {int(year)}") 
                    else:
                        st.caption("Year: N/A")
                        
                    rating = recommended_movie_ratings[i]
                    if pd.notna(rating):
                         st.caption(f"Rating: {rating:.1f} ⭐")
                    else:
                         st.caption("Rating: N/A")