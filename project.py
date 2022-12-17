import imdb
import json
from imdb import Cinemagoer
from imdb import IMDb
import pyglet, sys, os, time
from PIL import Image
import urllib.request
from omdb_scrapping import scraping_from_omdb_api
from top50_genre import movies_by_genres
from tv_series_by_genre import tv_series
from person_imdb import person_imdb
from animations import start_animations
from animations import load_animation
from animations import bye_animations
from animations import hi_animations
import emoji
import requests
api_key = "6a4ba2a0"
from graph_structure import graph_implementation


def main():
    hi_animations()
    smiley_emoji = emoji.emojize(":grinning_face_with_big_eyes:")
    wave_hand_emoji = emoji.emojize("\U0001F44B")
    grinning_face = ("\U0001F606")
    user_name = input(f"Hello, my name is Movie Schmmovie. It is a pleasure to meet you. May I ask your name? {smiley_emoji}")
    start_animations()
    load_animation(f"Hello {user_name} Let me get you started {grinning_face}")
    while True:
        user_choice = ["Movie Search", "Search top movies for a genre", "Serach top TV series for a genre", "Movie recommendation on the basis of genre and IMDb rating", "Person search to view their image"]
        idx = 1
        for i in user_choice:
            print(f"{idx}) {i}")
            idx += 1
        user_choice = int(input("What do you want to select from the options above? Enter an option from 1-5: "))
        if user_choice == 1:
            search_top_20_movies()
        elif user_choice == 2:
            movies_by_genres()
        elif user_choice == 3:
            tv_series()
        elif user_choice == 4:
            graph_implementation()
        elif user_choice == 5:
            person_imdb()
        continue_or_not = input("Do you want to continue? Enter yes or no: ")
        if continue_or_not == "yes":
            continue
        else:
            load_animation(f"See you later {user_name}, hope you had a good time {smiley_emoji} See you next time {wave_hand_emoji}")
            bye_animations()
            break

def search_top_20_movies():
    moviesDB = imdb.IMDb()
    movie_name = input("What is the movie/tv series name you want to search? ")
    movies = moviesDB.search_movie(movie_name)
    for idx, movie in enumerate(movies):
        title = movie["title"]
        print(f"{idx}: {title}")
    user_choice = int(input(f"Which movie's details you want to look for? Enter 0-19 integer. "))
    print(f"The details for {movies[user_choice]['title']} are as follows: ")
    print(f"Year: {movies[user_choice]['year']}")
    movie_id = movies[user_choice].getID()
    movie = moviesDB.get_movie(f'{movie_id}')
    genres = ", ".join(movie['genre'])
    print("Genre: ", genres)
    # print(movie)
    print("Rating : ", movie['rating'])
    try:
        print(f"Runtime : {movie['runtimes'][0]} mins")
    except:
        pass
    print("imdbID : ", movie['imdbID'])
    cast_list = []
    for i in range(len(movie['cast'])):
        cast_list.append(movie['cast'][i])
    cast_str = ', '.join(map(str, cast_list))
    print("Cast: ", cast_str)
    try:
        director_list = []
        for i in range(len(movie['director'])):
            director_list.append(movie['cast'][i])
        dir_str = ', '.join(map(str, director_list))
        print("Director: ", dir_str)
    except:
        pass
    print("kind : ", movie['kind'])
    try:
        print("short_Overview: ", movie['plot outline'])
    except:
        pass
    try:
        movie['plot']
        print(f"The summary plot for {movies[user_choice]['title']} is available!")
        plot = input(f"Do you want to review the summary plot for {movies[user_choice]['title']}? Enter yes to continue or no to exit: ")
        if plot == "yes" and movie['plot'] != None:
            try:
                plot_list = []
                for i in range(len(movie['plot'])):
                    plot_list.append(movie['plot'][i])
                plot_str = ', '.join(map(str, plot_list))
                print("Plot: \n", plot_str)
        
            except:
                pass
    except:
        pass

def scraping_from_imdbpy():
    moviesDB = imdb.IMDb()
    top_250_movies = moviesDB.get_top250_movies()
    top_250_movies_dict = {}
    for i in range(5):
        title = top_250_movies[i]['title']
        year = top_250_movies[i]['year']
        rating = top_250_movies[i]['rating']
        kind = top_250_movies[i]['kind']
        top_250_rank = top_250_movies[i]['top 250 rank']
        votes = top_250_movies[i]['votes']
        movie_id = movie_id_from_movie_title(title)
        movie_dict = {'title': title, 
                    'top_250 rank': top_250_rank,
                    'year': year, 
                    'rating': rating, 
                    'votes': votes,
                    'genre': movie_id_to_genre(movie_id),
                    'kind': kind}
        top_250_movies_dict[movie_id] = movie_dict
    with open('output.json', 'w+') as f:
        json.dump(top_250_movies_dict, f, indent = 4)

def movie_id_from_movie_title(title):
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(title)
    movie_id = movies[0].getID()
    print(movie_id)
    return movie_id

def movie_id_to_genre(movie_id):
    ia = Cinemagoer()
    movie = ia.get_movie(movie_id)
    # print(movie['genres'])
    genres = ", ".join(movie['genres'])
    # print(type(genres))
    return genres


if __name__ == '__main__':
    main()
