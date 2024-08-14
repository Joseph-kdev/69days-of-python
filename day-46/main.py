from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

year_prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f'https://www.billboard.com/charts/hot-100/{year_prompt}/')

soup = BeautifulSoup(response.text, "html.parser")

song_title = soup.select(".o-chart-results-list-row-container .o-chart-results-list__item h3")
returned_songs = []

for song in song_title:
    song_title = song.getText()
    remove_esc = ''.join([chr(i) for i in range(1, 32)])
    returned_songs.append(song_title.translate(str.maketrans('', '', remove_esc)))
 
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = year_prompt.split("-")[0]
playlist = sp.user_playlist_create(user=user_id, name=f"{year_prompt} Billboard 100", public=False, description="playlist created with python code")

for song in returned_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
        
added = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(added)
