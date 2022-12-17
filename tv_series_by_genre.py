import imdb 

def tv_series():
    moviesDB = imdb.IMDb()
    genre_list = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Fantasy", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Sport", "Superhero", "Thriller", "War", "Western"]
    print("Genres available are as follows: ")
    idx = 1
    for i in genre_list:
        print(f"{idx}: {i}")
        idx += 1
    choose_a_genre_idx = int(input(" What is the genre you are interested in? Enter a number 1 - 24: "))
    top50_by_genre = moviesDB.get_top50_movies_by_genres(genre_list[choose_a_genre_idx-1])
    how_many = int(input("How many TV series do you want? Enter a number between 1 - 50: "))
    movie_idx = 1
    for i in range(how_many):
        year = top50_by_genre[i]['year']
        print(f"{movie_idx}) {top50_by_genre[i]} - {year}")
        movie_idx += 1
    user_selection = int(input(f"Which TV series' details you want to look for from the list above? Enter an integer 1-{how_many}: "))
    print(f"The details for {top50_by_genre[user_selection - 1]} are as follows: ")
    try:
        print("Rating : ", top50_by_genre[user_selection - 1]['rating'])
    except:
        pass
    # movie = top50_by_genre[user_selection - 1]
    try:
        print(f"Runtime : {top50_by_genre[user_selection - 1]['runtimes'][0]} mins")
    except:
        pass
    # print("imdbID : ", top50_by_genre[user_selection - 1]['imdbID'])
    cast_list = []
    for i in range(len(top50_by_genre[user_selection - 1]['cast'])):
        cast_list.append(top50_by_genre[user_selection - 1]['cast'][i])
    cast_str = ', '.join(map(str, cast_list))
    print("Cast: ", cast_str)
    try:
        director_list = []
        for i in range(len(top50_by_genre[user_selection - 1]['director'])):
            director_list.append(top50_by_genre[user_selection - 1]['cast'][i])
        dir_str = ', '.join(map(str, director_list))
        print("Director: ", dir_str)
    except:
        pass
    print("kind : ", top50_by_genre[user_selection - 1]['kind'])
    try:
        print("short_Overview: ", top50_by_genre[user_selection - 1]['plot outline'])
    except:
        pass
    try:
        top50_by_genre[user_selection - 1]['plot']
        print(f"The summary plot for {top50_by_genre[user_selection - 1]['title']} is available!")
        plot = input(f"Do you want to review the summary plot for {top50_by_genre[user_selection - 1]['title']}? Enter yes to continue or no to exit: ")
        if plot == "yes" and top50_by_genre[user_selection - 1]['plot'] != None:
            try:
                print("Plot : ", top50_by_genre[user_selection - 1]['plot'])
                # plot_list = []
                # for i in range(len(top50_by_genre[user_selection - 1]['plot'])):
                #     plot_list.append(top50_by_genre[user_selection - 1]['plot'][i])
                # plot_str = ', '.join(map(str, plot_list))
                # print("Plot: \n", plot_str)

        
            except:
                pass
    except:
        pass
