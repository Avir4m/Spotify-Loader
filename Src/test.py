with open("src/songs.txt", "r", encoding="utf-8") as f :
    for line in f.readlines():
        song_data = line.rstrip().replace("'", "")
        song_name, song_artist = song_data.split(',', 1)
        song_name = song_name.replace("(", "").replace(")", "")
        song_artist = song_artist.replace("(", "").replace(")", "")[1:]
        print(song_name, "-", song_artist, "\n")
        f.close()