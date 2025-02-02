# Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24%2B-green)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-red)

A movie recommendation system built using collaborative filtering and content-based filtering techniques. This project demonstrates how to recommend movies to users based on their preferences and movie genres.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
  - [Collaborative Filtering](#collaborative-filtering)
  - [Content-Based Filtering](#content-based-filtering)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project implements two types of recommendation systems:
1. **Collaborative Filtering**: Recommends movies based on user similarity and ratings.
2. **Content-Based Filtering**: Recommends movies based on genre similarity.

The system uses the MovieLens dataset, which contains movie ratings and metadata.

---

## Features

- **User-Based Recommendations**: Recommends movies to a user based on the preferences of similar users.
- **Genre-Based Recommendations**: Recommends movies similar to a given movie based on genre.
- **Data Visualization**: Visualizes the distribution of movie ratings using Seaborn and Matplotlib.

---

## Dataset

The dataset used in this project is the [MovieLens dataset](https://grouplens.org/datasets/movielens/), which includes:
- **movies.csv**: Contains movie titles and genres.
- **ratings.csv**: Contains user ratings for movies.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the MovieLens dataset and place the `movies.csv` and `ratings.csv` files in the `data/` directory.

---

## Usage

1. **Collaborative Filtering**:
   - To recommend movies for a specific user (e.g., user ID 1):
     ```python
     print(recommend_movie(1))
     ```

2. **Content-Based Filtering**:
   - To recommend movies similar to a given movie (e.g., "Toy Story (1995)"):
     ```python
     print(recommend_movies_by_title("Toy Story (1995)"))
     ```

3. **Visualization**:
   - To visualize the distribution of movie ratings:
     ```python
     plt.figure(figsize=(8, 6))
     sns.countplot(x="rating", data=ratings, palette="viridis")
     plt.title("Distribution of Movie Ratings")
     plt.xlabel("Rating")
     plt.ylabel("Count")
     plt.show()
     ```

---

## Methods

### Collaborative Filtering
- **User-Item Matrix**: A pivot table is created to map users to movies and their ratings.
- **Cosine Similarity**: Used to calculate similarity between users based on their ratings.
- **Recommendation**: Movies are recommended based on the average ratings of similar users.

### Content-Based Filtering
- **TF-IDF Vectorization**: Converts movie genres into a numerical representation.
- **Cosine Similarity**: Used to calculate similarity between movies based on their genres.
- **Recommendation**: Movies are recommended based on genre similarity.

---

## Results

- **Collaborative Filtering**: Provides personalized recommendations for users.
- **Content-Based Filtering**: Recommends movies with similar genres to a given movie.
- **Visualization**: Insights into the distribution of movie ratings.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/) for providing the data.
- [Scikit-learn](https://scikit-learn.org/) and [Pandas](https://pandas.pydata.org/) for making data analysis and machine learning easier.

---
