import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("data/movies.csv")
movies["genres"] = movies["genres"].fillna("")
movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)
vectorizer = TfidfVectorizer(stop_words="english")

vectors = vectorizer.fit_transform(movies["genres"])
similarity = cosine_similarity(vectors)
def recommend(movie_name):

    matched_movies = movies[
        movies["title"].str.contains(movie_name, case=False, na=False)
    ]

    if matched_movies.empty:
        return []

    movie_index = matched_movies.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations