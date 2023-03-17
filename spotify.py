import yaml
import os
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os.path

def getTop10():

    with open('app_conf.yml', 'r') as f:
        app_config = yaml.safe_load(f.read())




    username = "tn7osj8so0qn99pcjy8701vgv"

    scope = ["user-read-currently-playing", "user-read-playback-state", "user-top-read", "user-library-read", "playlist-read-private"]


    token = util.prompt_for_user_token(username,scope=scope,client_id=app_config["client_id"],client_secret=app_config['client_secret'], redirect_uri="http://google.com/")

    if token:
        sp = spotipy.Spotify(auth=token)
        # Get user's top artists for spotify wrapped
        top_songs = sp.current_user_top_tracks(limit=10, time_range="medium_term")
        list = []
        
        for song in range(10):
            artist = top_songs['items'][song]['album']['artists'][0]["name"]
            image = top_songs['items'][song]['album']['images'][0]['url']
            song_name = top_songs['items'][song]['album']['name']
            artist_link = top_songs['items'][song]['album']['artists'][0]["external_urls"]["spotify"]
            
            list.append({
                "song": song_name,
                "artist": artist,
                "image": image, 
                "artist_link": artist_link
            
            })

    
        

        with open('top10_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Can't get token for", username)

