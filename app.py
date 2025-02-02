import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

# Load datasets
movies = pd.read_csv("C:/Users/aljau/movie-recommendation-system/data/movies.csv")
ratings = pd.read_csv("C:/Users/aljau/movie-recommendation-system/data/ratings.csv")

# Display dataset structure
print("Movies Data Preview:")
print(movies.head())
print("\nRatings Data Preview:")
print(ratings.head())

# Dataset info
print("\nMovies Dataset Info:")
print(movies.info())
print("\nRatings Dataset Info:")
print(ratings.info())

# Visualizing the distribution of ratings
plt.figure(figsize=(8, 6))
sns.countplot(x="rating", data=ratings, palette="viridis")
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Merge ratings and movies data
data = pd.merge(ratings, movies, on="movieId")

# Create user-item matrix
user_item_matrix = data.pivot_table(
    index="userId", columns="title", values="rating", fill_value=0
)

# Compute user similarity using cosine similarity
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index
)


def recommend_movies_for_user(user_id, n_recommendations=5):
    """
    Recommend movies for a given user based on user similarity.

    Parameters:
    user_id (int): Target user ID
    n_recommendations (int): Number of recommendations to return

    Returns:
    List of recommended movie titles
    """
    if user_id not in user_similarity_df.index:
        return "User ID not found in dataset."

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:6]
    similar_user_ratings = user_item_matrix.loc[similar_users.index]
    recommended_movies = similar_user_ratings.mean(axis=0).sort_values(ascending=False)
    return recommended_movies.head(n_recommendations)


# Example: Get recommendations for user ID 1
print("Recommended Movies for User 1:")
print(recommend_movies_for_user(1))

# Content-Based Filtering using TF-IDF on genres
movies["genres"] = movies["genres"].fillna("")
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Compute cosine similarity between movies
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


def recommend_movies_by_title(title, n_recommendations=5):
    """
    Recommend movies based on content similarity using genre metadata.

    Parameters:
    title (str): Target movie title
    n_recommendations (int): Number of recommendations to return

    Returns:
    List of recommended movie titles
    """
    if title not in movies["title"].values:
        return "Movie title not found in dataset."

    idx = movies[movies["title"] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[
        1 : n_recommendations + 1
    ]
    movie_indices = [i[0] for i in sim_scores]
    return movies["title"].iloc[movie_indices]


# Example: Get recommendations for a specific movie
target_movie = "Toy Story (1995)"
print(f"\nMovies similar to '{target_movie}':")
print(recommend_movies_by_title(target_movie))
