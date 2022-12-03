import modules.imdb_request_module as imdb_request_module
import modules.versioning_film_module as versioning_film_module

class VersioningFilmFacade:
    
    def get_versioning_film(Search):
        instance= imdb_request_module.ImdbRequest()
        instance.get_film(Name_Search=Search)
        response=[]
        title=(getattr(instance,'Film_Name'))
        id=(getattr(instance,'Film_id'))

        ratings =instance.get_globalrating()
        Cast = instance.get_cast()
        Poster=instance.get_poster()
        Trailer=instance.get_trailer()
        response.append(versioning_film_module.VersioningFilm(id,title,ratings,Cast,Poster,Trailer))

        return response   

        