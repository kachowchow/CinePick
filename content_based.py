import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets 
movies = pd.read_csv('data/movies.csv') 

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
            
# Recommendation Function
def recommend_movies(movie_title, num_recommendatiions=5):
      if movie_title not in movies['title'].values:
            print ("Movie not found in the database.")
            return []
      
      movie_index = movies[movies['title'] == movie_title].index[0]
      sim_scores = cosine_similarity(genre_vectors.iloc[[movie_index]], genre_vectors)[0]
      top_movies = sim_scores.argsort()[::-1][1:num_recommendatiions+1]
      return movies['title'].iloc[top_movies].tolist()

# Search Function
def search_movies(keyword, max_results = 25):
      matches = movies[movies['title'].str.contains(keyword, case=False, regex=False)]
      if matches.empty:
            print("No matches found.")
            return
      else:
            print(f"\nFound {len(matches)} matches: ")
            for i, title in enumerate(matches['title'].head(max_results), 1):
                  print(f"{i}. {title}")

# User Interation Function
def run_recommender():
      print("Welcome to CinePick!")
      print("Type the movie title to search for it.")
      print("Type 'exit' to quit the program.")

      while True:
            user_input = input("\nEnter a movie title or keyword or 'exit': ")
            if user_input.lower() == 'exit':
                  print("Thank you for using CinePick. Goodbye!")
                  break
            elif len(user_input) < 2:
                  print("Please enter at least 2 characters.")
                  continue

            search_movies(user_input)
            exact_title = input("\nEnter the exact movie title for recommendations: ")

            recommendations = recommend_movies(exact_title)
            if len(recommendations) > 0:
                  print(f"\nBecause you liked '{exact_title}', you might also like:")
                  for i, r in enumerate(recommendations, 1):
                        print(f"{i}. {r}")
            print()

# Run the recommender system
if __name__ == "__main__":
      run_recommender()