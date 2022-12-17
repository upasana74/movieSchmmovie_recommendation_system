# Project Title: Movie Schmmovie 
<img width="363" alt="Screen Shot 2022-12-17 at 04 42 22" src="https://user-images.githubusercontent.com/47816217/208235875-eb8264e8-b64d-44c6-9b9b-b2c664464e16.png">

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
1. Option 1: Search movie/tv shows:

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

2. Option 2: Search for the N top movies in a genre

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




-based on a graph based
