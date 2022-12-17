from project import movie_id_from_movie_title
from project import movie_id_to_genre
import imdb
import json

def scraping_from_imdbpy():
    moviesDB = imdb.IMDb()
    movie = moviesDB.get_movie()
    movie_dict = {}
    for i in range(len(movie)):
        title = movie[i]['title']
        year = movie[i]['year']
        rating = movie[i]['rating']
        kind = movie[i]['kind']
        top_250_rank = movie[i]['top 250 rank']
        votes = movie[i]['votes']
        movie_id = movie_id_from_movie_title(title)
        movie_dict = {'title': title, 
                    'top_250 rank': top_250_rank,
                    'year': year, 
                    'rating': rating, 
                    'votes': votes,
                    'genre': movie_id_to_genre(movie_id),
                    'kind': kind}
        movie_dict[movie_id] = movie_dict
    with open('movies_cache.json', 'w+') as f:
        json.dump(movie_dict, f, indent = 4)