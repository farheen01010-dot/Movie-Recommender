from recommender import recommend

movies = recommend("Toy Story")

for movie in movies:
    print(movie)