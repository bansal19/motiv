"""Get lyrics for all songs"""
import lyricwikia
import pandas as pd

data = pd.read_csv('dreamylyrics.csv')

song_title = data.Title.tolist()
song_artist = data.Artists.tolist()


for i in range(len(data.values)):
    # print(song_artist[i], song_title[i])
    try:
        lyrics = lyricwikia.get_lyrics(song_artist[i], song_title[i])
        # print(lyrics)
        data.iloc[i, data.columns.get_loc('Lyrics')] = lyrics
    except:
        pass
