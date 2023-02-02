# Project Title: MovieSchmmovie ([demo](https://drive.google.com/file/d/1Q7EEZ73ioP1CTyWMHOcbtb4DmZhpanDi/view?usp=share_link) | [report](https://drive.google.com/file/d/18udynkYEi9x_4hx5F8cDUWbGo4A0cAUt/view?usp=share_link))

<img width="230" alt="Screen Shot 2022-12-17 at 05 05 06" src="https://user-images.githubusercontent.com/47816217/208236610-4d041f60-30d4-473b-94bc-99b04a69384e.png">


MovieSchmmovie is an interactive graph-based IMDb based movie and TV series recommendation system. It is an user friendly console-based program to 
recommend movies for a certain preference of movie/TV show genre and IMDb. To offer some flexility to the user, it also offers to choose from the following options:

1. Search for a movie by it's name 

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

This is the part which makes use of the cached data in the file `movies_cache.json`, hence the comparitively faster response time
It asks for the genres and the IMDb rating you want and also the number of movies you want to be recommended. It uses a graph structure to 
store the movie information and recommend movies to the user depending on the node connections.


### Accessing the APIs

1. The [IMDbPY API](https://pypi.org/project/IMDbPY/) is publicly available online and does not require any api key to activate it.
2. The [OMDB API](https://www.omdbapi.com/) is also publicly available but you need to go to [this website](https://www.omdbapi.com/) and request 
    for an API key. Then you have to go to your mailbox to activate the key. You will need this key to use the omdb api to access movie data.
3. [Kaggle dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) also has good metadata for movies.

### Option 5: Person search to view their image

On selecting this option, you can type any person's name and select the person from the search results. On choosing a particular result, the picture of that personm pops up if it is in the IMDb database.

## Data Structure

1. The entire movies and TV series data is stored in the form of cache in `movies_cache.json`. A visualization of the nodes connection is as follows: 
(used python script in `nodes_visualize_adjacency_list.py` to create this plot)
![graph_nodes_1](https://user-images.githubusercontent.com/47816217/208280044-3ee41969-417a-4991-ba6b-a5b3d9149b8f.png)

2. A graph structure is used to store this dataset in order to retrieve nodes when the recommendation system is active.
Python file that constructs the graph: `graph_structure.py` (pictures are shown step by step during explanation). I have constructed an 
undirected graph by treating each movie as a separate child node and tokenizing each of the movies as nodes ‘c1’, ‘c2’, ‘c3’, ... etc.

3. Each of the movie nodes is connected to other nodes and stored in the form of a graph. For example, each if a movie named “Lol” has genres as comedy, thriller, romance and imdb of 8.4 in the cached dataset, then node “Lol” in the form of ‘c#’ is mapped to the nodes representing genres comedy, thriller, romance in the form of ‘g#’ and also connected to the node “8.4-8.6” rating node.
Mapping example:
{“c#”: [g#, g#, g#, “8.4-8.6”]
…}

4. Every genre and rating is tokenized as parent nodes. Each genre is tokenized as ‘g1’, ‘g2’, ‘g3’, ….. And each rating is tokenized with respect to it’s IMDb rating range  ["8.0-8.2", "8.2-8.4", "8.4-8.6", "8.6-8.8", "8.8-9.0", "9.0-9.2"]

5. Just like each child movie node is mapped to each of it’s genres and rating, each individual genre is also connected to it’s related child node. Same way each of the individual rating is mapped to it’s related child node.

6. Hence each of the movie nodes are connected to it’s genre nodes and imdb rating window nodes and vice versa.

The rest of the details about the graph is present in the final project report.
