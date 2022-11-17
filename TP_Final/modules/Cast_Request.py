# github_request.py
import requests
import json


class GithubRequest:
    _base_url = "https://imdb-api.com/API"
    
    API_Key = "k_d39n9ukc"

    @classmethod
    def get_cast(cls):

        

        content_id =json.loads(requests.get(cls._base_url+"/FullCast"+"/"+cls.API_Key+"/"+choosen_film_ID).content)

        Cast=""
        
        # recupère les itm au travers de l'API movie
        title = content_id["title"]
        #print("Title :" + title)
        Cast += "Title :" + title + "\n"
        writer = content_id["writers"]["items"][0]["name"]
        #print("Writer :" + writer)
        Cast += "Writer :" + writer + "\n"

        director = content_id["directors"]["items"][0]["name"]
        #print("Directors :" + director)

        Cast += "Directors :" + director + "\n"

        #print("Actors : ")
        
        Cast += "Actors : " + "\n"
        
        for i in range(5):
            actors = content_id["actors"][i]["name"]
            character = content_id["actors"][i]["asCharacter"]
            image = content_id["actors"][i]["image"]
            #print(actors + " as " + character + " " + image)
            Cast+ actors + " as " + character + " " + image +"\n\n"
        return Cast




## commande pour jouer
movie_name = input("Please enter a movie name:\n")
print(GithubRequest.get_events(movie_name))