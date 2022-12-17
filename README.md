# Project Title: Movie Schmmovie 

<img width="230" alt="Screen Shot 2022-12-17 at 05 05 06" src="https://user-images.githubusercontent.com/47816217/208236610-4d041f60-30d4-473b-94bc-99b04a69384e.png">


MovieSchmmovie is an interactive graph-based IMDb based movie and TV series recommendation system. It is an user friendly console-based program to 
recommend movies for a certain preference of movie/TV show genre and IMDb. To offer some flebility to the user, it also offers to choose from the following options:

1. Search for a movie/TV series by it's name
2. Search for the N top movies in a genre
3. Search for the top N TV series for a genre
4. Movie recommendation on the basis of genre and IMDb rating
5. Person search to view their image

## Description

MovieSchmmovie is a python-based program that makes use of data scraped from IMDb and also uses IMDb APIs like IMDbPY (open source) and also API key requiring apis like [OMDb](https://www.omdbapi.com/). The program is based on a graph based algorithm where every node is connected to the other nodes
which are related to it, for eg. a movie node with a genre thriller, drama with IMDb rating of 8.2 is connected to the nodes "Thriller", "Drama" and "8.2-8.4". 

## Instructions to run the code
1. Download the code files.
2. cd to the directory containing the code fields on the terminal.
3. Paste the following code and press enter:
```
python project.py
```
### Dependencies
1. python 2.7 and above
2. python
3. imdb
4. time
5. urllib.request
6. requests
7. json
8. platform   
9. subprocess  
10. urllib.request
11. pyglet
12. sys
13. os
14. PIL

Install all the dependencies by pasting the code below on the python terminal and pressing enter: 

```
pip install -r requirements.txt
```

## Instructions on the options:
### Option 1: Search movie/tv shows:

On selecting this option, you can enter a movie name, select a movie from the movie search results and view the following options:
1. Movie year
2. Movie Genres
3. IMDb rating
4. Runtime 
5. IMDbID
6. Cast
7. Directors
8. short_Overview
9. Summary plot

### Option 2: Search for the N top movies in a genre

On selecting this option, you can select a genre from below to display howsoever many movies you want in that genre:
1. Action
2. Adventure
3. Animation
4. Biography
5. Comedy
6. Crime
7. Drama
8. Fantasy
9. History
10. Horror
11. Music
12. Musical
13. Mystery
14. Romance
15. Sci-Fi
16. Sport
17. Superhero
18. Thriller
19. War
20. Western

You can also select a movie in the selection to display the movie details.

### Option 3: Search for the top N TV series for a genre

Similar to Option 2, but this is with TV series not movies as option 2

### Option 4: Movie recommendation on the basis of genre and IMDb rating

This is the part which makes use of the cached data in the file `top250movies.json`, hence the comparitively faster response time
It asks for the genres and the IMDb rating you want and also the number of movies you want to be recommended. It uses a graph structure to 
store the movie information and recommend movies to the user depending on the node connections.

### Accessing the APIs

1. The [IMDbPY API](https://pypi.org/project/IMDbPY/) is publicly available online and does not require any api key to activate it.
2. The [OMDB API](https://www.omdbapi.com/) is also publicly available but you need to go to [this website](https://www.omdbapi.com/) and request 
    for an API key. Then you have to go to your mailbox to activate the key. You will need this key to use the omdb api to access movie data.
3. [Kaggle dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) also has good metadata for movies.


