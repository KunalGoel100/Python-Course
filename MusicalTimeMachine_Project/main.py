import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2000-10-11"
ClientID = "d5e85691859c44d09201ca1aa1229927"
ClientSecret = "9c15d519f6054ec4ae3116f792863616"
ClientRedirect_Url = "https://example.com/callback"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"}



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ClientID",
                                               client_secret="ClientSecret",
                                               redirect_uri="ClientRedirect_Url",
                                               scope="user-library-read"))
artist_url = "spotify:artist:3eDT9fwXKuHWFvgZaaYC5v"

results = sp.artist_albums(artist_url, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])