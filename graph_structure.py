import json

genre_list = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Fantasy", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Sport", "Superhero", "Thriller", "War", "Western", "Family", "Film-Noir"]
rating_list = ["8.0-8.2", "8.2-8.4", "8.4-8.6", "8.6-8.8", "8.8-9.0", "9.0-9.2"]


def create_genre_rating_info_node():
    """
    stores dict in the format: { "g1": "Action", "g2": "Adventure", ....."r6": "9.0-9.2"}
    """
    genre_rating_info_node = {}
    for i in range(len(genre_list)):
        parent_key = 'g' + str(i+1)
        genre_rating_info_node[parent_key] = genre_list[i]
    for i in range(len(rating_list)):
        parent_key = 'r' + str(i+1)
        genre_rating_info_node[parent_key] = rating_list[i]
    return genre_rating_info_node

def create_adjacency_dict_child_nodes():
    data_dict = create_movie_info_node()
    adjacency_dict = {}
    inverted_genre_rating_info_dict = invert_keys_values_dict(create_genre_rating_info_node()) 

    for i, data in data_dict.items():
        each_item_list = []
        genres_each_movie = (data['genre'].split(","))
        genres_each_movie = [i.lstrip() for i in genres_each_movie]
        for each_genre in genres_each_movie:
            each_item_list.append(inverted_genre_rating_info_dict[each_genre])
        # print(each_item_list)
        if data['rating'] < 8.2:
            each_item_list.append(rating_list[0])
        elif data['rating'] < 8.4:
            each_item_list.append(rating_list[1])
        elif data['rating'] < 8.6:
            each_item_list.append(rating_list[2])
        elif data['rating'] < 8.8:
            each_item_list.append(rating_list[3])
        elif data['rating'] < 9.0:
            each_item_list.append(rating_list[4])
        elif data['rating'] <= 9.2:
            each_item_list.append(rating_list[5])
        adjacency_dict[i] = each_item_list
    return adjacency_dict

def create_movie_info_node(): 
    """
    # returns dict for cache movies in the format: {"1": {"title": ...,
                                                        "top_250 rank": ...,
                                                        "year": ...,
                                                        "rating": ...,
                                                        "votes": ...,
                                                        "genre": ...",
                                                        "kind": ...}, }
    """
    with open('./movies_cache.json', 'r') as file:
        data = json.load(file)

    movie_node_info = {}
    for i, (_, value) in enumerate(data.items()):
        new_key = 'c' + str(i + 1)
        movie_node_info[new_key] = value
    return movie_node_info

def invert_keys_values_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        new_dict[value] = key
    return new_dict

def create_dict_from_json():
    with open('./movies_cache.json', 'r') as file:
        data = json.load(file)
    return data

def graph_implementation():
    idx = 1
    for i in genre_list:
        print(f"{idx}) {i}")
        idx += 1
    print(f"\033[7;1mChoose the integers for the genres you want in the format of space separted intergers like 1 2 3.\033[0m ", end='\n\n')
    input_genres = input(f"Enter those integers in the format of space separted intergers like 1 2 3: ")
    input_genres = input_genres.split(" ")
    genre = [genre_list[int(i)-1] for i in input_genres]
    idx_r = 1
    for i in rating_list:
        print(f"{idx_r}) {i}")
        idx_r += 1
    print(f"\033[7;1mChoose the integers for the IMDb rating range you want in the format of space separted intergers like 1 2 3.\033[0m ", end='\n\n')
    input_rating = input(f"Enter the integers in the format of space separted intergers like 1 2 3: ")
    input_rating = input_rating.split(" ")
    rating = [rating_list[int(i)-1] for i in input_rating]

    inverse_genre_rating_node = invert_keys_values_dict(create_genre_rating_info_node())

    adj_list = create_adjacency_dict_child_nodes()
    with open("./graph_structure_in_json.json", "w+") as f:
        json.dump(adj_list, f, indent=1)

    active_list = []
    
    for gen in genre:
        active_list.append(inverse_genre_rating_node[gen])

    for rat in rating:
        active_list.append(inverse_genre_rating_node[rat]) 
    
    # active list = ["g1", "g2", .... ,"r1", "r2", ....]
    results_rating, results_genre = [],[]
    for idx, (key, val) in enumerate(adj_list.items()):
        if(key[0]!="c"):
            continue
        for vav in active_list:
            if(vav in val and vav[0]=="g"):
                results_genre.append(key)
            else:
                results_rating.append(key)
            

    #results_genre, results_rating = ["c12", "c32", "c121"], ["c32","c34"]
    final_res = list(set(results_rating) & set(results_genre)) # ["c1","c32"]
    with open('./movies_cache.json', 'r') as file:
        data = json.load(file)
    
    data_dict_keys = list(data.keys())
    final_res = [int(i[1:]) for i in final_res]
    # print(final_res)
    while True:
        try:
            print(f"\033[7;1mHow many movie recommendations do you want? \033[0m ", end='\n\n')
            user_number = input(f"Enter an integer 1-{len(final_res)}. If you want the full recommendation list, enter 'full'. To exit enter 'exit': ")
            if user_number == 'exit':
                break
            if user_number == "full":
                for idx, i in enumerate(final_res):
                    print(f"{idx+1}) {data[data_dict_keys[int(i-1)]]['title']}")
                break
            elif int(user_number) <= len(final_res) and int(user_number) >= 1:
                for idx, i in enumerate(final_res[:int(user_number)]):
                        print(f"{idx+1}) {data[data_dict_keys[int(i-1)]]['title']}")
                break

            else:
                try:
                    for idx, i in enumerate(final_res):
                        print(f"{idx+1}) {data[data_dict_keys[int(i-1)]]['title']}- {data[data_dict_keys[int(i-1)]]['year']}")

                except:
                    wrong_in = input(f"\033[7;1mWrong input! Try again. Enter 'yes' to continue, 'exit' to exit:\033[0m ", end='\n\n')
                    if wrong_in == "exit":
                        break
                    elif wrong_in == "yes":
                        continue
        except:
            print(f"\033[7;1mWrong input!\033[0m", end='\n\n')
            continue