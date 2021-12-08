from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="88ed5aec8fb242a5907111e2cfe1f65b",
        client_secret="074cac04c36d4834a21ded89cba3caa7",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]



# Gets input date from user, regarding the date of which he/she wants their songs
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Gets the URL from which the songs will be pulled
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
billboard_site = response.text
soup = BeautifulSoup(billboard_site, "html.parser")

# Generates a list of all songs
song_names = [artist_tag.getText() for artist_tag in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)










