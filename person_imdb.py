import imdb

from PIL import Image
import urllib.request

# URL = 'http://www.w3schools.com/css/trolltunga.jpg'
def url_image_open(url):
    with urllib.request.urlopen(url) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())

    img = Image.open('temp.jpg')

    img.show()

def person_imdb():
    moviesDB = imdb.IMDb()
    print(f"\033[7;1mWhat is the movie/tv person you want to search a picture for?\033[0m ", end='\n\n')
    person_name = input("Enter the name of the person: ")
    persons = moviesDB.search_person(person_name)
    for idx, movie in enumerate(persons):
        title = movie["name"]
        print(f"{idx}: {title}")
    print(f"\033[7;1mWhich person's picture you want to look at?\033[0m", end='\n\n')
    user_choice = int(input(f"Enter 0-{idx} integer. "))
    try:
        print(f"\033[7;1mOpening picture of {persons[user_choice]}:\033[0m ", end='\n\n')
        try:
            url = persons[user_choice]['full-size headshot']
        except:
            url = persons[user_choice]['headshot']
        url_image_open(url)
    except:
        print(f"\033[7;1mSorry! Picture of this person unavailable!\033[0m", end='\n\n')


