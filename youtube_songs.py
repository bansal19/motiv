# Downloading mp3 files from youtube-dl
# Example call:
# youtube-dl --audio-format mp3 -x --no-playlist -o "./Youtube_songs/jonasbrothers.%(ext)s"  https://www.youtube.com/watch?v=CnAmeh0-E-U
import subprocess
import pandas as pd

# subprocess.run(["ls", "-l"])

data = pd.read_csv("TrainingDataLINKS.csv")
data.columns = ['Index', 'Artist', 'Title', 'Mood', 'Year', 'Genre', 'Lyrics', 'All Info', 'Youtube Link']


for i in range(len(data)):
    artist_name = data.loc[i, 'Artist']
    track_name = data.loc[i, 'Title']
    track_link = data.loc[i, 'Youtube Link']

    new_track = artist_name + "-" + track_name
    location = "Youtube_songs/" + new_track + ".%(ext)s"

    process_call = ["youtube-dl", "--audio-format", "mp3", "-x", "--no-playlist", "-o", location, track_link]
    subprocess.run(process_call)
