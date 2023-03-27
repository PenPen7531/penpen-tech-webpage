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




    username = app_config["username"]

    scope = app_config['scope']


    token = util.prompt_for_user_token(username,scope=scope,client_id=app_config["client_id"],client_secret=app_config['client_secret'], redirect_uri="http://google.com/")

    if token:
        sp = spotipy.Spotify(auth=token)
        # Get user's top artists for spotify wrapped
        top_songs = sp.current_user_top_tracks(limit=10, time_range="medium_term")
        list = []
        current_track = sp.currently_playing()
        print(current_track)
        # print(top_songs['items'][0])
        for song in range(10):
            
            artist = top_songs['items'][song]['album']['artists'][0]["name"]
            image = top_songs['items'][song]['album']['images'][0]['url']
            song_name = top_songs['items'][song]['name']
            artist_link = top_songs['items'][song]['album']['artists'][0]["external_urls"]["spotify"]
            song_mp3 = top_songs['items'][song]['preview_url']
            list.append({
                "song": song_name,
                "artist": artist,
                "image": image, 
                "artist_link": artist_link,
                "mp3": song_mp3
            })
            
           

    
        

        with open('top10_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Can't get token for", username)

if __name__ == "__main__":
    getTop10()

