import imdb 

def tv_series():
    moviesDB = imdb.IMDb()
    genre_list = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Fantasy", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Sport", "Superhero", "Thriller", "War", "Western"]
    print(f"\033[7;1m;Genres available are as follows:\033[0m ", end='\n\n')
    idx = 1
    for i in genre_list:
        print(f"{idx}: {i}")
        idx += 1
    print(f"\033[7;1mWhat is the genre you are interested in?\033[0m ", end='\n\n')
    choose_a_genre_idx = int(input("Enter a number 1 - 24: "))
    top50_by_genre = moviesDB.get_top50_movies_by_genres(genre_list[choose_a_genre_idx-1])
    print(f"\033[7;1mHow many TV series do you want?\033[0m ", end='\n\n')
    how_many = int(input("How many TV series do you want? Enter a number between 1 - 50: "))
    movie_idx = 1
    for i in range(how_many):
        year = top50_by_genre[i]['year']
        print(f"{movie_idx}) {top50_by_genre[i]} - {year}")
        movie_idx += 1
    print(f"\033[7;1mWhich TV series' details you want to look for from the list above?\033[0m", end='\n\n')
    user_selection = int(input(f"Enter an integer 1-{how_many}: "))
    print(f"\033[7;1mThe details for {top50_by_genre[user_selection - 1]} are as follows:\033[0m ")
    try:
        print(f"\033[7;1mRating\033[0m: {top50_by_genre[user_selection - 1]['rating']}", end='\n\n')
    except:
        pass
    try:
        print(f"\033[7;1mRuntime\033[0m: {top50_by_genre[user_selection - 1]['runtimes'][0]} mins", end='\n\n')
    except:
        pass
    
    cast_list = []
    for i in range(len(top50_by_genre[user_selection - 1]['cast'])):
        cast_list.append(top50_by_genre[user_selection - 1]['cast'][i])
    cast_str = ', '.join(map(str, cast_list))
    print(f"\033[7;1mCast\033[0m: {cast_str}", end='\n\n')
    try:
        director_list = []
        for i in range(len(top50_by_genre[user_selection - 1]['director'])):
            director_list.append(top50_by_genre[user_selection - 1]['cast'][i])
        dir_str = ', '.join(map(str, director_list))
        print(f"\033[7;1mDirector\033[0m: {dir_str} ", end='\n\n')
    except:
        pass
    print(f"\033[7;1mkind\033[0m: {top50_by_genre[user_selection - 1]['kind']}", end='\n\n')
    try:
        print(f"\033[7;1mshort_Overview\033[0m: {top50_by_genre[user_selection - 1]['plot outline']}", end='\n\n')
    except:
        pass
    try:
        top50_by_genre[user_selection - 1]['plot']
        print(f"\033[7;1mThe summary plot for {top50_by_genre[user_selection - 1]['title']} is available!\033[0m", end='\n\n')
        print(f"\033[7;1mDo you want to review the summary plot for {top50_by_genre[user_selection - 1]['title']}?\033[0m", end='\n\n')
        plot = input(f"Enter yes to continue or no to exit: ")
        if plot == "yes" and top50_by_genre[user_selection - 1]['plot'] != None:
            try:
                print(f"\033[7;1mPlot: {top50_by_genre[user_selection - 1]['plot']}\033[0m", end='\n\n')
            except:
                pass
    except:
        pass
