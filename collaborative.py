import pandas as pd 

# Load datasets 
movies = pd.read_csv('data/movies.csv') 
ratings = pd.read_csv('data/ratings.csv') 

# Remove entries with 'no genres listed' 
movies = movies[movies['genres'] != '(no genres listed)']
movies.reset_index(drop=True, inplace=True) 
