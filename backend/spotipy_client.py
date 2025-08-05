import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load env variables
load_dotenv()

# Spotify credentials
SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("REDIRECT_URI")

# Scope of API
SCOPE = "user-library-read playlist-read-private"


auth_manager = SpotifyOAuth(
    scope=SCOPE,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    cache_path=".spotifycache"
    )

sp = spotipy.Spotify(auth_manager=auth_manager)

def get_current_user():
    return sp.current_user()

def get_user_playlists(limit=10):
    return sp.current_user_playlists(limit=limit)