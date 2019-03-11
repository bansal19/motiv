# http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=8c87110c01e16c90602f4a850c810c6d&artist=cher&track=believe&format=json
"""Example API Call above"""
import pandas as pd
import requests
import json
import sys
from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':

    data = pd.read_csv("TrainingDataReal.csv")
    data.columns = ['Index', 'Artist', 'Title', 'Mood', 'Year', 'Genre', 'Lyrics', 'All Info']

    youtube_link = []
    for i in range(len(data)):
        artist_name = data.loc[i, 'Artist']
        track_name = data.loc[i, 'Title'].lower().strip()

        artist = artist_name.replace(" ", "+")
        track = track_name.replace(" ", "+")

        url = "https://www.youtube.com/results?search_query=" + artist + "+" + track
        # url = "https://www.youtube.com/results?search_query=diamonds+rihanna"
        html = requests.get(url)

        index_begin = html.text.find("href=\"/watch?v=")
        sub_text = html.text[index_begin: index_begin + 27]
        # print(sub_text)

        sub_link = sub_text[6:-1]
        song_link = "https://www.youtube.com" + sub_link

        print(song_link)
        youtube_link.append(song_link)

    data['Youtube Link'] = youtube_link
    data.to_csv('TrainingDataLINKS.csv')
