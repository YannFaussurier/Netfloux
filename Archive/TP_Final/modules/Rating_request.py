# github_request.py
#pip install requests
#https://imdb-api.com/Identity/Last7Days

# github_request.py
import requests
import json

# get_globalrating() ask to the user the film he is interested in, display the 5 first choices, 
# then the Film ID assigned to the film chosen is used to find all the ratings of this film.
# Finally, the ratings are converted from string to float, empty ratings are set to 0, and put over 10
# The user gets the average ratings of all the sites.
class RatingRequest:
    _base_url = "https://imdb-api.com/API"
        
    @classmethod
    def get_globalrating(cls,film_name):
        
        #return requests.get(cls._base_url+"/SearchMovie"+"/k_5vnlaa7e"+"/inception 2010")

        # content retourne le contenu du film
        content = json.loads(requests.get(cls._base_url+"/SearchMovie"+"/k_2c1txez2/"+film_name).content)
        print(content)
        ###############################################################################################################
        # recupere l'id 1 au travers de l'API movie
        film_ID=content["results"][1]["id"]
        ###############################################################################################################


        # Demande à l'utilisateur quel nom de film il souhaite parmi les propositions
        ###############################################################################################################
        # on propose les 3 premiers noms qui s'affichent
        options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][3]['title'],content['results'][4]['title'],content['results'][5]['title']]
        user_input = ''
        input_message = "Pick the movie you want :\n"

        for index, item in enumerate(options):
            input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while user_input not in map(str, range(1, len(options) + 1)):
            user_input = input(input_message)

        print('You picked: ' + options[int(user_input) - 1])
        # choosen_film_ID est l'ID du film choisi par l'utilisateur
        # [int(user_input) - 1] est le numéro choisi par l'utilisateur
        choosen_film_ID = content["results"][int(user_input) - 1]["id"]
        ###############################################################################################################


        # on appelle l'API ratings pour avoir les ratings
        # content_id est la variable qui stocke tous les ratings
        content_id =json.loads(requests.get(cls._base_url+"/Ratings"+"/k_5vnlaa7e/"+choosen_film_ID).content)

        # on va faire une transformation pour avoir une moyenne globale
        # float et int car c'est soit noté sur 100 soit sur 10


        note_imDb = content_id["imDb"]
        note_metacritic = content_id["metacritic"]
        note_theMovieDb = content_id["theMovieDb"]
        note_rottenTomatoes = content_id["rottenTomatoes"]
        note_filmAffinity = content_id["filmAffinity"]

        ratings=[note_imDb,note_metacritic,note_theMovieDb,note_rottenTomatoes,note_filmAffinity]


        # turn the empty string rating into a numerical value
        for rating in range(len(ratings)):
            if ratings[rating]=="":   #len(ratings[rating])==0:
                ratings[rating]= ratings[rating] + "0"
                #C=print(ratings[rating])
                # To be sure that the loop detects with a null rating
                #B= print('is NULL')

        # convert the list into a list of numerical values
        ratings = list(map(float, ratings))

        # note_metacritic and note_rottenTomatoes are rated over 100 so we put them over 10
        ratings[1]=ratings[1]/10
        ratings[3]=ratings[3]/10

        # the final list with transformed ratings
        # print(ratings)

        final_note= sum(ratings)/len(ratings)
        return f"The average rating of {content['results'][int(user_input) - 1]['title']} is : {final_note} "# {C} {B} "


## commande pour jouer
movie_name = input("Please enter a movie name:\n")
print(RatingRequest.get_globalrating(movie_name))
