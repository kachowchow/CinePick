import pandas as pd 

# Load datasets 
movies = pd.read_csv('data/movies.csv') 
ratings = pd.read_csv('data/ratings.csv') 

# Remove entries with 'no genres listed' 
movies = movies[movies['genres'] != '(no genres listed)'] 
movies.reset_index(drop=True, inplace=True) 

# Extract all unique genres 
allgenres = set() 

for genre_list in movies['genres']: 
      genres = genre_list.split('|') 
      allgenres.update(genres) 
      
allgenres = list(allgenres) 

# Create binary vectors for genres 
genre_vectors = pd.DataFrame(0, index=movies.index, columns=allgenres) 

for i, genre_list in enumerate(movies['genres']): 
      genres = genre_list.split('|') 
      for genre in genres: 
            genre_vectors.at[i, genre] = 1 
            
# Combine movie titles with their genre vectors 
vectored_movies = pd.concat([movies[['title']], genre_vectors], axis=1) 

print(vectored_movies.shape())