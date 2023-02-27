import yaml
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = app_config['client_id'],
                                                client_secret = app_config['client_secret'],
                                                redirect_uri = app_config['redirect_uri'],
                                                scope = app_config['scope']))