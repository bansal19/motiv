"""
All data from last.fm online
"""
import pandas as pd
import requests
import ssl
import subprocess
from interruptingcow import timeout

ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == '__main__':

    data = pd.read_csv("TrainingDataReal.csv")
    data.columns = ['Index', 'Artist', 'Title', 'Mood', 'Year', 'Genre', 'Lyrics', 'All Info']

    for i in range(13, len(data)):
        relevant_data = data.loc[i, 'All Info']
        artist_name = data.loc[i, 'Artist']
        track_name = data.loc[i, 'Title']

        youtube_index = relevant_data.find('url')
        end_index = relevant_data.find(', \'duration')

        print(relevant_data[youtube_index + 7: end_index-1])

        song_url = relevant_data[youtube_index + 7: end_index-1]
        # url = https://www.last.fm/music/Rihanna/_/Rockstar+101
        try:
            html = requests.get(song_url)

            index_begin = html.text.find('href=\"https://www.youtube.com')
            youtube_link = html.text[index_begin + 6: index_begin + 49]
            # print(youtube_link)

            # Run youtube-dl to download the youtube song with the link:
            new_track = artist_name + "--" + track_name
            location = "SongMP3_files/" + new_track + ".%(ext)s"

            process_call = ["youtube-dl", "--audio-format", "mp3", "-x", "-R 2", "--no-playlist", "-o", location, youtube_link]
            try:
                with timeout(10, exception=RuntimeError):
                    subprocess.run(process_call)
            except RuntimeError:
                print("didn't finish within 10 seconds")

        except:
            print("Can't find video")
