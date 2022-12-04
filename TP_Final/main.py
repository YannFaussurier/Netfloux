import streamlit as st
import pandas as pd
import modules.versioning_film_facade as versioning_film_facade
import modules.versioning_film_module as versioning_film_module



def main():
    
    
    st.title('Welcome to NETFLOUX, our application dedicated to film search !')
    st.text('Here you\'ll be able to search any film you want through the imdb database.')
    st.text('our application will send back as many informations as possible about the film, as well as an average of all the ratings provided by IMDB')
    Search = st.text_input('Enter the name of the film you\'re searching for :', 'inception 2010')
    versioning_events = versioning_film_facade.VersioningFilmFacade.get_versioning_film(Search)

    for versioning_event in versioning_events:
        assert isinstance(versioning_event, versioning_film_module.VersioningFilm)
        print(versioning_event.title,'\n' ,versioning_event.rating,'\n',versioning_event.cast)
        
        st.image(versioning_event.Poster[0]['link'])
        url = versioning_event.Trailer
        st.write("check out the [Trailer](%s)" % url)
        
        st.text("you've chosen the movie/serie :")
        st.text(versioning_event.title)
        st.text(versioning_event.rating)
        for keys,values in versioning_event.cast.items():
            st.text(keys)
            st.image(values, width=200)
            

        

    
    

if __name__ == "__main__":
    
    main()