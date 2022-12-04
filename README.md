# Bienvenue sur le github de NETFLOUX

# Qu'est ce que netfloux ?

Netfloux est une application qui permet à un cinéphile curieux de se renseigner facilement sur n'importe quel film !

Grace à un système utilisant la base de donnée du siite web IMDB, vous n'avez qu'a taper le nom du film que vous cherchez, sélectionner votre film parmis la liste déroulante, et notre application vous renverra la note moyenne de tout les avis professionnels répertoriés sur IMDB directement, avec en bonus, des informations additionelles sur le film en question

# De quoi ai-je besoin pour faire fonctionner netfloux

Netfloux est une application assez simple développée en python qui n'a besoin que de quelques bibliothèques pour fonctionner :

-Json et Request, qui assurent l'interaction avec l'API de Imdb

-Streamlit, qui permet de générer le site web sur lequel vous utiliser l'application

Pour faire tourner l'application, placez vous dans le répertoire contenant le fichier main.py ainsi que le dossier "modules" puis entrez la commande suivante : "streamlit run main.py"
