import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open("Src/auth.txt", "r") as f:
    [SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET] = f.read().split("\n")
    f.close()

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_code = input("Enter the playlist link: \n")
playlist_dict = sp.playlist(playlist_code)

song_list = []
artists_list = []

def get_playlist():
    
    songs = playlist_dict["tracks"]["total"]
    tracks = playlist_dict["tracks"]
    items = tracks["items"]
    offset=0
    item=0
        
    while item < songs:
        
        song = items[item-offset]["track"]["name"]
        artists = [k["name"] for k in items[item-offset]["track"]["artists"]]
        artists = ','.join(artists)
        song_list.append(song)
        artists_list.append(artists)
        if (item+1)%100 == 0:
            tracks = sp.next(tracks)
            items = tracks["items"]
            offset = item+1
            
        item+=1
        
        songs_data = list(zip(song_list, artists_list))

        with open("src/songs.txt", "w", encoding="utf-8") as f:
            for i in songs_data:
                f.write(str(i) + "\n")
        f.close()

get_playlist()