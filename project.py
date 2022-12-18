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
    print(f"\033[7;1mHello, my name is Movie Schmmovie. It is a pleasure to meet you. May I ask your name? {smiley_emoji}\033[0m", end='\n\n')
    user_name = input(f"Enter your name: " )
    start_animations()
    load_animation(f"Hello {user_name} Let me get you started {grinning_face}")
    while True:
        user_choice = ["Movie Search", "Search top movies for a genre", "Serach top TV series for a genre", "Movie recommendation on the basis of genre and IMDb rating", "Person search to view their image"]
        idx = 1
        for i in user_choice:
            print(f"{idx}) {i}")
            idx += 1
        print(f"\033[7;1mWhat do you want to select from the options above? Choose an option from 1-5: \033[0m", end='\n\n')
        user_choice = int(input("Enter an option from 1-5: "))
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
        print(f"\033[7;1mDo you want to continue? \033[0m", end='\n\n')
        continue_or_not = input("Enter yes or no: ")
        if continue_or_not == "yes":
            continue
        else:
            load_animation(f"See you later {user_name}, hope you had a good time {smiley_emoji} See you next time {wave_hand_emoji}")
            bye_animations()
            break

def search_top_20_movies():
    moviesDB = imdb.IMDb()
    print(f"\033[7;1mWhat is the movie/tv series name you want to search? \033[0m", end='\n\n')
    movie_name = input("Enter a name for the movie/tv search: ")
    movies = moviesDB.search_movie(movie_name)
    for idx, movie in enumerate(movies):
        title = movie["title"]
        print(f"{idx}: {title}")
    print(f"\033[7;1mWhich movie's details you want to look for? \033[0m", end='\n\n')
    user_choice = int(input(f"Enter an integer in the range of 0-19 integer. "))
    print(f"\033[7;1mThe details for {movies[user_choice]['title']} are as follows: \033[0m", end='\n\n')
    print(f"\033[7;1mYear\033[0m: {movies[user_choice]['year']}", end='\n\n')
    movie_id = movies[user_choice].getID()
    movie = moviesDB.get_movie(f'{movie_id}')
    genres = ", ".join(movie['genre'])
    print(f"\033[7;1mGenre\033[0m: {genres}", end='\n\n')
    print(f"\033[7;1mRating\033[0m: {movie['rating']}", end='\n\n')
    try:
        print(f"\033[7;1mRuntime\033[0m: {movie['runtimes'][0]} mins", end='\n\n')
    except:
        pass
    print(f"\033[7;1mimdbID\033[0m: {movie['imdbID']}", end='\n\n')
    cast_list = []
    for i in range(len(movie['cast'])):
        cast_list.append(movie['cast'][i])
    cast_str = ', '.join(map(str, cast_list))
    print(f"\033[7;1mCast\033[0m: {cast_str}", end='\n\n')
    try:
        director_list = []
        for i in range(len(movie['director'])):
            director_list.append(movie['cast'][i])
        dir_str = ', '.join(map(str, director_list))
        print(f"\033[7;1mDirector\033[0m: {dir_str} ", end='\n\n')
    except:
        pass
    print(f"\033[7;1mkind\033[0m: {movie['kind']}", end='\n\n')
    try:
        print(f"\033[7;1mshort_Overview\033[0m: {movie['plot outline']}", end='\n\n')
    except:
        pass
    try:
        movie['plot']
        print(f"\033[7;1mThe summary plot for {movies[user_choice]['title']} is available!\033[0m:", end='\n\n')
        print(f"\033[7;1mDo you want to review the summary plot for {movies[user_choice]['title']}? \033[0m:", end='\n\n')
        plot = input(f"Do you want to review the summary plot for {movies[user_choice]['title']}? Enter yes to continue or no to exit: ", end='\n\n')
        if plot == "yes" and movie['plot'] != None:
            try:
                plot_list = []
                for i in range(len(movie['plot'])):
                    plot_list.append(movie['plot'][i])
                plot_str = ', '.join(map(str, plot_list))
                print(f"\033[7;1mPlot\033[0m: {plot_str}", end='\n\n')
        
            except:
                pass
    except:
        pass

def scraping_from_imdbpy():
    moviesDB = imdb.IMDb()
    top_250_movies = moviesDB.get_top250_movies()
    top_250_movies_dict = {}
    for i in range(len(top_250_movies)):
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
