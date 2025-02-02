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
- [License](#LICENSE)

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
