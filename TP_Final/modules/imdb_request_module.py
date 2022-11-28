import requests
import modules.response as response
#import modules.Rating_request as Rating
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
        

        #cls.Name_movie_search=input("Enter the name of the movie you're searching for : ")
        cls.Name_movie_search=Name_Search
        # answer =  requests.get(cls._base_url+"/SearchMovie"+"/k_sb9w25u9"+"/"+cls.Name_movie_search)
        
        # return response.Response(status_code=answer.status_code, content=answer.json())
        # content retourne le contenu du film
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
        

        