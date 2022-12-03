import requests
import json
import streamlit as st


class ImdbRequest:
    _base_url = "https://imdb-api.com/API"
    API_key="k_t11w0wia"
    Name_movie_search=""
    Film_id=""
    Film_Name=""

    
    @classmethod
    def get_film(cls,Name_Search):
        #Cette fonction ve récupérer le titre du film ainsi que son id, l'id est une information essentielle pour pouvoir accéder
        #aux autres informations du film à travers les autres fonction

        cls.Name_movie_search=Name_Search
        content = json.loads(requests.get(cls._base_url+"/SearchMovie"+"/"+cls.API_key+"/"+cls.Name_movie_search).content)
        
        
        # Demande à l'utilisateur quel nom de film il souhaite parmi les propositions
        ###############################################################################################################
        # on propose les 6 premiers noms qui s'affichent
        try:
            if(len(content['results'])>=6):
                options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title'],content['results'][4]['title'],content['results'][5]['title']]
            elif(len(content['results'])==5):  
                options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title'],content['results'][4]['title']]
            elif(len(content['results'])==4):  
                options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title'],content['results'][3]['title']]
            elif(len(content['results'])==3):  
                options = [content['results'][0]['title'],content['results'][1]['title'],content['results'][2]['title']]    
            elif(len(content['results'])==2):  
                options = [content['results'][0]['title'],content['results'][1]['title']]    
            else:
                options = [content['results'][0]['title']]  
              
        except TypeError:
            print(content)
            


        
        
        list=[]
        for index, item in enumerate(options):
            list.append(f'{index+1}) {item}\n')

        choice=st.selectbox('choose the film you want : ',list)

        #st.text(content["results"][int(user_input) - 1]["id"])
        cls.Film_id = content["results"][list.index(choice)]["id"]
        cls.Film_Name= content['results'][list.index(choice)]['title']
        ###############################################################################################################

    
    @classmethod
    def get_globalrating(cls):
        
        content_id =json.loads(requests.get(cls._base_url+"/Ratings"+"/"+cls.API_key+"/"+cls.Film_id).content)

        # on va faire une transformation pour avoir une moyenne globale
        # float et int car c'est soit noté sur 100 soit sur 10


        note_imDb = content_id["imDb"]
        note_metacritic = content_id["metacritic"]
        note_theMovieDb = content_id["theMovieDb"]
        note_rottenTomatoes = content_id["rottenTomatoes"]
        note_filmAffinity = content_id["filmAffinity"]

        ratings=[note_imDb,note_metacritic,note_theMovieDb,note_rottenTomatoes,note_filmAffinity]


        # Conversion de la note en valeur numérique
        for rating in range(len(ratings)):
            if ratings[rating]=="":   #len(ratings[rating])==0:
                ratings[rating]= ratings[rating] + "0"


        # Conversion de la liste en liste de valeurs numériques
        ratings = list(map(float, ratings))

        #Selon les sites, les métriques pour noter les film diffèrent, nous effectuons pour que toute les note soient sur 10 (IMDB et ROTTENTOMATOE Sont sur 100)
        ratings[1]=ratings[1]/10
        ratings[3]=ratings[3]/10

        # Calcul de la moyenne de toute les notes

        final_note= sum(ratings)/len(ratings)
        return f"The average rating of {cls.Film_Name} is : {final_note} "# {C} {B} " 

        
    @classmethod
    def get_cast(cls):


        content_id =json.loads(requests.get(cls._base_url+"/FullCast"+"/"+ cls.API_key +"/"+cls.Film_id).content)

        Cast="Cast of the movie : \n\n"
        
        
        writer = content_id["writers"]["items"][0]["name"]
        #print("Writer :" + writer)
        Cast += "Writer :" + writer + "\n\n"

        director = content_id["directors"]["items"][0]["name"]
        #print("Directors :" + director)

        Cast += "Directors :" + director + "\n\n\n"

        #print("Actors : ")
        
        Cast += "Actors : " + "\n\n"
        ListImage=[]
        Cast=[]
        
        for i in range(7):
            actors = content_id["actors"][i]["name"]
            character = content_id["actors"][i]["asCharacter"]
            image = content_id["actors"][i]["image"]
            #print(actors + " as " + character + " " + image)
            Cast.append(actors + " as " + character + "\n\n")
            ListImage.append(image)

        CastDict=dict(zip(Cast,ListImage))


           
        return CastDict

    @classmethod    
    def get_poster(cls):
        content_poster = json.loads(requests.get(cls._base_url+"/Posters/"+cls.API_key+"/"+cls.Film_id).content)
        poster = content_poster['posters']

        
        return poster

    @classmethod    
    def get_trailer(cls):
        
        content_trailer = json.loads(requests.get(cls._base_url+"/Trailer/"+cls.API_key+"/"+cls.Film_id).content)
        trailer = content_trailer['link']

        return trailer
        

        