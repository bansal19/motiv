# http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=8c87110c01e16c90602f4a850c810c6d&artist=cher&track=believe&format=json
"""Example API Call above"""
import pandas as pd
import requests
import json
import sys
from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    year = 1900
    artists = []
    songs = []
    years = []
    while year <= 2016:
        url = "https://tsort.info/music/yr" + str(year) + ".htm"
        data_request = Request(url)
        response = urlopen(data_request)
        html = response.read()

        response.close()

        soup = BeautifulSoup(html, 'html.parser')

        song_table = soup.find('table', {'class':'songlist'})

        for row in song_table.find_all('tr')[0:50]:
            artist = row.find_all("td", {"class":"art"})
            song = row.find_all("td", {"class":"tit"})
            song_year = row.find_all("td", {"class":"yer"})
            for item in artist:
                artists.append(item.get_text())
            for item in song:
                songs.append(item.get_text())
            for item in song_year:
                years.append(item.get_text())
        year += 1
    data = pd.DataFrame(list(zip(artists, songs, years)), columns=['Artist', 'Song', 'Year'])
    data.to_csv('100yearsData.csv')
