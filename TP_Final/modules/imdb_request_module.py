import requests
import modules.response as response

class ImdbRequest:
    _base_url = "https://imdb-api.com/API"
        
    @classmethod
    def get_film(cls):
        Name_movie=input("Entrez le nom du film que vous recherchez : ")
        answer =  requests.get(cls._base_url+"/SearchMovie"+"/k_sb9w25u9"+"/"+Name_movie)
        
        return response.Response(status_code=answer.status_code, content=answer.json())

    @classmethod
    def get_rating(cls,id):
        answer =  requests.get(cls._base_url+"/Ratings"+"/k_t11w0wia"+"/"+id)
        
        return response.Response(status_code=answer.status_code, content=answer.json())    
        