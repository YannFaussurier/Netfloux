import modules.imdb_request_module as imdb_request_module
import modules.versioning_event_module as versioning_event_module

class VersioningEventFacade:
    
    def get_versioning_film():
        movies =imdb_request_module.ImdbRequest.get_film().content['results']
        response=[]
        for movie in movies:
            ratings =imdb_request_module.ImdbRequest.get_rating(movie['id']).content
            
            response.append(versioning_event_module.VersioningEvent(movie['id'],movie['title'],movie['image'],ratings))

        return response   

        