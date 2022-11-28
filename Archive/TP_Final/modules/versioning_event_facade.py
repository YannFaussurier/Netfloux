import modules.imdb_request_module as imdb_request_module
import modules.versioning_event_module as versioning_event_module

class VersioningEventFacade:
    
    def get_versioning_film():
        instance= imdb_request_module.ImdbRequest()
        instance.get_film()
        response=[]
        title=(getattr(instance,'Film_Name'))
        id=(getattr(instance,'Film_id'))

        
        ratings =instance.get_globalrating()
        Cast = instance.get_cast()
        response.append(versioning_event_module.VersioningEvent(id,title,ratings,Cast))

        return response   

        