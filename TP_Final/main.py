import modules.versioning_event_facade as versioning_event_facade
import modules.versioning_event_module as versioning_event_module

def main():
    versioning_events = versioning_event_facade.VersioningEventFacade.get_versioning_film()

    for versioning_event in versioning_events:
        assert isinstance(versioning_event, versioning_event_module.VersioningEvent)
        print(versioning_event.title,'\n' ,versioning_event.rating,'\n',versioning_event.cast)

    
    

if __name__ == "__main__":
    main()