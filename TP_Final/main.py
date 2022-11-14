import modules.versioning_event_facade as versioning_event_facade
import modules.versioning_event_module as versioning_event_module

def main():
    versioning_events = versioning_event_facade.VersioningEventFacade.get_versioning_film()

    for versioning_event in versioning_events:
        assert isinstance(versioning_event, versioning_event_module.VersioningEvent)
        print(versioning_event.id,versioning_event.title,versioning_event.picture,versioning_event.rating)

    
    

if __name__ == "__main__":
    main()