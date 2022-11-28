import requests
import modules.response as response
#import modules.Rating_request as Rating
import json
import streamlit as st

class ImdbRequest:
    _base_url = "https://imdb-api.com/API"
    API_key="k_2c1txez2"
    Name_movie_search=""
    Film_id=""
    Film_Name=""

    @classmethod
    def get_film(cls):
        txt = st.text_input('Enter the name of the film you\'re searching for :', 'inception 2010')

        #cls.Name_movie_search=input("Enter the name of the movie you're searching for : ")
        cls.Name_movie_search=txt
        # answer =  requests.get(cls._base_url+"/SearchMovie"+"/k_sb9w25u9"+"/"+cls.Name_movie_search)
        
        # return response.Response(status_code=answer.status_code, content=answer.json())
        # content retourne le contenu du film
        content = json.loads(requests.get(cls._base_url+"/SearchMovie"+"/"+cls.API_key+"/"+cls.Name_movie_search).content)
        

        # Demande à l'utilisateur quel nom de film il souhaite parmi les propositions
        ###############################################################################################################
        # on propose les 3 premiers noms qui s'affichent
        if(len(content)>=6):
            options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title'],content['results'][4]['title'],content['results'][5]['title']]
        elif(len(content)==5):  
            options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title'],content['results'][4]['title']]
        elif(len(content)==4):  
            options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title']]
        elif(len(content)==3):  
            options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title']]    
        elif(len(content)==2):  
            options = [content['results'][0]['title'],content['results'][1]['title']]    
        else:
            options = [content['results'][0]['title']]   

        user_input = ''
        input_message = "Pick the movie you want :\n"
        st.text("Pick the movie you want :\n")
        list=[]
        for index, item in enumerate(options):
            input_message += f'{index+1}) {item}\n'
            list.append(f'{index+1}) {item}\n')

        choice=st.selectbox('choose the film you want : ',list)
        input_message += 'Your choice: '
        st.text('Your choice: ')

        #while user_input not in map(str, range(1, len(options) + 1)):
        #    user_input = input(input_message)

        user_input=choice
        #print('You picked: ' + options[int(user_input) - 1])
        # cls.film_id est l'ID du film choisi par l'utilisateur
        # [int(user_input) - 1] est le numéro choisi par l'utilisateur
        cls.Film_id = content["results"][int(user_input) - 1]["id"]
        cls.Film_Name= content['results'][int(user_input) - 1]['title']
        ###############################################################################################################


    @classmethod
    def get_globalrating(cls):
        
        #return requests.get(cls._base_url+"/SearchMovie"+"/k_5vnlaa7e"+"/inception 2010")

        # on appelle l'API ratings pour avoir les ratings
        # content_id est la variable qui stocke tous les ratings
        content_id =json.loads(requests.get(cls._base_url+"/Ratings"+"/"+cls.API_key+"/"+cls.Film_id).content)

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
        return f"The average rating of {cls.Film_Name} is : {final_note} "# {C} {B} " 
    
    @classmethod
    def get_cast(cls):


        content_id =json.loads(requests.get(cls._base_url+"/FullCast"+"/"+ cls.API_key +"/"+cls.Film_id).content)

        Cast="Cast\n\n"
        
        
        writer = content_id["writers"]["items"][0]["name"]
        #print("Writer :" + writer)
        Cast += "Writer :" + writer + "\n\n"

        director = content_id["directors"]["items"][0]["name"]
        #print("Directors :" + director)

        Cast += "Directors :" + director + "\n\n\n"

        #print("Actors : ")
        
        Cast += "Actors : " + "\n\n"
        
        for i in range(5):
            actors = content_id["actors"][i]["name"]
            character = content_id["actors"][i]["asCharacter"]
            image = content_id["actors"][i]["image"]
            #print(actors + " as " + character + " " + image)
            Cast+= actors + " as " + character + " " + image +"\n\n"

           
        return Cast

        