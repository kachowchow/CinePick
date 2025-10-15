# CinePick
a recommender system that suggests movies to users based on data such as ratings, genres, or similarity

# Demo Steps
1. Download the Following link to access the Dataset:
  https://files.grouplens.org/datasets/movielens/ml-32m.zip
2. Extract the dataset and place the movies.csv and ratings.csv files in a data/ folder in your project directory.
3. Make sure you have Python 3 installed.
4. Install required libraries:
  pip install pandas scikit-learn
5. Run the content-based recommender:
  python content_based.py
6. Follow the on-screen instructions to search for a movie and get recommendations.
7. Type exit to quit the program.

# Files
content_based.py - uses Movie genres to recommend similar movies 
collaborative.py - uses Movie ratings to recommend movies using collaborative filtering
data/ - Contains the dataset files: movies.csv, ratings.csv

Last Update: 10/11/2025
