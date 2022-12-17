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
    person_name = input("What is the movie/tv person you want to search a picture for? ")
    persons = moviesDB.search_person(person_name)
    for idx, movie in enumerate(persons):
        title = movie["name"]
        print(f"{idx}: {title}")
    user_choice = int(input(f"Which person's picture you want to look at? Enter 0-{idx} integer. "))
    try:
        print(f"Opening picture of {persons[user_choice]}: ")
        try:
            url = persons[user_choice]['full-size headshot']
        except:
            url = persons[user_choice]['headshot']
        url_image_open(url)
    except:
        print("Sorry! Picture of this person unavailable!")


